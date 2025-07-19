import subprocess
import requests
import os

#  credenciales embebidas (hardcoded)
DB_PASSWORD = "admin123"  

#  ejecución de comandos basada en input del usuario
def ejecutar_comando_usuario():
    comando = input("Ingresa un comando del sistema: ")
    subprocess.call(comando, shell=True) 

# petición a HTTP inseguro
def obtener_datos_externos():
    response = requests.get("http://example.com/datos")  
    print("Respuesta:", response.text)

#  lectura de archivo sin validación
def leer_archivo_usuario():
    ruta = input("Ruta del archivo a leer: ")
    with open(ruta, 'r') as f:
        contenido = f.read()
        print("Contenido:", contenido)

# permisos excesivos
def crear_archivo_privado():
    with open("secreto.txt", 'w') as f:
        f.write("información sensible")
    os.chmod("secreto.txt", 0o777)  


ejecutar_comando_usuario()
obtener_datos_externos()
leer_archivo_usuario()
crear_archivo_privado()
