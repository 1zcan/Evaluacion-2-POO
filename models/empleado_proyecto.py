class empleado_proyecto:
    def __init__(self, empleado_id, proyecto_id):
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id

    def __repr__(self):
        return f"EmpleadoProyecto({self.empleado_id}, {self.proyecto_id})"