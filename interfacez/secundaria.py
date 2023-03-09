# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secundaria.ui'
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
        Form.resize(446, 240)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 171, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.btnaddcontacto = QPushButton(Form)
        self.btnaddcontacto.setObjectName(u"btnaddcontacto")
        self.btnaddcontacto.setGeometry(QRect(320, 200, 87, 27))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 50, 281, 121))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.rfctxt = QLineEdit(self.layoutWidget)
        self.rfctxt.setObjectName(u"rfctxt")

        self.gridLayout.addWidget(self.rfctxt, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.mailtxt = QLineEdit(self.layoutWidget)
        self.mailtxt.setObjectName(u"mailtxt")

        self.gridLayout.addWidget(self.mailtxt, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.nombretxt = QLineEdit(self.layoutWidget)
        self.nombretxt.setObjectName(u"nombretxt")

        self.gridLayout.addWidget(self.nombretxt, 2, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Agregar Contactos", None))
#if QT_CONFIG(statustip)
        Form.setStatusTip(QCoreApplication.translate("Form", u"RFC del contacto", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("Form", u"Agregar Contacto", None))
        self.btnaddcontacto.setText(QCoreApplication.translate("Form", u"Agregar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"RFC", None))
#if QT_CONFIG(statustip)
        self.rfctxt.setStatusTip(QCoreApplication.translate("Form", u"RFC del Contacto", None))
#endif // QT_CONFIG(statustip)
        self.rfctxt.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Correo", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nombre", None))
    # retranslateUi

