# Autor: José Padilla Duarte
# Grupo: TIDS1-1

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as font
from utilerias import *

#------------------------ Funciones --------------------------
def aceptar_com():
    nombre = nombre_sv.get().strip()
    bebida = bebida_sv.get().strip()
    num_sobres = sobres_iv.get()
    endulzante = endulzante_sv.get()
    
    if nombre == "":
        messagebox.showwarning("Aviso", "Debe escribir el nombre.")
        return
    if bebida == "":
        messagebox.showwarning("Aviso", "Debe escoger una bebida.")
        return   

    mensaje = "Orden a nombre de: " + nombre + ".\nBebida: " + bebida + \
        "\nEndulzante: " + str(num_sobres) + " sobre(s) de " + endulzante + \
        "\nTotal a pagar: $"
        
    match bebida:
        case "Café Americano":
            precio = 25
        case "Capuccino":
            precio = 40
        case "Chocolate":
            precio = 30
        case "Frappé":
            precio = 45
        case "Te Chai":
            precio = 35
        case _:
            precio = 9999

    mensaje += str(precio)
    messagebox.showinfo("Orden de bebida", mensaje)


def cancelar_com():
    nombre_sv.set("")
    bebida_sv.set("")
    endulzante_sv.set("azúcar")
    sobres_iv.set(1)

#--------------------- Código Principal ----------------------
limpiar_consola()
messagebox.showinfo("Aviso", "Bienvenidos a Coyote Coffee Shop ☕")
root = Tk()
root.title("Coyote Coffe Shop ☕ - JPD")
root.geometry(geometryCentrado(root, 700, 280))
root.resizable(width=False, height=False)

# Vars necesarias:
nombre_sv = StringVar()
bebida_sv = StringVar()
endulzante_sv = StringVar()
sobres_iv = IntVar()
sobres_iv.set(1)

lbNombre = Label(root, text="Nombre:")
lbNombre.place(x=10, y=30)
enNombre = Entry(root, width=24, textvariable=nombre_sv)
enNombre.place(x=80, y=30)

lbBebida = Label(root, text="Bebida:")
lbBebida.place(x=10, y=70)
cboBebida = ttk.Combobox(root, textvariable=bebida_sv)
cboBebida['values'] = ('Café Americano', 'Capuccino', 'Chocolate', 'Frappé', 'Te Chai')
cboBebida['state'] = 'readonly'
cboBebida.place(x=80, y=70)

lbInfo = Label(root, text="Precios:     ")
lbInfo['font'] = font.Font(size=11, weight="bold")
lbInfo['text'] += "\nCafé Americano $25\nCapuccino $40\nChocolate $30\nFrappé $45\nTe Chai $35"
lbInfo['justify'] = "right"
lbInfo.place(x=300, y=10)

lfrm = LabelFrame(root, text="Endulzante:", width=400, height=60)
lfrm.place(x=30, y=120)

rbAzucar = Radiobutton(lfrm, text="azúcar", value="azúcar", variable=endulzante_sv)
rbAzucar.place(x=10, y=5)
rbSplenda = Radiobutton(lfrm, text="splenda", value="splenda", variable=endulzante_sv)
rbSplenda.place(x=100, y=5)
rbStevia = Radiobutton(lfrm, text="stevia", value="stevia", variable=endulzante_sv)
rbStevia.place(x=190, y=5)
rbAzucar.select()

lbSobres = Label(lfrm, text="Sobres:")
lbSobres.place(x=280, y=7)
spSobres = Spinbox(lfrm, from_=0, to=5, justify="center", textvariable=sobres_iv)
spSobres.place(x=340, y=7, width=50)

btnAceptar = Button(root, text="Aceptar", width=15, height=2, command=aceptar_com)
btnAceptar.place(x=30, y= 210)
btnCancelar = Button(root, text="Cancelar", width=15, height=2, command=cancelar_com)
btnCancelar.place(x=185, y= 210)
btSalir = Button(root, text="Salir", width=15, height=2, command=root.destroy)
btSalir.place(x=340, y= 210)

img = PhotoImage(file="capuccino.png")      # No permite imágenes JPG
img = img.subsample(3) 
lbImagen = Label(root, image=img)
lbImagen.place(x=485, y=20)

root.lift()         # traer la ventana tk al frente si finaliza la inicialización
root.focus_force()  # active la ventana tk
root.mainloop()