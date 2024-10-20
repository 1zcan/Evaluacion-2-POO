class asignacion_proyecto:
    def __init__(self, empleado_id, proyecto_id):
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id

    def __repr__(self):
        return f"AsignacionProyecto(Empleado ID: {self.empleado_id}, Proyecto ID: {self.proyecto_id})"

