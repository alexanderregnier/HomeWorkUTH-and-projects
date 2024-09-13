from tkinter import *

root = Tk()
root.title("Mi primer ventana")
root.geometry("500x300")    

ancho = 300     # width
alto = 150      # height
# cadena_de_geometry = str(ancho) + "x" + str(alto)
cadena_de_geometry = f"{ancho}x{alto}"
print(cadena_de_geometry)
root.geometry(cadena_de_geometry)

# def imprimir():
#     print("Imprimiendo desde la ventana...")
def imprimir():
    etiq = Label(root, text="Imprimiendo...")
    etiq.pack()

boton1 = Button(root, text="Minimizar", command=root.iconify, bg="Red")
boton1.pack(side=LEFT)
boton2 = Button(root, text="Imprimir", command=imprimir, bg="Blue")
boton2.pack(side=RIGHT)

root.mainloop()