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

        if opcion == "1":  # Si la opción es 1, se piden los datos del empleado y se llama a la función crear_empleado
            nombre = input("Nombre del empleado: ")
            direccion = input("Dirección del empleado: ")
            telefono = input("Teléfono del empleado: ")
            email = input("Email del empleado: ")
            fecha_contrato = input("Fecha de contrato del empleado (YYYY-MM-DD): ")
            salario = float(input("Salario del empleado: "))
            crear_empleado(
                nombre, direccion, telefono, email, fecha_contrato, salario
            )  # Llamamos a la función crear_empleado

        elif opcion == "2":  # Si la opcion es 2, se pide el nombre y el gerente del departamento y se llama a la funcion crear_departamento
            nombre = input("Nombre del departamento: ")

            gerente = input("gerente del departamento: ")
            crear_departamento(nombre, gerente)

        elif opcion == "3":
            Empleados = obtener_empleados()  # llamamos a la funcion obtener_Empleados que se encuentra en el archivo empleados_controller.py
            if Empleados:
                for empleados in Empleados:
                    print(
                        f"nombre: {empleados[1]}, direccion:{empleados[2]}, telefono: {empleados[3]}, email: {empleados[4]}, trabaja desde: {empleados[5]}, salario: {empleados[6]}"
                    )
            else:
                print("No hay Empleados registrados.")

        elif opcion == "4":
            departamentos = obtener_departamentos()  # llamamos a la funcion obtener_departamentos que se encuentra en el archivo departamento_controller.py
            if departamentos:  # Si hay departamentos registrados, se recorre la lista de departamentos y se imprime el nombre, la edad y la gerente de cada uno
                for (
                    departamento
                ) in departamentos:  # Recorremos la lista de departamentos,
                    print(f"departamento:{departamento[0]},gerente:{departamento[1]}")
            else:
                print("No hay departamentos registrados.")

        elif opcion == "5":
          # Si la opcion es 5, se pide el nombre del empleados a actualizar y se llama a la funcion buscar_empleado_por_nombre
            nombre = input("Nombre del empleado a actualizar: ")
            empleado = buscar_empleado_por_nombre(nombre)
            if empleado:  # Si el empleado existe..
                nuevo_nombre = input("Nuevo nombre del empleado: ")
                direccion = input("Nueva dirección del empleado: ")
                telefono = input("Nuevo teléfono del empleado: ")
                email = input("Nuevo Email del empleado: ")
                fecha_contrato = input("Nueva fecha de contrato del empleado (YYYY-MM-DD): ")
                salario = float(input("Nuevo salario del empleado: "))
                actualizar_empleado(nuevo_nombre, direccion, telefono, email, fecha_contrato, salario)
                print("Empleado actualizado exitosamente.")
            else:
                print("Empleado no encontrado.")


        elif opcion == "6":
            nombre = input("Nombre del departamento a actualizar: ")
            departamento = buscar_departamento_por_nombre(nombre)
            if departamento:
                nuevo_nombre = input("Nuevo nombre del departamento: ")
                gerente = input("Nuevo id del gerente del departamento: ")
                actualizar_departamento(nombre, nuevo_nombre, gerente)
                print("departamento actualizado exitosamente.")
            else:
                print("departamento no encontrado.")

        elif opcion == "7":
            nombre = input("ID del empleados a eliminar: ")
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
