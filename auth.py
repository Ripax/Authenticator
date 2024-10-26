#! /usr/bin/python3.12
# Author : Anupam Biswas
# Date : 23 september 2024
# app name : 2 ass fuck Authenticator.
from PyQt5.QtGui import QIcon


def info():
    __Author__ = 'Anupam Biswas'
    __version__ = '1.0.7'
    __date__ = '23 september 2024'
    __app_name__ = '2 ass fuck Authenticator.'

import json
import os
import sys
import time
from datetime import datetime

import pyotp
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsDropShadowEffect, QMessageBox
from soupsieve.util import lower

from ui.authenticator import Ui_authenticator
from icon import resource

date = datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
username = os.getlogin()


def load_auth_data(filepath=".auth"):
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


class authenticator(Ui_authenticator, QWidget):
    def __init__(self, authdata):
        super(authenticator, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"[2fA] Authenticator app {username}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.icon.setPixmap(QtGui.QPixmap(":/icon/2fa.png"))

        # set data to Combobox from .auth data.
        locations = authdata.get(username, {})
        cur_path = os.getcwd()
        for location in locations.keys():
            icon_path = f"{cur_path}/icon/{location}_icon.png"
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

    @staticmethod
    def seceret_code(site):
        with open('.auth', 'r') as data:
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
        # QMessageBox.information(self, "Information", "Copied.")
        self.msg_box = QMessageBox(QMessageBox.Information, "Information", "Copied.")
        self.msg_box.show()
        QTimer.singleShot(2000, self.msg_box.close)  # Close after 2 seconds


# For widgets
if __name__ == '__main__':
    auth_data = load_auth_data()
    app = QApplication(sys.argv)
    widgets = authenticator(auth_data)
    widgets.show()
    sys.exit(app.exec_())