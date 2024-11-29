from models.usuario import Usuario
import bcrypt

def buscar_por_id_empleado(self, id_empleado: int) -> Usuario:
        cursor = self.conexion.cursor()
        query = "SELECT * FROM usuario WHERE idEmpleado = %s LIMIT 1"
        cursor.execute(query, [id_empleado])

        usuario = None
        for (username, contrasena, idRol, idEmpleado) in cursor:
            usuario = Usuario(username, bytes(contrasena.encode("UTF-8")), idRol, idEmpleado)

        cursor.close()
        return usuario

def agregar(self, nuevo_usuario: Usuario) -> bool:
    nuevo_usuario.contrasena = bcrypt.hashpw(nuevo_usuario.contrasena.encode("UTF-8"), bcrypt.gensalt(14))

    cursor = self.conexion.cursor()
    query = "INSERT INTO usuario (username, contrasena, idRol, idEmpleado) VALUES (%s, %s, %s, %s)"
    parametros = [nuevo_usuario.username, nuevo_usuario.contrasena, nuevo_usuario.idRol, nuevo_usuario.idEmpleado]
    cursor.execute(query, parametros)
    self.conexion.commit()
    cursor.close()
    return True
