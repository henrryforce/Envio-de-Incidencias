from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidgetItem,QMessageBox,QFileDialog
from PySide6.QtCore import Qt
from interfacez.mainwindow import Ui_MainWindow
from interfacez.secundaria import Ui_Form
from interfacez.tabla import Ui_Form as tabla
from interfacez.ajustes import Ui_Form as ajustes
from interfacez.eliminar import Ui_Eliminar
from helpers import absPath
import PyPDF2
import json
import sys
import re
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
class ventanaEliminar(QWidget,Ui_Eliminar):
     found = False
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBuscar.clicked.connect(self.serchContact)
        self.btnEliminar.clicked.connect(self.eliminarContacto)
     def eliminarContacto(self):
        if(self.found):
            for i, dato in enumerate(self.datos):
                if dato['rfc'] == self.txtSerch.text():
                    del self.datos[i]
                    break
            with open(absPath("contactos.json"), "w") as fichero:
                json.dump(self.datos, fichero)
            self.txtEliminarCorreo.setText("")
            self.txtSerch.setText("")
            self.txtEliminarName.setText("")
            QMessageBox.information(self, "Confirmación", f"Eliminado con exito")
        else:
            QMessageBox.warning(self, "Error", f"Debes ingresar un RFC")
     def serchContact(self):               
        if(self.txtSerch.text() == ""):
            QMessageBox.warning(self, "Error", f"Debes ingresar un RFC")
        else:
            with open(absPath("contactos.json")) as fichero:
                self.datos = json.load(fichero)
            for contacto in self.datos:
                if (self.txtSerch.text() == contacto["rfc"]):
                    self.txtEliminarName.setText(contacto["nombre"])
                    self.txtEliminarCorreo.setText(contacto["correo"])
                    self.found = True
            if(self.txtEliminarCorreo.text() =="" and self.txtEliminarName.text() == ""):
                QMessageBox.warning(self, "Error", f"RFC no encontrado")
            

class ventanaAjustes(QWidget,ajustes):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnSaveSettings.clicked.connect(self.saveSettings)
        self.setSetiings()

     def setSetiings(self):
        with open(absPath("ajustes.json")) as ajustes:
            self.ajustes = json.load(ajustes)
        self.txtSettingsCorreo.setText(self.ajustes["correo"])
        self.txtsettingsPass.setText(self.ajustes["pass"])
        self.txtpuerto.setText(self.ajustes["puerto"])
        self.txtsmtp.setText(self.ajustes["smtp"])
     def saveSettings(self):
        self.datos = {
             "correo":self.txtSettingsCorreo.text(),
            "pass":self.txtsettingsPass.text(),
            "smtp":self.txtsmtp.text(),
            "puerto":self.txtpuerto.text()
        }
        with open(absPath("ajustes.json"), "w") as fichero:
            json.dump(self.datos, fichero)
        QMessageBox.information(self, "Confirmación", f"Agregado con exito")
        

class ventanaTabla(QWidget,tabla):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configTabla()
     def configTabla(self):
        # cargamos el contenido del fichero
        with open(absPath("contactos.json")) as fichero:
            self.datos = json.load(fichero)
        # definimos la configuración de las columnas (claves del json)
        self.columnas = ["nombre", "rfc", "correo"]
        # configuramos la tabla a partir de la información recuperada
        self.tabla.setRowCount(len(self.datos))
        # establecemos la longitud de las columnas
        self.tabla.setColumnCount(len(self.columnas))
        # establecemos las cabeceras de las columnas
        self.tabla.setHorizontalHeaderLabels(self.columnas)
        # dibujamos la tabla y los botones
        for i, fila in enumerate(self.datos):
            for j, columna in enumerate(self.columnas):
                item = QTableWidgetItem()
                # Con Qt.EditRole se establece el tipo de campo automáticamente
                item.setData(Qt.EditRole, fila[columna])
                self.tabla.setItem(i, j, item)
        # personalizamos y redimensionamos la tabla
        self.tabla.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
        self.tabla.setHorizontalHeaderItem(1, QTableWidgetItem("RFC"))
        self.tabla.setHorizontalHeaderItem(2, QTableWidgetItem("Email"))
        self.tabla.resizeColumnsToContents()
        # configuramos las señales
        self.tabla.itemChanged.connect(self.celda_modificada)
     def celda_modificada(self, celda):
        # recuperamos la fila y la clave de la columna del item seleccionado
        fila, columna = celda.row(), self.columnas[celda.column()]
        # modificamos el mismo lugar del dataframe recuperando el dato con tipo
        self.datos[fila][columna] = celda.data(Qt.EditRole)
        # guardamos el fichero
        self.guardar_json()
     def guardar_json(self):
        with open(absPath("contactos.json"), "w") as fichero:
            json.dump(self.datos, fichero)
