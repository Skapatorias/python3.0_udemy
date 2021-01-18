

class Persona():
    def __init__(self):
        self.cedula = 12345

    def mensaje(self):
        print("Este mensaje es de la clase persona")

class Obrero(Persona):
    def __init__(self):
        self.especialesta = 1

    def mensaje(self):
        print("Este mensaje es de la clase Obrero")

obrero_planta = Obrero()
obrero_planta.mensaje()
print()
print("*****************************************************")
print()

class Gato():
    def hablar(self):
        print("Miau")

class Perro(Gato):
    def hablar(self):
        print("Guau")

def escucharmascotas(animal):
    animal.hablar()

mascota = Perro()
escucharmascotas(mascota)