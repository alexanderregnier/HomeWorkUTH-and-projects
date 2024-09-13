# Autor: José Padilla Duarte
# Grupo: TIDS1-1

from tkinter import *
from tkinter import messagebox
from utilerias import *
from datetime import date, datetime

#------------------------------------ Funciones -------------------------------------
def aceptar_com():
    nombre = nombre_sv.get().strip()
    carrera = carrera_sv.get().strip()
    fecha = fecha_sv.get().strip()
    if len(nombre)==0:
        messagebox.showinfo("Aviso", "Faltan datos")
        return      # De aquí no pasas
    if len(fecha)>0:
        try:
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Aviso", f"La fecha introducida no es correcta: {fecha}")
            return      # De aquí no pasas
    
    mensaje = nombre + " comenzó a estudiar " + carrera + " el día " + format(fecha.date(), "%d/%m/%Y") + "."
    messagebox.showinfo("Aviso", mensaje)

#--------------------------------- Código principal ---------------------------------
limpiar_consola()
root = Tk()
root.title("Práctica 1 hecha por José Padilla D.")
root.geometry(geometryCentrado(root, 400, 160))
root.resizable(width=False, height=False)

nombre_sv = StringVar()
carrera_sv = StringVar()
fecha_sv = StringVar()
fecha_sv.set( format(date.today(), "%d/%m/%Y") )    # Tomar la fecha del SO y ponerla en el formato "DD/MM/AAAA"

eti1 = Label(root, text="Nombre:")
eti1.place(x=10, y=10)
ent1 = Entry(root, width=30, textvariable=nombre_sv)
ent1.place(x=80, y=10)

eti2 = Label(root, text="Carrera:")
eti2.place(x=10, y=40)
ent2 = Entry(root, width=40, textvariable=carrera_sv)
ent2.place(x=80, y=40)

eti3 = Label(root, text="Fecha de Inicio:")
eti3.place(x=10, y=70)
ent3 = Entry(root, textvariable=fecha_sv)
ent3.place(x=110, y=70)

btnAceptar = Button(root, text="Aceptar", width=12, command=aceptar_com)
btnAceptar.place(x=90, y=110)
btnCancelar = Button(root, text="Cancelar", width=12, command=root.destroy)
btnCancelar.place(x=210, y=110)

root.mainloop()