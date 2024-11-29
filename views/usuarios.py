from models.usuario import Usuario
from controllers.usuario_controller import agregar

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
    passwd=input("Ingrese contraseña: ")
    usuario=Usuario(nombre,passwd)
    agregar(usuario)

def main():
    while True:
        op=menu()
        if op==1:
            add_user()
        elif op==0:
            print("SALIR")
