import pickle

lista = ["Maria", "Jose", "Pedro", "Rosa"]

fichero = open("lista_nombres", "wb")

pickle.dump(lista,fichero)

fichero.close()