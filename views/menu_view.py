from controllers.empleados_controller import (
    crear_empleado,
    obtener_empleados,
    actualizar_empleado,
    eliminar_empleado,
    buscar_empleado_por_nombre,
)
from controllers.departamento_controller import (
    crear_departamento,
    obtener_departamentos,
    actualizar_departamento,
    eliminar_departamento,
    buscar_departamento_por_nombre,
)
from controllers.proyectos_controller import (
    crear_proyecto,
    obtener_proyectos,
    actualizar_proyecto,
    eliminar_proyecto,
    buscar_proyecto_por_nombre,
)
from controllers.asignacion_proyecto_controller import (
    asignar_proyecto,
    obtener_asignaciones,
    actualizar_asignacion,
    eliminar_asignacion,
)
from controllers.registro_tiempo_controller import (
    registrar_tiempo,
    obtener_registros_tiempo,
    actualizar_registro_tiempo,
    eliminar_registro_tiempo,
)
from models.db import crear_tablas

def mostrar_menu():
    crear_tablas()

    while True:
        print("\n--- Menú ---")
        print("1. Crear Empleado")
        print("2. Crear Departamento")
        print("3. Crear Proyecto")
        print("4. Asignar Proyecto")
        print("5. Registrar Tiempo")
        print("6. Mostrar Empleados")
        print("7. Mostrar Departamentos")
        print("8. Mostrar Proyectos")
        print("9. Mostrar Asignaciones")
        print("10. Mostrar Registros de Tiempo")
        print("11. Actualizar Empleado")
        print("12. Actualizar Departamento")
        print("13. Actualizar Proyecto")
        print("14. Actualizar Asignación")
        print("15. Actualizar Registro de Tiempo")
        print("16. Eliminar Empleado")
        print("17. Eliminar Departamento")
        print("18. Eliminar Proyecto")
        print("19. Eliminar Asignación")
        print("20. Eliminar Registro de Tiempo")
        print("21. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del empleado: ")
            direccion = input("Dirección del empleado: ")
            telefono = input("Teléfono del empleado: ")
            email = input("Email del empleado: ")
            fecha_contrato = input("Fecha de contrato (YYYY-MM-DD): ")
            salario = float(input("Salario del empleado: "))
            crear_empleado(nombre, direccion, telefono, email, fecha_contrato, salario)
        elif opcion == "2":
            nombre = input("Nombre del departamento: ")
            crear_departamento(nombre)
        elif opcion == "3":
            nombre = input("Nombre del proyecto: ")
            descripcion = input("Descripción del proyecto: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
            crear_proyecto(nombre, descripcion, fecha_inicio, fecha_fin)
        elif opcion == "4":
            empleado_id = int(input("ID del empleado: "))
            proyecto_id = int(input("ID del proyecto: "))
            asignar_proyecto(empleado_id, proyecto_id)
        elif opcion == "5":
            empleado_id = int(input("ID del empleado: "))
            proyecto_id = int(input("ID del proyecto: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            horas = float(input("Horas trabajadas: "))
            descripcion = input("Descripción del trabajo: ")
            registrar_tiempo(empleado_id, proyecto_id, fecha, horas, descripcion)
        elif opcion == "6":
            empleados = obtener_empleados()
            for empleado in empleados:
                print(empleado)
        elif opcion == "7":
            departamentos = obtener_departamentos()
            for departamento in departamentos:
                print(departamento)
        elif opcion == "8":
            proyectos = obtener_proyectos()
            for proyecto in proyectos:
                print(proyecto)
        elif opcion == "9":
            asignaciones = obtener_asignaciones()
            for asignacion in asignaciones:
                print(asignacion)
        elif opcion == "10":
            registros = obtener_registros_tiempo()
            for registro in registros:
                print(registro)
        elif opcion == "11":
            id = int(input("ID del empleado a actualizar: "))
            nombre = input("Nuevo nombre del empleado: ")
            direccion = input("Nueva dirección del empleado: ")
            telefono = input("Nuevo teléfono del empleado: ")
            email = input("Nuevo email del empleado: ")
            fecha_contrato = input("Nueva fecha de contrato (YYYY-MM-DD): ")
            salario = float(input("Nuevo salario del empleado: "))
            actualizar_empleado(id, nombre, direccion, telefono, email, fecha_contrato, salario)
        elif opcion == "12":
            id = int(input("ID del departamento a actualizar: "))
            nombre = input("Nuevo nombre del departamento: ")
            actualizar_departamento(id, nombre)
        elif opcion == "13":
            id = int(input("ID del proyecto a actualizar: "))
            nombre = input("Nuevo nombre del proyecto: ")
            descripcion = input("Nueva descripción del proyecto: ")
            fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
            actualizar_proyecto(id, nombre, descripcion, fecha_inicio, fecha_fin)
        elif opcion == "14":
            id = int(input("ID de la asignación a actualizar: "))
            empleado_id = int(input("Nuevo ID del empleado: "))
            proyecto_id = int(input("Nuevo ID del proyecto: "))
            actualizar_asignacion(id, empleado_id, proyecto_id)
        elif opcion == "15":
            id = int(input("ID del registro de tiempo a actualizar: "))
            empleado_id = int(input("Nuevo ID del empleado: "))
            proyecto_id = int(input("Nuevo ID del proyecto: "))
            fecha = input("Nueva fecha (YYYY-MM-DD): ")
            horas = float(input("Nuevas horas trabajadas: "))
            descripcion = input("Nueva descripción del trabajo: ")
            actualizar_registro_tiempo(id, empleado_id, proyecto_id, fecha, horas, descripcion)
        elif opcion == "16":
            id = int(input("ID del empleado a eliminar: "))
            eliminar_empleado(id)
        elif opcion == "17":
            id = int(input("ID del departamento a eliminar: "))
            eliminar_departamento(id)
        elif opcion == "18":
            id = int(input("ID del proyecto a eliminar: "))
            eliminar_proyecto(id)
        elif opcion == "19":
            id = int(input("ID de la asignación a eliminar: "))
            eliminar_asignacion(id)
        elif opcion == "20":
            id = int(input("ID del registro de tiempo a eliminar: "))
            eliminar_registro_tiempo(id)
        elif opcion == "21":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 21.")
