import mysql.connector
from models.db import conectar
from models.empleados import Empleado

def crear_empleado(nombre, direccion, telefono, email, fecha_contrato, salario):
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
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM empleados")
        empleados = cursor.fetchall()
        return [Empleado(*empleado) for empleado in empleados]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def buscar_empleado_por_nombre(nombre):
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM empleados WHERE nombre = %s", (nombre,))
        empleado = cursor.fetchone()
        if empleado:
            return Empleado(*empleado)
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def actualizar_empleado(id, nombre, direccion, telefono, email, fecha_contrato, salario):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE empleados SET nombre = %s, direccion = %s, telefono = %s, email = %s, fecha_contrato = %s, salario = %s WHERE id = %s",
            (nombre, direccion, telefono, email, fecha_contrato, salario, id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_empleado(id):
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
