from tkinter import *

root = Tk()

imagen = PhotoImage(file="tierra.gif")

label = Label(root, image=imagen)
label.pack()

root.mainloop()