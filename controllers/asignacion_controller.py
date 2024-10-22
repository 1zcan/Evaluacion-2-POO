import mysql.connector
from models.db import conectar
from models.asignacion import Asignacion

def crear_asignacion(empleado_id, departamento_id):
    
    #Función para crear una asignación.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO asignaciones (empleado_id, departamento_id) VALUES (%s, %s)",
            (empleado_id, departamento_id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def obtener_asignaciones():
    
    #Función para obtener todas las asignaciones.
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM asignaciones")
        asignaciones = cursor.fetchall()
        return [Asignacion(*asignacion) for asignacion in asignaciones]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def buscar_asignacion_por_empleado(empleado_id):
    
    #Función para buscar una asignación por ID de empleado.
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM asignaciones WHERE empleado_id = %s", (empleado_id,))
        asignacion = cursor.fetchone()
        if asignacion:
            return Asignacion(*asignacion)
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def actualizar_asignacion(empleado_id, departamento_id):
    
    #Función para actualizar una asignación.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE asignaciones SET departamento_id = %s WHERE empleado_id = %s",
            (departamento_id, empleado_id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_asignacion(empleado_id):
    
    #Función para eliminar una asignación.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM asignaciones WHERE empleado_id = %s", (empleado_id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
