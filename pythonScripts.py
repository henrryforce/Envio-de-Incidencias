import os
import PyPDF2
import json
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def enviarCorreos(nombre, correo, file, archivo):
    de = "contacto@despachoavila.com"
    passord = "Password@"
    cuerpo = "Hola te envio el archivo de incidencias" #cambiar a input en la interfaz grafica
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = de
    mensaje['To'] = correo
    mensaje['Subject'] = "Incidencias"
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
    sesion_smtp = smtplib.SMTP('smtp.hostinger.com', 587)    
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

path = "/home/luis/Documentos/Repos/scriptsPython/incidencias"
archivos = os.listdir(path)
for archivo in archivos:
    with open(path+"/"+archivo, 'rb') as file:
        lector_pdf = PyPDF2.PdfReader(file)
        numero_paginas = len(lector_pdf.pages)
        pagina = lector_pdf.pages[0]
        texto_pagina = pagina.extract_text()
    print(texto_pagina)
    with open('contactos.json') as jsonFile:
        contactos = json.load(jsonFile)
    # buaqueda del rfc del JSON en el texto del PDF
    for contacto in contactos:
        res_search = re.search(contacto["rfc"] ,texto_pagina)
        if(res_search is not None):
            enviarCorreos(contacto["nombre"], contacto["correo"],file,archivo)

    
