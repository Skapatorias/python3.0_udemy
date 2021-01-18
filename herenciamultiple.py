
class Clase1:
    def saluda(self):
        print("Soy el metodo de la clase 1")


class Clase2:
    def metodo2(self):
        print("Soy el metodo de la clase 2")


class Clase3(Clase1, Clase2):
    def metodo3(self):
        print("Soy el metodo de la clase 2")


c = Clase3()
c.saluda()
c.metodo3()
c.metodo2()