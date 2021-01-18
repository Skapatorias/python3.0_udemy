

set_conjunto1 = set({1,2,3,4})
print(set_conjunto1)

set_conjunto1.add(22)
set_conjunto1.add(1)
print(set_conjunto1)


set2 = {2,5,8,9}
print(set2)

paquete = set({"hola", 2, 3,5})
otropaq = paquete.copy()
print(otropaq)
paquete.discard("hola")
print(paquete)
paquete.remove(2)
print(paquete)


diccionario = {
    "clave1": 123,
    "clave2": True,
    "clave3": ["manzana", "pera", "naranja"]}
print(diccionario)

print(type(diccionario['clave1']))
print(type(diccionario['clave2']))
print(type(diccionario['clave3']))

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())


for i,c in diccionario.items():
    print (i,c)
