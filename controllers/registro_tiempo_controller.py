from models import registro_tiempo

class RegistroTiempoController:
    def __init__(self):
        self.registros = []

    def create(self, id, empleado_id, fecha, horas, descripcion, proyecto_id):
        nuevo_registro = registro_tiempo(id, empleado_id, fecha, horas, descripcion, proyecto_id)
        self.registros.append(nuevo_registro)
        return nuevo_registro

    def read(self, id):
        for registro in self.registros:
            if registro.id == id:
                return registro
        return None

    def update(self, id, empleado_id=None, fecha=None, horas=None, descripcion=None, proyecto_id=None):
        registro = self.read(id)
        if registro:
            if empleado_id is not None:
                registro.empleado_id = empleado_id
            if fecha is not None:
                registro.fecha = fecha
            if horas is not None:
                registro.horas = horas
            if descripcion is not None:
                registro.descripcion = descripcion
            if proyecto_id is not None:
                registro.proyecto_id = proyecto_id
            return registro
        return None

    def delete(self, id):
        registro = self.read(id)
        if registro:
            self.registros.remove(registro)
            return True
        return False

    def list_all(self):
        return self.registros