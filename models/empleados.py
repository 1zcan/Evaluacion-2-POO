class empleados:
    def __init__(self, id, nombre, direccion, telefono, email, fecha_contrato, salario):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_contrato = fecha_contrato
        self.salario = salario
        self.proyectos = []  # Lista de proyectos asignados al empleado

    def asignar_proyecto(self, proyecto):
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)

    def presentarse(self):
        return f"Hola, soy {self.nombre}, vivo en {self.direccion}, mi teléfono es {self.telefono}, mi email es {self.email}, fui contratado el {self.fecha_contrato} y mi salario es {self.salario}."

    def __repr__(self):
        return f"Empleado({self.nombre}, {self.direccion}, {self.telefono}, {self.email}, {self.fecha_contrato}, {self.salario})"
