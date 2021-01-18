import sys

if len(sys.argv)==3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("Error: Introdujo uno (1) o mas de dos (2) argumentos")
    print("Solución: Introduzca los argumentos de forma correcta")
    print("Solucion: scripts.py 'texto' 'cantidad de repeticiones'")