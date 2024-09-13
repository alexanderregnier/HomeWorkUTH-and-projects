from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Botones TTK")
root.geometry("300x200")

def seleccionar(opcion):
    print(opcion)

ttk.Button(root, text="Python", command=lambda: seleccionar("Python")).pack()
ttk.Button(root, text="Java", command=lambda: seleccionar("Java")).pack()
ttk.Button(root, text="C++", command=lambda: seleccionar("C++")).pack()

root.mainloop()