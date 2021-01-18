

try:
    c= int(input("Ingrese un valor:"))
    c/0

except ZeroDivisionError:
    print("No se puede dividir por cero")

except ValueError:
    print("Ingrese numeros y no caracteres")

except Exception as c:
    print(type(c).__name__)