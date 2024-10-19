import mysql.connector
from models.db import conectar

def crear_profesor(nombre, edad, materia):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("INSERT INTO profesores (nombre, edad, materia) VALUES (%s, %s, %s)", (nombre, edad, materia))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_profesores():
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesores")
    profesores = cursor.fetchall()
    cursor.close()
    conn.close()
    return profesores

def buscar_profesor_por_nombre(nombre):
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesores WHERE nombre = %s", (nombre,))
    profesor = cursor.fetchone()
    cursor.close()
    conn.close()
    return profesor

def actualizar_profesor(nombre, nuevo_nombre, edad, materia):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE profesores SET nombre = %s, edad = %s, materia = %s WHERE nombre = %s", (nuevo_nombre, edad, materia, nombre))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_profesor(nombre):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profesores WHERE nombre = %s", (nombre,))
    conn.commit()
    cursor.close()
    conn.close()