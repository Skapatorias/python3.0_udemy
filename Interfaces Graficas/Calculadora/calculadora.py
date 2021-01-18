from tkinter import *

i= 0

def click(valor):
    global i
    entrada.insert(i,valor)
    i +=1

def borrar():
    entrada.delete(0, END)
    i=0

def operaciones():
    operacion = entrada.get()
    resultado = eval(operacion)
    entrada.delete(0,END)
    entrada.insert(0,resultado)
    i= 0

root = Tk()
root.title("Mi Calculadora")

#Entrda
entrada = Entry(root, font=("Curier 20"))
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Botones Numeros
boton1= Button(root, text="1", width=5, height=2, command=lambda:click(1))
boton2= Button(root, text="2", width=5, height=2, command=lambda:click(2))
boton3= Button(root, text="3", width=5, height=2, command=lambda:click(3))
boton4= Button(root, text="4", width=5, height=2, command=lambda:click(4))
boton5= Button(root, text="5", width=5, height=2, command=lambda:click(5))
boton6= Button(root, text="6", width=5, height=2, command=lambda:click(6))
boton7= Button(root, text="7", width=5, height=2, command=lambda:click(7))
boton8= Button(root, text="8", width=5, height=2, command=lambda:click(8))
boton9= Button(root, text="9", width=5, height=2, command=lambda:click(9))
boton0= Button(root, text="0", width=13, height=2, command=lambda:click(0))
#Botones Extras
boton_borrar= Button(root, text="AC", width=5, height=2, command=lambda:borrar())
boton_parentesis1= Button(root, text="(", width=5, height=2, command=lambda:click("("))
boton_parentesis2= Button(root, text=")", width=5, height=2, command=lambda:click(")"))
boton_punto= Button(root, text=".", width=5, height=2, command=lambda:click("."))

#Operaciones
boton_div= Button(root, text="/", width=5, height=2, command=lambda:click("/"))
boton_mul= Button(root, text="*", width=5, height=2, command=lambda:click("*"))
boton_sum= Button(root, text="+", width=5, height=2, command=lambda:click("+"))
boton_rest= Button(root, text="-", width=5, height=2, command=lambda:click("-"))
boton_igual= Button(root, text="=", width=5, height=2, command=lambda:operaciones())

#Colocar Botones
boton_borrar.grid(row=1, column=0, padx=3, pady=3)
boton_parentesis1.grid(row=1, column=1, padx=3, pady=3)
boton_parentesis2.grid(row=1, column=2, padx=3, pady=3)
boton_div.grid(row=1, column=3, padx=3, pady=3)

boton7.grid(row=2, column=0, padx=3, pady=3)
boton8.grid(row=2, column=1, padx=3, pady=3)
boton9.grid(row=2, column=2, padx=3, pady=3)
boton_mul.grid(row=2, column=3, padx=3, pady=3)

boton4.grid(row=3, column=0, padx=3, pady=3)
boton5.grid(row=3, column=1, padx=3, pady=3)
boton6.grid(row=3, column=2, padx=3, pady=3)
boton_sum.grid(row=3, column=3, padx=3, pady=3)

boton1.grid(row=4, column=0, padx=3, pady=3)
boton2.grid(row=4, column=1, padx=3, pady=3)
boton3.grid(row=4, column=2, padx=3, pady=3)
boton_rest.grid(row=4, column=3, padx=3, pady=3)

boton0.grid(row=5, column=0, columnspan=2, padx=3, pady=3)
boton_punto.grid(row=5, column=2, padx=3, pady=3)
boton_igual.grid(row=5, column=3, padx=3, pady=3)




root.mainloop()