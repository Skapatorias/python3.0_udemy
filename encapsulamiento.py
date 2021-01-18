class Coche:
    def __init__(self):
        self.marca = "Audi"
        self.kilometros = 1000
        self.anio = 2020
        self.__ruedas = 4
        print(f'Se ha creado un auto {self.marca}')

    def __del__(self):
        print ("Se ha vendido el auto", self.marca)

    def __str__(self):
        return (f'EL auto es un {self.marca} con {self.kilometros} kilómetros, tiene {self.__ruedas} ruedas y es del año {self.anio}.')


miCoche = Coche()
miCoche.__ruedas = 100  # AL ESTAR ENCAPSULADO NO SE PUEDE MODIFICAR DESDE FUERA DEL OBJETO
print(str(miCoche))
del(miCoche)
