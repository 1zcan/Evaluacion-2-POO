import mysql.connector
from models.db import conectar

def crear_estudiante(nombre, edad, carrera):#Función para crear un estudiante
    conn = conectar()#Llamamos a la función conectar que se encuentra en el archivo db.py
    if conn is None:
        return
    cursor = conn.cursor()#Creamos un cursor, que nos permitirá ejecutar las consultas en la base de datos
    cursor.execute("INSERT INTO estudiantes (nombre, edad, carrera) VALUES (%s, %s, %s)", (nombre, edad, carrera))#Ejecutamos la consulta para insertar un nuevo estudiante en la tabla estudiantes
    conn.commit()#Confirmamos la transacción
    cursor.close()#Cerramos el cursor
    conn.close()#Cerramos la conexión


def obtener_estudiantes():
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    return estudiantes#Retornamos la lista de estudiantes

def buscar_estudiante_por_nombre(nombre):
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes WHERE nombre = %s", (nombre,))#Ejecutamos la consulta para buscar un estudiante por nombre, pasando el nombre como parámetro en una tupla
    estudiante = cursor.fetchone()
    cursor.close()
    conn.close()
    return estudiante

def actualizar_estudiante(nombre, nuevo_nombre, edad, carrera):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE estudiantes SET nombre = %s, edad = %s, carrera = %s WHERE nombre = %s", (nuevo_nombre, edad, carrera, nombre))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_estudiante(nombre):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE nombre = %s", (nombre,))
    conn.commit()
    cursor.close()
    conn.close()