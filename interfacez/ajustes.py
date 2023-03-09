# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajustes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 10, 81, 31))
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.btnSaveSettings = QPushButton(Form)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")
        self.btnSaveSettings.setGeometry(QRect(290, 250, 87, 27))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 351, 161))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.txtSettingsCorreo = QLineEdit(self.widget)
        self.txtSettingsCorreo.setObjectName(u"txtSettingsCorreo")

        self.gridLayout.addWidget(self.txtSettingsCorreo, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.txtsettingsPass = QLineEdit(self.widget)
        self.txtsettingsPass.setObjectName(u"txtsettingsPass")

        self.gridLayout.addWidget(self.txtsettingsPass, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.txtsmtp = QLineEdit(self.widget)
        self.txtsmtp.setObjectName(u"txtsmtp")

        self.gridLayout.addWidget(self.txtsmtp, 2, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.txtpuerto = QLineEdit(self.widget)
        self.txtpuerto.setObjectName(u"txtpuerto")

        self.gridLayout.addWidget(self.txtpuerto, 3, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Ajustes", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ajustes", None))
        self.btnSaveSettings.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Servidor SMTP", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Puerto de conexion", None))
    # retranslateUi

