import mysql.connector
from models.db import conectar
from models.empleados import empleados

def crear_empleado(nombre, direccion, telefono, email, fecha_contrato, salario):
    #Función para crear un empleado.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO empleados (nombre, direccion, telefono, email, fecha_contrato, salario) VALUES (%s, %s, %s, %s, %s, %s)",
            (nombre, direccion, telefono, email, fecha_contrato, salario)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def obtener_empleados():
    # Función para obtener todos los empleados.
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM empleados")
        empleados = cursor.fetchall()
        return [empleado for empleado in empleados]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()


def buscar_empleado_por_id(id):
    #Función para buscar un empleado por nombre.
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM empleados WHERE id = %s", (id,))
        empleado = cursor.fetchone()
        if empleado:
            return empleados(*empleado)
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def actualizar_empleado(id, nuevo_nombre, direccion, telefono, email, fecha_contrato, salario):
    #Función para actualizar un empleado.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE empleados SET nombre = %s, direccion = %s, telefono = %s, email = %s, fecha_contrato = %s, salario = %s WHERE id = %s",
            (nuevo_nombre, direccion, telefono, email, fecha_contrato, salario, id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_empleado(id):
    #Función para eliminar un empleado.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM empleados WHERE id = %s", (id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
