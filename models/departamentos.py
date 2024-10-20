class Departamento:
    def __init__(self, id, nombre, gerente_id, gerente):
        self.id = id
        self.nombre = nombre
        self.gerente_id = gerente_id  # ID del gerente, referencia a la tabla empleados
        self.gerente = gerente  # Objeto de la clase Empleado

    def descripcion(self):
        return (
            f"El departamento de {self.nombre} está a cargo de {self.gerente.nombre}."
        )

    def __repr__(self):
        return f"Departamento({self.nombre}, Gerente: {self.gerente.nombre})"
