from controllers.estudiante_controller import (
    crear_estudiante,
    obtener_estudiantes,
    actualizar_estudiante,
    eliminar_estudiante,
    buscar_estudiante_por_nombre,
)  # importar funciones del controlador de estudiantes
from controllers.profesor_controller import (
    crear_profesor,
    obtener_profesores,
    actualizar_profesor,
    eliminar_profesor,
    buscar_profesor_por_nombre,
)  # Importar funciones del controlador de profesores
from models.db import (
    crear_tablas,
)  # Importar función para crear las tablas en la base de datos


def mostrar_menu():  # Función para mostrar el menú
    crear_tablas()  # Crear las tablas si no existen

    while (
        True
    ):  # Ciclo infinito para mostrar el menú, hasta que el usuario decida salir
        print("\n--- Menú ---")
        print("1. Crear Estudiante")
        print("2. Crear Profesor")
        print("3. Mostrar Estudiantes")
        print("4. Mostrar Profesores")
        print("5. Actualizar Estudiante")
        print("6. Actualizar Profesor")
        print("7. Eliminar Estudiante")
        print("8. Eliminar Profesor")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if (
            opcion == "1"
        ):  # Si la opcion es 1, se pide el nombre, la edad y la carrera del estudiante y se llama a la funcion crear_estudiante
            nombre = input("Nombre del estudiante: ")
            edad = int(input("Edad del estudiante: "))
            carrera = input("Carrera del estudiante: ")
            crear_estudiante(
                nombre, edad, carrera
            )  # llamamos a la funcion crear_estudiante que se encuentra en el archivo estudiante_controller.py

        elif (
            opcion == "2"
        ):  # Si la opcion es 2, se pide el nombre, la edad y la materia del profesor y se llama a la funcion crear_profesor
            nombre = input("Nombre del profesor: ")
            edad = int(input("Edad del profesor: "))
            materia = input("Materia del profesor: ")
            crear_profesor(nombre, edad, materia)  #
        elif (
            opcion == "3"
        ):  # Si la opcion es 3, se llama a la funcion obtener_estudiantes que se encuentra en el archivo estudiante_controller.py
            estudiantes = obtener_estudiantes()  # llamamos a la funcion obtener_estudiantes que se encuentra en el archivo estudiante_controller.py
            if estudiantes:  # Si hay estudiantes registrados, se recorre la lista de estudiantes y se imprime el nombre, la edad y la carrera de cada uno
                for estudiante in estudiantes:  # Recorremos la lista de estudiantes,
                    print(
                        f"{estudiante[0]} - {estudiante[1]}, {estudiante[2]} años, Carrera: {estudiante[3]}"
                    )  # imprimimos el nombre, la edad y la carrera de cada estudiante
            else:
                print(
                    "No hay estudiantes registrados."
                )  # Si no hay estudiantes registrados, se imprime un mensaje
        elif opcion == "4":
            profesores = obtener_profesores()  # llamamos a la funcion obtener_profesores que se encuentra en el archivo profesor_controller.py
            if profesores:  # Si hay profesores registrados, se recorre la lista de profesores y se imprime el nombre, la edad y la materia de cada uno
                for profesor in profesores:  # Recorremos la lista de profesores,
                    print(
                        f"{profesor[0]} - {profesor[1]}, {profesor[2]} años, Materia: {profesor[3]}"
                    )
            else:
                print("No hay profesores registrados.")
        elif (
            opcion == "5"
        ):  # Si la opcion es 5, se pide el nombre del estudiante a actualizar y se llama a la funcion buscar_estudiante_por_nombre
            nombre = input("Nombre del estudiante a actualizar: ")
            estudiante = buscar_estudiante_por_nombre(nombre)
            if estudiante:  # Si el estudiante existe, se pide el nuevo nombre, la nueva edad y la nueva carrera del estudiante y se llama a la funcion actualizar_estudiante
                nuevo_nombre = input("Nuevo nombre del estudiante: ")
                edad = int(input("Nueva edad del estudiante: "))
                carrera = input("Nueva carrera del estudiante: ")
                actualizar_estudiante(nombre, nuevo_nombre, edad, carrera)
                print("Estudiante actualizado exitosamente.")
            else:
                print("Estudiante no encontrado.")
        elif opcion == "6":
            nombre = input("Nombre del profesor a actualizar: ")
            profesor = buscar_profesor_por_nombre(nombre)
            if profesor:
                nuevo_nombre = input("Nuevo nombre del profesor: ")
                edad = int(input("Nueva edad del profesor: "))
                materia = input("Nueva materia del profesor: ")
                actualizar_profesor(nombre, nuevo_nombre, edad, materia)
                print("Profesor actualizado exitosamente.")
            else:
                print("Profesor no encontrado.")
        elif opcion == "7":
            nombre = input("Nombre del estudiante a eliminar: ")
            eliminar_estudiante(nombre)
            print("Estudiante eliminado exitosamente.")
        elif opcion == "8":
            nombre = input("Nombre del profesor a eliminar: ")
            eliminar_profesor(nombre)
            print("Profesor eliminado exitosamente.")
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
