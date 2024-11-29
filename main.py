from views.login import MenuLogin
from views.usuarios import menu as MenuUsuario
from views.indicadores import mostrarMenuIndicador
from models.db import DB

def main():
    DB()
    menu_login = MenuLogin()
    inicio = menu_login.iniciar_sesion()
    if inicio:
        while True:
            print("Seleccione una opción:")
            print("1. Ir a vista de usuarios")
            print("2. Ir a vista de indicadores")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                MenuUsuario()
            elif opcion == "2":
                mostrarMenuIndicador()
            else:
                print("Opción no válida")

if __name__ == "__main__":
    main()