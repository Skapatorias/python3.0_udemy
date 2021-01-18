menu = """
Bienvenido al conversor de monedas 💲
1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = input (menu)


if opcion == "1": 
    pesos = float(input("¿Cuántos pesos colombianos tienes?"))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes " + dolares + " dólares. ")
    
elif opcion =="2":
    pesos = float(input("¿Cuántos pesos argentinos tienes?"))
    valor_dolar = 75
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes " + dolares + " dólares. ")
    
elif opcion =="3":
    pesos = float(input("¿Cuántos pesos mexicanos tienes?"))
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes " + dolares + " dólares. ")
    
else:
    print ("Ingresa una opción correcta")
