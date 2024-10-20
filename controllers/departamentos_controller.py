import mysql.connector
from models.db import conectar
from models.empleados import Empleado
from models.departamentos import Departamento

def crear_departamento(nombre, gerente_id):
    # Función para crear un departamento
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO departamentos (nombre, gerente_id) VALUES (%s, %s)",
            (nombre, gerente_id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def obtener_departamentos():
    # Función para obtener todos los departamentos
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT d.id, d.nombre, d.gerente_id, e.nombre FROM departamentos d JOIN empleados e ON d.gerente_id = e.id")
        departamentos = cursor.fetchall()
        return [Departamento(id, nombre, gerente_id, Empleado(gerente_id, gerente_nombre, None, None, None, None, None)) for id, nombre, gerente_id, gerente_nombre in departamentos]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def buscar_departamento_por_nombre(nombre):
    # Función para buscar un departamento por nombre
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT d.id, d.nombre, d.gerente_id, e.nombre FROM departamentos d JOIN empleados e ON d.gerente_id = e.id WHERE d.nombre = %s", (nombre,))
        departamento = cursor.fetchone()
        if departamento:
            id, nombre, gerente_id, gerente_nombre = departamento
            return Departamento(id, nombre, gerente_id, Empleado(gerente_id, gerente_nombre, None, None, None, None, None))
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def actualizar_departamento(id, nombre, gerente_id):
    # Función para actualizar un departamento
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE departamentos SET nombre = %s, gerente_id = %s WHERE id = %s",
            (nombre, gerente_id, id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_departamento(id):
    # Función para eliminar un departamento
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM departamentos WHERE id = %s", (id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
