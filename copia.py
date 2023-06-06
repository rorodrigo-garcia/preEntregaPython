import json

from pathlib import Path


def obtenerRuta ():
    BASE_DIR = Path(__file__).resolve().parent
    return rf"{BASE_DIR}/usuarios.json"

def registrar_datos(usuarios) -> dict:
    nombre = input("Ingrese su Nombre: ").strip().capitalize()
    contraseña = input("Ingrese su contraseña: ").strip().capitalize()
    if nombre not in usuarios.keys():
        usuarios.update({ nombre : contraseña})
        guardar_datos(usuarios)
        print("Usuario registrado")
    else:
        print("Pruebe con otro usuario.")
    return usuarios

def login(usuarios) -> dict:
    nombre = input("Ingrese su Nombre: ").strip().capitalize()
    contraseña = input("Ingrese su contraseña: ").strip().capitalize()
    if nombre in usuarios.keys():
        if contraseña == usuarios[nombre]:
            usuarios.update({ nombre : contraseña})
            guardar_datos(usuarios)
            print("Usuario logueado")
        else:
            print("La contraseña no coincide.")
    else:
        print("Usuario no encontrado")

def guardar_datos(usuarios):
    with open(obtenerRuta(),"w") as archivo:
        json.dump(usuarios, archivo, indent=4)
        print("Registro guardado")

def datos():
    with open(obtenerRuta()) as archivo:
        data = json.load(archivo)
        return data

def main():
    usuarios = datos()
    registrar_datos(usuarios)
    print(datos())

main()
login(usuarios=[0])