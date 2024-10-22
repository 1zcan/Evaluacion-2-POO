class empleados:
    def __init__(self, id, nombre, direccion, telefono, email, fecha_contrato, salario):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_contrato = fecha_contrato
        self.salario = salario

    def __repr__(self):
        return f"Empleado({self.id}, {self.nombre}, {self.direccion}, {self.telefono}, {self.email}, {self.fecha_contrato}, {self.salario})"
