#! /usr/bin/python3.12
# Author : Anupam Biswas
# Date : 23 september 2024
# app name : 2 ass fuck Authenticator.
from PyQt5.uic.Compiler.qtproxies import QtCore


def info():
    __Author__ = 'Anupam Biswas'
    __version__ = '1.2.4'
    __date__ = '23 september 2024'
    __app_name__ = '2af Authenticator.'

import json
import os
import sys
import time
from datetime import datetime

import pyotp
from PyQt5 import QtGui, QtMultimedia
from PyQt5.QtCore import QTimer, Qt, QPoint, QUrl, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect, QGraphicsDropShadowEffect, QMessageBox, QLabel


from ui.authenticator import Ui_authenticator
from utils._utils_config import AuthFileManager
from icon import resource

date = datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
username = os.getlogin()

configuration = AuthFileManager()

def load_auth_data(filepath=configuration.get_auth_path()):
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            json.dump({username: {}}, file)  # Default empty structure
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f""
            f"Please check your "
            f"{
            filepath
            } file," 
            f"it's json based file "
            f" please be careful while you  edit this."
            )
        return None


class authenticator(Ui_authenticator, QWidget):
    def __init__(self, authdata):
        super(authenticator, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"[2fA] Authenticator app {username}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.icon.setPixmap(QtGui.QPixmap(":/icon/2fa.png"))

        # Setup sound effect
        self.sound = QtMultimedia.QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("aud/click.wav"))  # Place click.wav in your script's directory
        self.sound.setVolume(0.9)

        # set data to Combobox from .auth data.
        config_icon_path = os.path.expanduser("~/config/authenticator/icons")
        locations = authdata.get(username, {})
        cur_path = os.getcwd()

        for location in locations.keys():
            user_icon_path = os.path.join(config_icon_path, f"{location}_icon.png")
            default_icon_path = os.path.join(cur_path, "icon", f"{location}_icon.png")

            if os.path.exists(user_icon_path):
                icon_path = user_icon_path
            else:
                icon_path = default_icon_path

            icon = QtGui.QIcon(icon_path)
            self.sites_comboBox.addItem(icon, location)

        # set Enable Mumbai as default site for authenticator.
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.otp.setStyleSheet(u"color: rgb(56, 242, 227);")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QtGui.QColor(56, 242, 227))
        shadow.setOffset(0, 0)

        # Adding shadow to the label
        self.otp.setGraphicsEffect(shadow)

        self.pushButton.clicked.connect(self.copy_totp)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_totp)
        self.timer.start(1000)

        self.toggle_sites()
        self.sites_comboBox.currentIndexChanged.connect(self.toggle_sites)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    @staticmethod
    def seceret_code(site):
        with open(configuration.get_auth_path(), 'r') as data:
            auth = json.load(data)
        return auth[username][site]

    def toggle_sites(self):
        _location = self.sites_comboBox.currentText()
        self.generate_totp(secret=self.seceret_code(_location))


    def generate_totp(self, secret=None):
        # Get the secret from the QRCode, which is shared by your Organization.
        if not secret:
            QMessageBox.warning(self, "Error", "No secret provided.")
            return

        # Create a TOTP object
        self.totp = pyotp.TOTP(secret)
        self.update_totp()

    def update_totp(self):
        if hasattr(self, 'totp'):
            # Get the current time in seconds since last update.
            current_time = int(time.time())
            # Calculate how much time is left in the current 60-second window
            time_remaining = 60 - (current_time % 60)

            # Update the progress bar
            self.time_check.setText(str(time_remaining))

            # Only regenerate TOTP at the start of a new time window
            if time_remaining == 60:
                # Get the current TOTP token
                totp_token = self.totp.now()
                self.otp.setText(f"{totp_token}")
            else:
                # Update the countdown, but keep the current token
                current_token = self.totp.now()
                self.otp.setText(f"{current_token}")

    def copy_totp(self):
        totp = self.otp.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(str(totp))
        self.sound.play()

        # If an overlay already exists, remove it before creating a new one
        if hasattr(self, "overlay_label") and self.overlay_label is not None:
            self.overlay_label.deleteLater()
            self.overlay_label = None

        # Create a new overlay label
        self.overlay_label = QLabel("Copied", self.pushButton)
        self.overlay_label.setAlignment(Qt.AlignCenter)
        self.overlay_label.setFont(self.pushButton.font())
        self.overlay_label.setStyleSheet("color: black; background: transparent; border: none;")
        self.overlay_label.resize(self.pushButton.size())
        self.overlay_label.move(60, 0)
        self.overlay_label.show()

        # Create and apply opacity effect
        self.text_opacity = QGraphicsOpacityEffect()
        self.overlay_label.setGraphicsEffect(self.text_opacity)
        self.text_opacity.setOpacity(0.7)

        # Create fade-out animation
        self.fade_out_text = QPropertyAnimation(self.text_opacity, b"opacity")
        self.fade_out_text.setDuration(800)
        self.fade_out_text.setStartValue(0.7)
        self.fade_out_text.setEndValue(0)
        self.fade_out_text.setEasingCurve(QEasingCurve.InOutQuad)

        def on_fade_finished():
            self.overlay_label.deleteLater()
            self.overlay_label = None

        self.fade_out_text.finished.connect(on_fade_finished)

        # Start fade-out after 2 seconds
        QTimer.singleShot(2000, self.fade_out_text.start)


# For widgets
if __name__ == '__main__':
    auth_data = load_auth_data()
    app = QApplication(sys.argv)
    widgets = authenticator(auth_data)
    configuration.load_stylesheet(app)
    widgets.show()
    sys.exit(app.exec_())