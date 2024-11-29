import pwinput
from models.usuario import UsuarioModelo
from views.usuarios import menu
from views.indicadores import mostrarMenuIndicador

class MenuLogin:
    def iniciar_sesion(self):
            print("Iniciando sesión:")
            username = input("Ingrese su nombre de usuario: ").strip()
            contrasena = pwinput.pwinput("Ingrese la contraseña: ").strip()
            usuario = UsuarioModelo.autenticar(username, contrasena)

            if usuario:
                print(f"¡Bienvenido, {usuario.username}")
                print("1 Vista de usuarios")
                print("2 Vista de indicadores")
                print("3 Salir")
                opcion = input("Ingrese el número de la opción deseada: ")
                if opcion == "1":
                    menu()
                elif opcion == "2":
                    mostrarMenuIndicador()
                elif opcion == "3":
                    print("Hasta pronto!")
                    
                # if usuario.idRol == 1: 
                #     self.menu_principal_administrativo.mostrarMenu()
                # elif usuario.idRol == 2: 
                #     self.menu_principal_empleado.mostrarMenu()
            else:
                print("Usuario o contraseña incorrectos.")