class subVentana(QWidget,Ui_Form):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnaddcontacto.clicked.connect(self.addJson)
     def addJson(self):
        nombre = self.nombretxt.text()
        rfc = self.rfctxt.text()
        correo = self.mailtxt.text()
        if(nombre == "" or rfc == "" or correo==""):
            self.mostrar_mensaje()
        else:
            with open(absPath("contactos.json")) as fichero:
                self.datos = json.load(fichero)
                self.datos.append({"nombre":nombre,"rfc":rfc,"correo":correo})
            # Guardamos los registros del fichero
            with open(absPath("contactos.json"), "w") as fichero:
                json.dump(self.datos, fichero)
            QMessageBox.information(self, "Confirmación", f"Agregado con exito")
            self.nombretxt.setText("")
            self.rfctxt.setText("")
            self.mailtxt.setText("")
     def mostrar_mensaje(self):
        QMessageBox.warning(self, "Error", f"No puedes agregar campos en blanco")
        
class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz
    pathArchivos =""
    def __init__(self):
        
        # Llamamos al constructor explícito de QMainWindow
        super().__init__()
        self.setupUi(self)
        #eventos del menu
        self.actionAgregar.triggered.connect(self.mostrarSubVentana)
        self.actionSalir.triggered.connect(self.close)
        self.actionListar.triggered.connect(self.mostrarTabla)
        self.actionEliminar.triggered.connect(self.mostarEliminar)
        self.btnArcvhivos.clicked.connect(self.setPathArchivos)
        self.btnEnviar.clicked.connect(self.enviarIncidencias)
        self.actionConfiguracion.triggered.connect(self.mostrarConfig)
        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.agregarContactos = subVentana()
        self.tablaContactos= ventanaTabla()
        self.settings = ventanaAjustes()
        self.eliminar = ventanaEliminar()
    def enviarIncidencias(self):
        if(self.pathArchivos == ""):
            QMessageBox.warning(self, "Error", f"Debes agregar el directorio de los archivos de incidencias")
        if(self.txtcorreo.toPlainText() == ""):
            QMessageBox.warning(self, "Error", f"Debes ingresar el texto del correo")
        if(self.pathArchivos != "" and self.txtcorreo.toPlainText !=""):
            archivos = os.listdir(self.pathArchivos)
            with open('contactos.json') as jsonFile:
                    contactos = json.load(jsonFile)
            for archivo in archivos:
                with open(self.pathArchivos+"/"+archivo, 'rb') as file:
                    lector_pdf = PyPDF2.PdfReader(file)
                    pagina = lector_pdf.pages[0]
                    texto_pagina = pagina.extract_text()                
                # buaqueda del rfc del JSON en el texto del PDF
                for contacto in contactos:
                    res_search = re.search(contacto["rfc"] ,texto_pagina)
                    if(res_search is not None):
                        self.statusBar().showMessage('ultimo correo enviado a '+contacto["nombre"])
                        time.sleep(90)
                        self.enviarCorreos(contacto["nombre"], contacto["correo"],file,archivo,self.txtcorreo.toPlainText())
        QMessageBox.information(self, "Correos Enviados", f"Se han enviado los correos")
    def enviarCorreos(self,nombre, correo, file, archivo,body):
        with open(absPath("ajustes.json")) as ajustes:
            self.ajustes = json.load(ajustes)
        de = self.ajustes["correo"]
        passord = self.ajustes["pass"]
        cuerpo = body #cambiar a input en la interfaz grafica
        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        # Establecemos los atributos del mensaje
        mensaje['From'] = de
        mensaje['To'] = correo
        mensaje['Subject'] = "Incidencias" + nombre
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(file.name, 'rb')
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'pdf',Name=archivo)
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % archivo)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        # Creamos la conexión con el servidor
        sesion_smtp = smtplib.SMTP(self.ajustes["smtp"], int(self.ajustes["puerto"]))    
        # Ciframos la conexión
        sesion_smtp.starttls()
        # Iniciamos sesión en el servidor
        sesion_smtp.login(de,passord)
        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()
        # Enviamos el mensaje
        sesion_smtp.sendmail(de, correo, texto)
        # Cerramos la conexión
        sesion_smtp.quit()
    def mostrarSubVentana(self):
        self.agregarContactos.show()
    def mostrarTabla(self):
        self.tablaContactos.configTabla()
        self.tablaContactos.show()
    def setPathArchivos(self):
        self.pathArchivos = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lblarchivos.setText(self.pathArchivos)
    def mostrarConfig(self):
        self.settings.setSetiings()
        self.settings.show()
    def mostarEliminar(self):
        self.eliminar.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())