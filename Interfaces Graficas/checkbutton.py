from tkinter import *

def eleccion():
    elegir = ""

    if pollo.get()==1:
        elegir+= "Has elegido Pollo\n"
    if pizza.get()==1:
        elegir+= "Has elegido Pizza\n"
    if hambur.get()==1:
        elegir+= "Has elegido Hamburguesa\n"
    if pollo.get()==1 and pizza.get()==1 and hambur.get()==1:
        elegir+= """
        Tu orden final es: [MENU COMPLETO]"""

    imprimir.config(text=elegir)


root = Tk()
root.geometry("400x300")

frame = Frame(root)
frame.pack()

pollo = IntVar()
pizza = IntVar()
hambur = IntVar()

foto_pollo = PhotoImage(file="pollo.gif")
foto_pizza = PhotoImage(file="pizza.gif")
foto_hamburguesa = PhotoImage(file="hamburguesa.gif")

Label(root, image=foto_pollo).pack()
Label(root, image=foto_pizza).pack()
Label(root, image=foto_hamburguesa).pack()

Checkbutton(frame, text="Pizza", variable=pizza, onvalue=1, offvalue=0, command=eleccion).pack(side="right")
Checkbutton(frame, text="Hamburguesa", variable=hambur, onvalue=1, offvalue=0, command=eleccion).pack(side="right")
Checkbutton(frame, text="Pollo", variable=pollo, onvalue=1, offvalue=0, command=eleccion).pack(side="right")

imprimir = Label(root)
imprimir.pack()

root.mainloop()