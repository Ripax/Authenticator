#! /usr/bin/python3.12
# Author : Anupam Biswas
# Date : 23 september 2024

__Author__ = 'Anupam Biswas'
__version__ = '1.0.7'

import sys
import os
import pyotp
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, \
    QMessageBox, QProgressBar, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt, QSize
from PyQt5 import QtCore, QtGui

from datetime import datetime
from ui.authenticator import Ui_authenticator

from icon import resource

import time

from pyotp import TOTP

date = datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
username = os.getlogin()


class authenticator(Ui_authenticator, QWidget):
    def __init__(self):
        super(authenticator, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"[2fA] Authenticator app {username}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.label.setPixmap(QtGui.QPixmap(":/icon/2fa.png"))

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.progressBar.setMaximum(60)

        self.pushButton.clicked.connect(self.copy_totp)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_totp)
        self.timer.start(1000)
        self.generate_totp()

    def generate_totp(self):
        # Get the secret from the QRCode, which is shared by your Organization.
        secret = "Your 26 Digit code."
        if not secret:
            QMessageBox.warning(self, "Error", "No secret provided.")
            return

        # Create a TOTP object
        self.totp = pyotp.TOTP(secret)
        self.update_totp()

    def update_totp(self):
        if hasattr(self, 'totp'):
            # Get the current time in seconds since epoch
            current_time = int(time.time())
            # Calculate how much time is left in the current 60-second window
            time_remaining = 60 - (current_time % 60)

            # Update the progress bar
            self.progressBar.setValue(time_remaining)

            # Only regenerate TOTP at the start of a new time window
            if time_remaining == 60:
                # Get the current TOTP token
                totp_token = self.totp.now()
                self.lcdNumber.display(f"{totp_token}")
            else:
                # Update the countdown, but keep the current token
                current_token = self.totp.now()
                self.lcdNumber.display(f"{current_token}")


    def copy_totp(self):
        totp = round(self.lcdNumber.value())
        clipboard = QApplication.clipboard()
        clipboard.setText(str(totp))
        # QMessageBox.information(self, "Information", "Copied.")
        self.msg_box = QMessageBox(QMessageBox.Information, "Information", "Copied.")
        self.msg_box.show()
        QTimer.singleShot(2000, self.msg_box.close)  # Close after 2 seconds


# For widgets
if __name__ == '__main__':
    app = QApplication([])
    widgets = authenticator()
    widgets.show()
    sys.exit(app.exec_())