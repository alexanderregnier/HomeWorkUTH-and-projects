# Autor: José Padilla Duarte
# Grupo: TIDS1-1

from tkinter import *
from tkinter import messagebox
from utilerias import *

#------------------------ Funciones --------------------------
def calcular_com():
    try: 
        estatura = int(estatura_sv.get())
        edad = int(edad_sv.get())
        if sexo_sv.get() == "F":
            peso = 20 * pow(estatura/100, 2) + (edad/10) * 0.9
        else:
            peso = 24 * pow(estatura/100, 2) + (edad/10) * 0.9
        peso_sv.set(format(peso, ".3f"))
    except:
        messagebox.showwarning("Aviso", "Error en los datos.")

#--------------------- Código Principal ----------------------
limpiar_consola()
root = Tk()
root.title("Calcula tu peso promedio (complexión normal) - JPD")
root.geometry(geometryCentrado(root, 500, 180))
root.resizable(width=False, height=False)

# StringVars necesarias:
estatura_sv = StringVar()
edad_sv = StringVar()
sexo_sv = StringVar()
peso_sv = StringVar()
estatura_sv.set(165)
edad_sv.set(18)

lfrm = LabelFrame(root, text="Sexo", width=210, height=60)
lfrm.place(x=10, y=10)

rbFem = Radiobutton(lfrm, text="Femenino", value="F", variable=sexo_sv)
rbFem.place(x=10, y=7)
rbMas = Radiobutton(lfrm, text="Masculino", value="M", variable=sexo_sv)
rbMas.place(x=110, y=7)
rbFem.select()

label1 = Label(root, text="Estatura en cms:")
label1.place(x=10, y=100)
spEstatura = Spinbox(root, from_=140, to=210, justify="center", textvariable=estatura_sv)
spEstatura.place(x=120, y=100, width=60)

label2 = Label(root, text="Edad:")
label2.place(x=10, y=130)
spEdad = Spinbox(root, from_=10, to=100, justify="center", textvariable=edad_sv)
spEdad.place(x=120, y=130, width=60)

label3 = Label(root, text="Peso en kg:")
label3.place(x=250, y=40)
entryPeso = Entry(root, state=DISABLED, justify="right", bd=4, width=12, 
    textvariable=peso_sv, font=("Helvetica", "12", "bold"))
entryPeso.place(x=330, y=40)

btnCalcular = Button(root, text="Calcular", width=15, height=2, command=calcular_com)
btnCalcular.place(x=320, y=100)

root.mainloop()