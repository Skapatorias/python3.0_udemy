

##def numeros():
##    i = 1
##    while i:
##        yield i
##        i += 1
##
##print(numeros())

def generaPares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1

devuelve = generaPares(10)
print(next(devuelve))
print(next(devuelve))
print(next(devuelve))

##
##def devuelve_paises(*paises):
##    for pais in paises:
##        yield pais

def devuelve_paises(*paises):
    for pais in paises:
        yield from pais




paises = devuelve_paises("Argentina", "Brasil", "Colombia", "Bolivia")
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))




