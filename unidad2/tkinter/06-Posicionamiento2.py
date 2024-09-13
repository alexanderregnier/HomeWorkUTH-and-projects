from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Posicionar")
root.geometry("400x200")

def saludo():
    print("Hola te saludo")

def minimizar():
    root.iconify()

etiqueta1 = Label(root, text="Saluda desde aquí")
etiqueta1.place(x=30, y=50)

etiqueta2 = Label(root, text="Minimizar desde aquí")
etiqueta2.place(x=30, y=100)

boton1 = ttk.Button(root, text="Haz clic aquí para saludar", command=saludo, width=24)
boton1.place(x=200, y=50)

boton2 = ttk.Button(root, text="Haz clic aquí para minimizar", command=minimizar, width=24)
boton2.place(x=200, y=100)

boton3 = ttk.Button(root, text="Salir", command=quit)
boton3.place(x=300, y=150)

root.mainloop()