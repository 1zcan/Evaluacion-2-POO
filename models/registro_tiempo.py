class registro_tiempo:
    def __init__(self, id, empleado_id, fecha, horas, descripcion, proyecto_id):
        self.id = id
        self.empleado_id = empleado_id
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion
        self.proyecto_id = proyecto_id

    def __repr__(self):
        return f"RegistroTiempo({self.id}, {self.empleado_id}, {self.fecha}, {self.horas}, {self.descripcion}, {self.proyecto_id})"