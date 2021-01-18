class Coche:
    def __init__(self,marca,kilometros,anio):
        self.marca = marca
        self.kilometros = kilometros
        self.anio = anio
        print(f'Se ha creado un auto {marca}')

    def __del__(self):
        print ("Se ha vendido el auto", self.marca)

    def __str__(self):
        return (f'EL auto es un {self.marca} con {self.kilometros} kilómetros y es del año {self.anio}.')


miCoche = Coche("Audi", 2000, 2020)
print(str(miCoche))
del(miCoche)
