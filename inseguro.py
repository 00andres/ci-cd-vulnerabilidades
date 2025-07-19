import subprocess
import requests
import os
import shlex
from getpass import getpass


def obtener_password():
    return getpass("Ingrese la contraseña de la base de datos: ")


def ejecutar_comando_usuario():
    comando = input("Comando permitido (solo 'ls' o 'dir'): ").strip()
    comandos_permitidos = {
        'ls': ['ls', '-la'],
        'dir': ['dir']
    }
    if comando in comandos_permitidos:
        subprocess.run(comandos_permitidos[comando])
    else:
        print("Comando no permitido.")


def obtener_datos_externos():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        print("Respuesta:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error al obtener datos:", e)


def leer_archivo_usuario():
    ruta = input("Ruta del archivo a leer: ").strip()
    if os.path.exists(ruta) and os.path.isfile(ruta):
        try:
            with open(ruta, 'r') as f:
                contenido = f.read()
                print("Contenido del archivo:")
                print(contenido)
        except Exception as e:
            print("Error al leer el archivo:", e)
    else:
        print("El archivo no existe o no es válido.")


def crear_archivo_privado():
    try:
        with open("secreto.txt", 'w') as f:
            f.write("información sensible")
        os.chmod("secreto.txt", 0o600)  
        print("Archivo secreto.txt creado con permisos seguros.")
    except Exception as e:
        print("Error al crear archivo:", e)


if __name__ == "__main__":
    password = obtener_password()
    ejecutar_comando_usuario()
    obtener_datos_externos()
    leer_archivo_usuario()
    crear_archivo_privado()
