

class Persona:
    def __init__(self, nombre, edad, apellido, sexo):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo


    def datosPersonales(self):
        print(f'{self.nombre} {self.apellido} tiene {self.edad} años')


miPersona = Persona ("Pepe", 20, "Gonzalez", "Masculino")
miPersona.datosPersonales()


class Empleado(Persona):

    def datosEmpleado(self, vacaciones, salario):
        print(f'Tiene {vacaciones} días de vacaciones y cobra {salario} pesos')

miPersona2 = Empleado("María", 30, "Luna", "Femenino")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(10, 30000)