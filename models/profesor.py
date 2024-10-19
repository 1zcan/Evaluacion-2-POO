from models.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y enseño {self.materia}."
