
class Gelatina:
    def __init__(self, sabor, color, tamanio):
        self.sabor = sabor
        self.color = color
        self.tamanio = tamanio

    def imprimir(self):
        print("La gelatina es de " + self.sabor)
        print(f'La gelatina se de color {self.color}')
        print("La gelatina es "+ self.tamanio)


class Coche():
    def __init__(self):
        self.marca = "Audi"
        self.color = "rojo"
        self.ruedas = 4
        self.enMarcha = False

    def arrancar(self,arrancamos):
        self.enMarcha = arrancamos
        if(self.enMarcha):
            return "El coche está en marcha"
        else:
            return "El coche se encuentra apagado"

    def __str__(self):
        return (f'Este auto es de marca {self.marca}, de color {self.color} y tiene {self.ruedas} ruedas')


gel1 = Gelatina("frutilla", "rojo", "grande")
gel2 = Gelatina("mora", "azul", "chica")
gel3 = Gelatina ("naranja","naranja","mediana")
gel4 = Gelatina ("uva","violeta","chica")
gel1.imprimir()
gel2.imprimir()
gel3.imprimir()
gel4.imprimir()


miCoche = Coche()
print(miCoche.arrancar(1))

print(str(miCoche))
