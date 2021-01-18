from io import open


fichero = open("Archivo.txt", "w")
texto = "Hola estamos trabajando con los ficheros de python"
fichero.write(texto)
fichero.close()

