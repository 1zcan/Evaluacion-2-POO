from controllers.empleados_controller import (
    crear_empleados,
    obtener_empleados,
    actualizar_empleados,
    eliminar_empleados,
    buscar_empleados_por_nombre,
)  # importar funciones del controlador de Empleados

from controllers.departamentos_controller import (
    crear_departamento,
    obtener_departamentos,
    actualizar_departamento,
    eliminar_departamento,
    buscar_departamento_por_nombre,
)  # Importar funciones del controlador de departamento

from models.db import (
    crear_tablas,
)  # Importar función para crear las tablas en la base de datos


def mostrar_menu():  # Función para mostrar el menú
    crear_tablas()  # Crear las tablas si no existen

    while (
        True
    ):  # Ciclo infinito para mostrar el menú, hasta que el usuario decida salir
        print("\n--- Menú ---")
        print("1. Crear empleados")
        print("2. Crear departamento")
        print("3. Mostrar empleados")
        print("4. Mostrar departamentos")
        print("5. Actualizar empleados")
        print("6. Actualizar departamento")
        print("7. Eliminar empleados")
        print("8. Eliminar departamento")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if (
            opcion == "1"
        ):  # Si la opcion es 1, se pide el nombre, la edad y la carrera del empleados y se llama a la funcion crear_empleados
            nombre = input("Nombre del empleados: ")
            edad = int(input("Edad del empleados: "))
            carrera = input("Carrera del empleados: ")
            crear_empleados(
                nombre, edad, carrera
            )  # llamamos a la funcion crear_empleados que se encuentra en el archivo empleados_controller.py

        elif (
            opcion == "2"
        ):  # Si la opcion es 2, se pide el nombre, la edad y la materia del departamento y se llama a la funcion crear_departamento
            nombre = input("Nombre del departamento: ")
            edad = int(input("Edad del departamento: "))
            materia = input("Materia del departamento: ")
            crear_departamento(nombre, edad, materia)  #
        elif (
            opcion == "3"
        ):  # Si la opcion es 3, se llama a la funcion obtener_Empleados que se encuentra en el archivo empleados_controller.py
            Empleados = obtener_empleados()  # llamamos a la funcion obtener_Empleados que se encuentra en el archivo empleados_controller.py
            if Empleados:  # Si hay Empleados registrados, se recorre la lista de Empleados y se imprime el nombre, la edad y la carrera de cada uno
                for empleados in Empleados:  # Recorremos la lista de Empleados,
                    print(
                        f"{empleados[0]} - {empleados[1]}, {empleados[2]} años, Carrera: {empleados[3]}"
                    )  # imprimimos el nombre, la edad y la carrera de cada empleados
            else:
                print(
                    "No hay Empleados registrados."
                )  # Si no hay Empleados registrados, se imprime un mensaje
        elif opcion == "4":
            departamentos = obtener_departamentos()  # llamamos a la funcion obtener_departamentos que se encuentra en el archivo departamento_controller.py
            if departamentos:  # Si hay departamentos registrados, se recorre la lista de departamentos y se imprime el nombre, la edad y la materia de cada uno
                for (
                    departamento
                ) in departamentos:  # Recorremos la lista de departamentos,
                    print(
                        f"{departamento[0]} - {departamento[1]}, {departamento[2]} años, Materia: {departamento[3]}"
                    )
            else:
                print("No hay departamentos registrados.")
        elif (
            opcion == "5"
        ):  # Si la opcion es 5, se pide el nombre del empleados a actualizar y se llama a la funcion buscar_empleados_por_nombre
            nombre = input("Nombre del empleados a actualizar: ")
            empleados = buscar_empleados_por_nombre(nombre)
            if empleados:  # Si el empleados existe, se pide el nuevo nombre, la nueva edad y la nueva carrera del empleados y se llama a la funcion actualizar_empleados
                nuevo_nombre = input("Nuevo nombre del empleados: ")
                edad = int(input("Nueva edad del empleados: "))
                carrera = input("Nueva carrera del empleados: ")
                actualizar_empleados(nombre, nuevo_nombre, edad, carrera)
                print("empleados actualizado exitosamente.")
            else:
                print("empleados no encontrado.")
        elif opcion == "6":
            nombre = input("Nombre del departamento a actualizar: ")
            departamento = buscar_departamento_por_nombre(nombre)
            if departamento:
                nuevo_nombre = input("Nuevo nombre del departamento: ")
                edad = int(input("Nueva edad del departamento: "))
                materia = input("Nueva materia del departamento: ")
                actualizar_departamento(nombre, nuevo_nombre, edad, materia)
                print("departamento actualizado exitosamente.")
            else:
                print("departamento no encontrado.")
        elif opcion == "7":
            nombre = input("Nombre del empleados a eliminar: ")
            eliminar_empleados(nombre)
            print("empleados eliminado exitosamente.")
        elif opcion == "8":
            nombre = input("Nombre del departamento a eliminar: ")
            eliminar_departamento(nombre)
            print("departamento eliminado exitosamente.")
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
