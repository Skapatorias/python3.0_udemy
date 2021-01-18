
def doblar(numero):
    return numero * 2


numeros = [2, 5, 10, 23, 50, 33]

i = map(doblar, numeros)

print(list(i))

###

numero = [2, 5, 10, 23, 50, 33]
j = map(lambda x: x*2, numero)
print(list(j))

###
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

i = map(lambda x, y: x*y, a,b)
print(list(i))