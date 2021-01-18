from tkinter import *

root = Tk()

root.title("Mi primera ventana")   #TITULO VENTANA
root.resizable(1,1)                #SI SE PUEDE MODIFICAR ALTO Y ANCHO
root.iconbitmap("tierra.ico")       #ICONO
#root.geometry("600x350")  #TAMAÑO DE LA VENTANA


miFrame = Frame(root)                            #CREAMOS FRAME
#miFrame.pack(side=RIGHT, anchor="n")
miFrame.pack(fill="x", expand=True)                                   #SE EMPAQUETA FRAME
miFrame.config(width=400, height=300)            #PASO ANCHO Y ALTO
miFrame.config(cursor="pirate")                  #CAMBIAR CURSOR
miFrame.config(bg="red")                         #COLOR AL FRAME
miFrame.config(bd="10")                          #ANCHO BORDE
miFrame.config(relief="ridge")                   #FORMA BORDE


root.config(cursor="boat")                  #CAMBIAR CURSOR
root.config(bg="blue")                         #COLOR AL FRAME
root.config(bd="20")                          #ANCHO BORDE
root.config(relief="sunken")                   #FORMA BORDE



root.mainloop()          #MANTIENE VENTANA ABIERTA

