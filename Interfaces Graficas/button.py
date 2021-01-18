from tkinter import *

def sumar():
    resultado.set(int(var1.get())+int(var2.get()))

def restar():
    resultado.set(int(var1.get())-int(var2.get()))


root = Tk()

frame = Frame(root)
frame.pack()

var1= StringVar()
var2= StringVar()
resultado= StringVar()

entrada1 = Entry(frame)
entrada1.pack()
entrada1.config(bd=10, font=("Curier 20"), textvariable=var1)

entrada2 = Entry(frame)
entrada2.pack()
entrada2.config(bd=10, font=("Curier 20"), textvariable=var2)

entrada3 = Entry(frame)
entrada3.pack()
entrada3.config(bd=10, font=("Curier 20"), state="disable", textvariable=resultado)

boton1 = Button(frame, text="SUMAR")
boton1.pack()
boton1.config(bd=5, font=("Curier 10"), command=sumar)

boton2 = Button(frame, text="RESTAR")
boton2.pack()
boton2.config(bd=5, font=("Curier 10"), command=restar)

root.mainloop()
