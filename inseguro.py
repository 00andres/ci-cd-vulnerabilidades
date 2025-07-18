import subprocess

def ejecutar_comando(comando):
    subprocess.call(comando, shell=True)

ejecutar_comando("ls -la")
