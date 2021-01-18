from tkinter import *

root = Tk()


texto_nuevo = StringVar()
texto_nuevo.set("Python")

root.title("Bienvenidos")
root.config(width=400, height=300)

label = Label(root, text="Hola Mundo")
label.place(x=100, y=70)
label.config(bg="blue", fg="red", font=("Curier", 20))


label = Label(root, text="Bienvenidos")
label.place(x=150,y=120)
label.config(bg="red", fg="blue", font=("Curier", 20), textvariable=texto_nuevo)


root.mainloop()