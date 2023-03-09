# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 414)
        self.actionAgregar = QAction(MainWindow)
        self.actionAgregar.setObjectName(u"actionAgregar")
        self.actionListar = QAction(MainWindow)
        self.actionListar.setObjectName(u"actionListar")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionConfiguracion = QAction(MainWindow)
        self.actionConfiguracion.setObjectName(u"actionConfiguracion")
        self.actionEliminar = QAction(MainWindow)
        self.actionEliminar.setObjectName(u"actionEliminar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 0, 241, 61))
        font = QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(670, 350, 81, 21))
        font1 = QFont()
        font1.setPointSize(8)
        self.label_4.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 70, 711, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lblarchivos = QLabel(self.layoutWidget)
        self.lblarchivos.setObjectName(u"lblarchivos")

        self.horizontalLayout_2.addWidget(self.lblarchivos)

        self.btnArcvhivos = QPushButton(self.layoutWidget)
        self.btnArcvhivos.setObjectName(u"btnArcvhivos")

        self.horizontalLayout_2.addWidget(self.btnArcvhivos)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 140, 108, 19))
        self.btnEnviar = QPushButton(self.centralwidget)
        self.btnEnviar.setObjectName(u"btnEnviar")
        self.btnEnviar.setGeometry(QRect(510, 280, 241, 41))
        font2 = QFont()
        font2.setPointSize(24)
        self.btnEnviar.setFont(font2)
        self.txtcorreo = QPlainTextEdit(self.centralwidget)
        self.txtcorreo.setObjectName(u"txtcorreo")
        self.txtcorreo.setGeometry(QRect(230, 130, 531, 121))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 24))
        self.menuContactos = QMenu(self.menubar)
        self.menuContactos.setObjectName(u"menuContactos")
        self.menuSalir = QMenu(self.menubar)
        self.menuSalir.setObjectName(u"menuSalir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuContactos.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())
        self.menuContactos.addAction(self.actionAgregar)
        self.menuContactos.addAction(self.actionListar)
        self.menuContactos.addAction(self.actionEliminar)
        self.menuSalir.addAction(self.actionSalir)
        self.menuSalir.addAction(self.actionConfiguracion)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Envio de incidencias", None))
        self.actionAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.actionListar.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionConfiguracion.setText(QCoreApplication.translate("MainWindow", u"Configuracion", None))
        self.actionEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enviar incidencias", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Created by lleon", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Path de los archivos", None))
        self.lblarchivos.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnArcvhivos.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Texto del correo", None))
        self.btnEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.menuContactos.setTitle(QCoreApplication.translate("MainWindow", u"Contactos", None))
        self.menuSalir.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
    # retranslateUi

