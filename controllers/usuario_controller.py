from models.usuario import Usuario
from models.db import DB
import bcrypt

def agregar(nuevo_usuario: Usuario) -> bool:
    nuevo_usuario.contrasena = bcrypt.hashpw(nuevo_usuario.contrasena.encode("UTF-8"), bcrypt.gensalt(14))

    cursor = DB.get_connection().cursor()
    query = "INSERT INTO usuarios (username, contrasena) VALUES (%s, %s)"     
    parametros = [nuevo_usuario.username, nuevo_usuario.contrasena]
    cursor.execute(query, parametros)
    DB.get_connection().commit()
    cursor.close()
    return True

def editar(id_usuario: int, usuario_editado: Usuario) -> bool:
    cursor = DB.get_connection().cursor()
    query = "UPDATE usuarios SET username = %s, contrasena = %s WHERE idEmpleado = %s"
    parametros = [usuario_editado.username, usuario_editado.contrasena, id_usuario]
    cursor.execute(query, parametros)
    DB.get_connection().commit()
    cursor.close()
    return True

def mostrar_uno(id_usuario: int) -> Usuario:
    cursor = DB.get_connection().cursor()
    query = "SELECT * FROM usuarios WHERE idEmpleado = %s"
    cursor.execute(query, [id_usuario])

    usuario = None
    for (username, contrasena, idRol, idEmpleado) in cursor:
        usuario = Usuario(username, bytes(contrasena.encode("UTF-8")), idRol, idEmpleado)

    cursor.close()
    return usuario

def mostrar_todos() -> list:
    cursor = DB.get_connection().cursor()
    query = "SELECT * FROM usuarios"
    cursor.execute(query)

    usuarios = []
    for (username, contrasena, idRol, idEmpleado) in cursor:
        usuarios.append(Usuario(username, bytes(contrasena.encode("UTF-8")), idRol, idEmpleado))

    cursor.close()
    return usuarios

def eliminar(id_usuario: int) -> bool:
    cursor = DB.get_connection().cursor()
    query = "DELETE FROM usuarios WHERE idEmpleado = %s"
    cursor.execute(query, [id_usuario])
    DB.get_connection().commit()
    cursor.close()
    return True