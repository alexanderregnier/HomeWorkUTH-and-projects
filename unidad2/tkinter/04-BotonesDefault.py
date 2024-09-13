from tkinter import *

root = Tk()
root.title("Botones Default")
root.geometry("300x200")

def seleccionar(opcion):
    print(opcion)

Button(root, text="Python", command=lambda: seleccionar("Python")).pack()
Button(root, text="Java", command=lambda: seleccionar("Java")).pack()
Button(root, text="C++", command=lambda: seleccionar("C++")).pack()

root.mainloop()