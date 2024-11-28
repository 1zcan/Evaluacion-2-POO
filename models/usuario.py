class Usuario:
    def __init__(self, username: str, contrasena: str, idRol: int, idEmpleado: int) -> None:
        self.username = username
        self.contrasena = contrasena
        # self.idRol = idRol
        # self.idEmpleado = idEmpleado

class UsuarioModelo():
    @staticmethod
    def autenticar(self, username: str, contrasena: str) -> Usuario:
        cursor = self.conexion.cursor()
        query = "SELECT * FROM usuario WHERE username = %s LIMIT 1"
        cursor.execute(query, [username])

        usuario = None
        for (username, contrasena_db, idRol, idEmpleado) in cursor:
            usuario = Usuario(username, bytes(contrasena_db.encode("UTF-8")), idRol, idEmpleado)
            if usuario.confirmar_contrasena(contrasena):
                cursor.close()
                return usuario

        cursor.close()
        return None