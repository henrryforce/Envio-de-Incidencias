# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabla.ui'
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
        Form.resize(678, 307)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 20, 111, 41))
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 80, 661, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tabla = QTableWidget(self.formLayoutWidget)
        self.tabla.setObjectName(u"tabla")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.tabla)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tabla de contactos", None))
        self.label.setText(QCoreApplication.translate("Form", u"Contactos", None))
    # retranslateUi

