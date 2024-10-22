import mysql.connector
from models.db import conectar
from models.proyectos import Proyecto

def crear_proyecto(nombre, descripcion, fecha_inicio):
    
    #Función para crear un proyecto.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO proyectos (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)",
            (nombre, descripcion, fecha_inicio)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def obtener_proyectos():
    
    #Función para obtener todos los proyectos.
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM proyectos")
        proyectos = cursor.fetchall()
        return [Proyecto(*proyecto) for proyecto in proyectos]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def buscar_proyecto_por_id(id):
    
    #Función para buscar un proyecto por ID.
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM proyectos WHERE id = %s", (id,))
        proyecto = cursor.fetchone()
        if proyecto:
            return Proyecto(*proyecto)
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def actualizar_proyecto(id, nombre, descripcion, fecha_inicio):
    
    #Función para actualizar un proyecto.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE proyectos SET nombre = %s, descripcion = %s, fecha_inicio = %s WHERE id = %s",
            (nombre, descripcion, fecha_inicio, id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_proyecto(id):
    
    #Función para eliminar un proyecto.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM proyectos WHERE id = %s", (id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()