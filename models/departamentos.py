class departamentos:
    def __init__(self, id, nombre, gerente_id):
        self.id = id
        self.nombre = nombre
        self.gerente_id = gerente_id

    def __repr__(self):
        return f"Departamento({self.id}, {self.nombre}, {self.gerente_id})"
