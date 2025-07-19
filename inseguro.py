import subprocess
import requests
import os
import shlex
from getpass import getpass


def obtener_password():
    return getpass("Ingrese la contraseña de la base de datos: ")


def ejecutar_comando_usuario():
    comando = input("Comando permitido (solo 'ls' o 'dir'): ")
    if comando in ['ls', 'dir']:
        subprocess.call([comando])
    else:
        print("Comando no permitido.")


def obtener_datos_externos():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        print("Respuesta:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error al obtener datos:", e)


def leer_archivo_usuario():
    ruta = input("Ruta del archivo a leer: ")
    if os.path.exists(ruta) and os.path.isfile(ruta):
        with open(ruta, 'r') as f:
            contenido = f.read()
            print("Contenido:", contenido)
    else:
        print("Archivo no encontrado.")


def crear_archivo_privado():
    with open("secreto.txt", 'w') as f:
        f.write("información sensible")
    os.chmod("secreto.txt", 0o600)  


password = obtener_password()
ejecutar_comando_usuario()
obtener_datos_externos()
leer_archivo_usuario()
crear_archivo_privado()
