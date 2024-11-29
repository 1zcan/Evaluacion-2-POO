from models.usuario import Usuario
from controllers.usuario_controller import agregar, editar, eliminar, mostrar_uno, mostrar_todos

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
    op = leer_numero("Ingrese una opción: ")
    
    if op == 1:
        add_user()
    elif op == 2:
        edit_user()
    elif op == 3:
        delete_user()
    elif op == 4:
        show_user()
    elif op == 5:
        show_all_users()
    elif op == 0:
        print("SALIR")
    else:
        print("Opción no válida. Intente nuevamente.")


def add_user():
    nombre = input("Ingrese nombre: ")
    passwd = input("Ingrese contraseña: ")
    nuevo_usuario = Usuario(nombre, passwd)
    agregar(nuevo_usuario)

def edit_user():
    id_usuario = leer_numero("Ingrese el ID del usuario a editar: ")
    nombre = input("Ingrese el nuevo nombre: ")
    passwd = input("Ingrese la nueva contraseña: ")
    usuario = Usuario(nombre, passwd)
    editar(id_usuario, usuario)

def delete_user():
    id_usuario = leer_numero("Ingrese el ID del usuario a eliminar: ")
    eliminar(id_usuario)

def show_user():
    id_usuario = leer_numero("Ingrese el ID del usuario a mostrar: ")
    usuario = mostrar_uno(id_usuario)
    if usuario:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Contraseña: {usuario.passwd}")
    else:
        print("Usuario no encontrado.")

def show_all_users():
    usuarios = mostrar_todos()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Contraseña: {usuario.passwd}")


