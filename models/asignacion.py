class asignacion:
    def __init__(self, empleado_id, departamento_id):
        self.empleado_id = empleado_id
        self.departamento_id = departamento_id

    def __repr__(self):
        return f"Asignacion({self.empleado_id}, {self.departamento_id})"
