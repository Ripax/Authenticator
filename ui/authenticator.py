# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authenticator.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_authenticator(object):
    def setupUi(self, authenticator):
        authenticator.setObjectName("authenticator")
        authenticator.resize(174, 350)
        authenticator.setMinimumSize(QtCore.QSize(174, 350))
        authenticator.setMaximumSize(QtCore.QSize(174, 350))
        self.gridLayout = QtWidgets.QGridLayout(authenticator)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(authenticator)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.icon = QtWidgets.QLabel(self.frame)
        self.icon.setStyleSheet("QLabel {\n"
"    border: 1px solid rgb(43, 43, 43);\n"
"    border-radius: 4px;\n"
"}")
        self.icon.setText("")
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.verticalLayout_2.addWidget(self.icon)
        self.OTP_frame = QtWidgets.QFrame(self.frame)
        self.OTP_frame.setStyleSheet("QFrame{\n"
"    border: 1px solid rgb(43, 43, 43);\n"
"    border-radius: 4px;\n"
"}")
        self.OTP_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OTP_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OTP_frame.setObjectName("OTP_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.OTP_frame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.otp = QtWidgets.QLabel(self.OTP_frame)
        font = QtGui.QFont()
        font.setFamily("Baby Doll")
        font.setPointSize(40)
        self.otp.setFont(font)
        self.otp.setText("")
        self.otp.setAlignment(QtCore.Qt.AlignCenter)
        self.otp.setObjectName("otp")
        self.verticalLayout.addWidget(self.otp)
        self.verticalLayout_2.addWidget(self.OTP_frame)
        self.frame_sites = QtWidgets.QFrame(self.frame)
        self.frame_sites.setMaximumSize(QtCore.QSize(16777215, 36))
        self.frame_sites.setStyleSheet("QFrame{\n"
"    border: 1px solid rgb(43, 43, 43);\n"
"    border-radius: 4px;\n"
"}")
        self.frame_sites.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sites.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sites.setObjectName("frame_sites")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_sites)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mumbai = QtWidgets.QRadioButton(self.frame_sites)
        self.mumbai.setObjectName("mumbai")
        self.horizontalLayout_2.addWidget(self.mumbai)
        self.chennai = QtWidgets.QRadioButton(self.frame_sites)
        self.chennai.setObjectName("chennai")
        self.horizontalLayout_2.addWidget(self.chennai)
        self.verticalLayout_2.addWidget(self.frame_sites)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(82, 82))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 95))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(52, 82, 76);\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #39f0ed, stop: 1 #34faaf);\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #34faaf , stop: 1 #39f0ed,);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.footer = QtWidgets.QFrame(self.frame)
        self.footer.setMaximumSize(QtCore.QSize(16777215, 20))
        self.footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.footer.setObjectName("footer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_check = QtWidgets.QLabel(self.footer)
        self.time_check.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Baby Doll")
        font.setPointSize(10)
        self.time_check.setFont(font)
        self.time_check.setStyleSheet("QLabel, QToolTip {\n"
"    color: rgb(34, 34, 34);\n"
"}")
        self.time_check.setAlignment(QtCore.Qt.AlignCenter)
        self.time_check.setObjectName("time_check")
        self.horizontalLayout.addWidget(self.time_check, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.label_creadit = QtWidgets.QLabel(self.footer)
        font = QtGui.QFont()
        font.setFamily("Baby Doll")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_creadit.setFont(font)
        self.label_creadit.setStyleSheet("QLabel, QToolTip {\n"
"    color: rgb(45, 45, 45);\n"
"    border: 0px solid #222222;\n"
"    border-radius: 0px;\n"
"}")
        self.label_creadit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_creadit.setObjectName("label_creadit")
        self.horizontalLayout.addWidget(self.label_creadit, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.footer)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(authenticator)
        QtCore.QMetaObject.connectSlotsByName(authenticator)

    def retranslateUi(self, authenticator):
        _translate = QtCore.QCoreApplication.translate
        authenticator.setWindowTitle(_translate("authenticator", "2fa for dneg"))
        self.mumbai.setText(_translate("authenticator", "Mumbai"))
        self.chennai.setText(_translate("authenticator", "Chennai"))
        self.pushButton.setText(_translate("authenticator", "   Copy"))
        self.time_check.setText(_translate("authenticator", "60"))
        self.label_creadit.setToolTip(_translate("authenticator", "@Copyright 2024"))
        self.label_creadit.setText(_translate("authenticator", "@HTMLDigger"))