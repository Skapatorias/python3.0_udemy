from io import open


fichero = open("Archivo.txt", "r")

#print(fichero.read(5))
#print(fichero.readlines())
#fichero.seek(10)
#print(fichero.read())

fichero.seek(len(fichero.readline()))
print(fichero.read())

fichero.close()