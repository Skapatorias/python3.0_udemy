

lista = []

lista.append(1)
lista.append("Carlos")
lista.append("Maria")

lista.clear()
lista.append("Carlos")
lista2 = ["Rosario", "Anibal", "Antonio"]
lista.extend(lista2)
lista.append("Juan")
lista.insert(0, "Rosa")


print(lista)
print(lista.count("Anibal"))
print(lista.index("Rosario"))

