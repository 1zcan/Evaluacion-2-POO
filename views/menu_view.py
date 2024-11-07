from controllers.empleados_controller import (
    crear_empleado,
    obtener_empleados,
    actualizar_empleado,
    eliminar_empleado,
    buscar_empleado_por_nombre,
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
        ):  # Si la opción es 1, se piden los datos del empleado y se llama a la función crear_empleado
            nombre = input("Nombre del empleado: ")
            direccion = input("Dirección del empleado: ")
            telefono = input("Teléfono del empleado: ")
            email = input("Email del empleado: ")
            fecha_contrato = input("Fecha de contrato del empleado (YYYY-MM-DD): ")
            salario = float(input("Salario del empleado: "))
            crear_empleado(
                nombre, direccion, telefono, email, fecha_contrato, salario
            )  # Llamamos a la función crear_empleado

        elif (
            opcion == "2"
        ):  # Si la opcion es 2, se pide el nombre y el gerente del departamento y se llama a la funcion crear_departamento
            nombre = input("Nombre del departamento: ")

            gerente = input("gerente del departamento: ")
            crear_departamento(nombre, gerente)  #
        elif (
            opcion == "3"
        ):  # Si la opcion es 3, se llama a la funcion obtener_Empleados que se encuentra en el archivo empleados_controller.py
            Empleados = obtener_empleados()  # llamamos a la funcion obtener_Empleados que se encuentra en el archivo empleados_controller.py
            if Empleados:  # Si hay Empleados registrados, se recorre la lista de Empleados y se imprime el nombre, la edad y la departamento de cada uno
                for empleados in Empleados:  # Recorremos la lista de Empleados,
                    print(
                        f"{empleados[0]} - {empleados[1]}, {empleados[2]} años, departamento: {empleados[3]}"
                    )
            else:
                print("No hay Empleados registrados.")
        elif opcion == "4":
            departamentos = obtener_departamentos()  # llamamos a la funcion obtener_departamentos que se encuentra en el archivo departamento_controller.py
            if departamentos:  # Si hay departamentos registrados, se recorre la lista de departamentos y se imprime el nombre, la edad y la gerente de cada uno
                for (
                    departamento
                ) in departamentos:  # Recorremos la lista de departamentos,
                    print(
                        f"{departamento[0]} - {departamento[1]}, {departamento[2]} años, gerente: {departamento[3]}"
                    )
            else:
                print("No hay departamentos registrados.")
        elif (
            opcion == "5"
        ):  # Si la opcion es 5, se pide el nombre del empleados a actualizar y se llama a la funcion buscar_empleado_por_nombre
            nombre = input("Nombre del empleados a actualizar: ")
            empleados = buscar_empleado_por_nombre(nombre)
            if empleados:  # Si el empleados existe, se pide el nuevo nombre, la nueva edad y la nueva departamento del empleados y se llama a la funcion actualizar_empleado
                nuevo_nombre = input("Nuevo nombre del empleados: ")
                edad = int(input("Nueva edad del empleados: "))
                departamento = input("Nuevo departamento de empleados: ")
                actualizar_empleado(nombre, nuevo_nombre, edad, departamento)
                print("empleados actualizado exitosamente.")
            else:
                print("empleado no encontrado.")
        elif opcion == "6":
            nombre = input("Nombre del departamento a actualizar: ")
            departamento = buscar_departamento_por_nombre(nombre)
            if departamento:
                nuevo_nombre = input("Nuevo nombre del departamento: ")
                gerente = input("Nuevo gerente del departamento: ")
                actualizar_departamento(nombre, nuevo_nombre, gerente)
                print("departamento actualizado exitosamente.")
            else:
                print("departamento no encontrado.")
        elif opcion == "7":
            nombre = input("Nombre del empleados a eliminar: ")
            eliminar_empleado(nombre)
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
