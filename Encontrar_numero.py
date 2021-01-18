import random

def run (less, higher):
    number_found = False
    random_number = random.randint (less, higher)
    intentos = 0

    while not number_found:
        intentos += 1
        number = int (input("Intenta un número: "))
        if number == random_number:
            print ("Encontraste el numero!!!")
            print ("Lo encontraste en {}".format(intentos))
            number_found = True
        elif number > random_number:
            print ("El número es más pequeño")
        else:
            print ("El número es más grande")


if __name__ == "__main__":
    print("******************")
    less= int(input("Ingrese el número mínimo"))
    print("******************")
    print("******************")
    higher = int(input("Ingrese el numero máximo"))
    print("******************")
    run(less,higher)