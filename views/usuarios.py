from models.usuario import Usuario
from controllers.usuario_controller import agregar_usuario

def leer_numero(mensaje):
    while True:
        try:
            op=int(input(mensaje))
            return op
        except ValueError:
            print("Debe ingresar un número.")

def menu():
    print("App Usuarios")
    print("1.- Agregar")
    print("2.- Editar")
    print("3.- Eliminar")
    print("4.- Mostrar uno")
    print("5.- Mostrar todos")
    print("0.- Salir")
    op=leer_numero("Ingrese una opción: ")
    return op

def add_user():
    nombre=input("Ingrese nombre: ")
    edad=leer_numero("Ingrese edad: ")
    passwd=input("Ingrese contraseña: ")
    usuario=Usuario(nombre,edad,passwd)
    agregar_usuario(usuario)

def main():
    while True:
        op=menu()
        if op==1:#agregar
            add_user()
        elif op==0:
            print("Gracias por preferirnos")
