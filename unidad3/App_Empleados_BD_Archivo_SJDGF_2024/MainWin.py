# Autor: Sadrach Juan Diego Garicia Flores
# Grupo: 2-2
# Fecha: 07/03/2024

from cls_BD_MySQL import *
from mis_funciones import geometryCentrado
from tkinter import *
from winEmpleados import WinEmpleados
from WinUsuarios import WinUsuarios
from WinPuestos import WinPuestos

TITLE_HERE = "Venta principal del sistema o APP (by SAD34)"

class MainWin:
    def __init__(self) -> None:
        menuTk = Tk()
        menuTk.title = Tk(TITLE_HERE)
        menuTk.geometry(geometryCentrado(menuTk, 600, 400))

        barra_menus = Menu()
        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_catalogos = Menu(barra_menus,tearoff=False)

        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        barra_menus.add_cascade(menu=menu_catalogos, label="Catalogos")

        menu_archivo.add_command(label="salir", command=menuTk.destroy)
        menu_catalogos.add_command(label="Empleados",command=lambda:WinEmpleados(menuTk))
        menu_catalogos.add_command(label="puestos", command=lambda: WinPuestos(menuTk))
        menu_catalogos.add_command(label="Usuarios",command=lambda:WinUsuarios(menuTk))

        menuTk.config(menu=barra_menus)
        menuTk.focus_force()
        menuTk.mainloop()