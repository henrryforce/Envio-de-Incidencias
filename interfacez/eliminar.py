# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        if not Eliminar.objectName():
            Eliminar.setObjectName(u"Eliminar")
        Eliminar.resize(436, 236)
        self.label = QLabel(Eliminar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 171, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.btnBuscar = QPushButton(Eliminar)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(310, 80, 87, 27))
        self.btnEliminar = QPushButton(Eliminar)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(310, 140, 87, 27))
        self.widget = QWidget(Eliminar)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 70, 251, 131))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.txtSerch = QLineEdit(self.widget)
        self.txtSerch.setObjectName(u"txtSerch")

        self.gridLayout.addWidget(self.txtSerch, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.txtEliminarName = QLineEdit(self.widget)
        self.txtEliminarName.setObjectName(u"txtEliminarName")
        self.txtEliminarName.setEnabled(False)

        self.gridLayout.addWidget(self.txtEliminarName, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.txtEliminarCorreo = QLineEdit(self.widget)
        self.txtEliminarCorreo.setObjectName(u"txtEliminarCorreo")
        self.txtEliminarCorreo.setEnabled(False)

        self.gridLayout.addWidget(self.txtEliminarCorreo, 2, 1, 1, 1)


        self.retranslateUi(Eliminar)

        QMetaObject.connectSlotsByName(Eliminar)
    # setupUi

    def retranslateUi(self, Eliminar):
        Eliminar.setWindowTitle(QCoreApplication.translate("Eliminar", u"Elimnar", None))
        self.label.setText(QCoreApplication.translate("Eliminar", u"Eliminar Contacto", None))
        self.btnBuscar.setText(QCoreApplication.translate("Eliminar", u"Buscar", None))
        self.btnEliminar.setText(QCoreApplication.translate("Eliminar", u"Eliminar", None))
        self.label_2.setText(QCoreApplication.translate("Eliminar", u"RFC", None))
        self.label_3.setText(QCoreApplication.translate("Eliminar", u"Nombre", None))
        self.label_4.setText(QCoreApplication.translate("Eliminar", u"Correo", None))
    # retranslateUi

