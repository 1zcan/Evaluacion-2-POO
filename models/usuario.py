from models.db import DB
import bcrypt
class Usuario:
    def __init__(self, username: str, contrasena: str) -> None:
        self.username = username
        self.contrasena = contrasena
        # self.idRol = idRol
        # self.idEmpleado = idEmpleado
        
    def confirmar_contrasena(self, intento_contrasena: str) -> bool:
        # return bcrypt.checkpw(intento_contrasena.encode("UTF-8"), self.contrasena)
        return intento_contrasena == self.contrasena
class UsuarioModelo():
    @staticmethod
    def autenticar(username: str, contrasena: str) -> Usuario:
        cursor = DB.get_connection().cursor()
        query = "SELECT * FROM usuarios WHERE username = %s LIMIT 1"
        cursor.execute(query, [username])

        usuario = None
        for (username, contrasena_db) in cursor:
            # usuario = Usuario(username, bytes(contrasena_db.encode("UTF-8")))
            usuario = Usuario(username, contrasena_db)
            if usuario.confirmar_contrasena(contrasena):
                cursor.close()
                return usuario

        cursor.close()
        return None