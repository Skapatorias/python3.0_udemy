edades = [12, 15, 6,93,73,43,54,41,28,63,21,11,32,12,9,1]

def mayores(edad):
    return edad >= 18

entrar = list(filter(mayores,edades))
print(entrar)