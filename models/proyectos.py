class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    def __repr__(self):
        return f"Proyecto({self.nombre}, {self.descripcion}, {self.fecha_inicio})"
