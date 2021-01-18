from tkinter import *


root = Tk()

texto = Text(root)
texto.pack()
texto.config(width= 40, height=15, padx=15, pady=15, font=("Curier, 10"), selectbackground="blue")

label = Label(root, text="Escribe aquí")
label.pack()
label.config(bg="Red", font="Curier, 20")


root.mainloop()