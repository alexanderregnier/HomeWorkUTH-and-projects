'''
Archivo: Main_SJDGF.py

Autor: Sadrach Juan Diego Garica Flores
Email: Jdiego0805@gmail.com
Fecha de última modificación: 20-febrero-2024

'''
from mis_funciones import *
from cls_archivo_JSON import *
from cls_datagridSB import *

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

App_Name = "Mis contactos SJDGF"

def geometryCentrado(tk_obj, ancho_ventana, alto_ventana):
    ancho_pantalla = tk_obj.winfo_screenwidth()
    alto_pantalla = tk_obj.winfo_screenheight()
    w_pos = int(ancho_pantalla/2 - ancho_ventana/2)
    h_pos = int(alto_pantalla/2 - alto_ventana/2)
    return f"{ancho_ventana}x{alto_ventana}+{w_pos}+{h_pos}"

class main():
    def __init__(self) -> None:
        self.Datos = []
        self.Archivo = ArchivoJSON('contactos.json')
        Cls()
        if self.Archivo.Existe():
            self.Datos=self.Archivo.TomarContenido()
            mensaje = f"hay {len(self.Datos)} contactos en el archivo '{self.Archivo.nombre}'"
            if len(self.Datos)>0:
                mensaje += "\n\n Sus datos han sido cargados"
            msg.showinfo(App_Name, mensaje)
        else:
            resp = msg.askquestion(App_Name, f"El archvo '{self.Archivo.nombre}' no ha sido creado ¿Desea crearlo?")
            if resp == "yes":
                self.Archivo.CrearNuevo()
                msg.showerror(App_Name, f"El archvo '{self.Archivo.nombre}' ha sido creado")
            else:
                msg.showinfo("", f"El programa termina su ejecucion.")
                exit("El programa ha finalizado.")

        self.Datos = self.Archivo.TomarContenido()
        mainWin = Tk()
        mainWin.title(App_Name)
        mainWin.geometry(geometryCentrado(mainWin, 700,340))
        mainWin.resizable(width=False, height=False)

        self.dg1 = DataGridSB(mainWin, _x=10, _y=10, _width=700, _height=284, _background="gray")
        self.dg1.crearColumnas(("nombre", "teléfono", "email"))

        self.dg1.anchoColumna("#0",_width=40, _minwidth=40, _stretch=tk.NO)
        self.dg1.anchoColumna("nombre",_width=200, _minwidth=40, _stretch=tk.NO)
        self.dg1.anchoColumna("teléfono",_width=200, _minwidth=40, _stretch=tk.NO)
        self.dg1.anchoColumna("email",_width=200, _minwidth=40, _stretch=tk.NO)

        self.dg1.encabezadoColumna("#0", "NO", 'w')
        self.dg1.encabezadoColumna("nombre", "Nombre", 'w')
        self.dg1.encabezadoColumna("teléfono", "Teléfono", 'w')
        self.dg1.encabezadoColumna("email", "Email", 'w')

        n = 0 
        for r in self.Datos:
            n += 1
            self.dg1.agregarRenglon("", n, n, (r['nombre'], r['teléfono'], r['email']))
        print("total contactos encontrados", n)

        btnAgregar = ttk.Button(mainWin, text="Agregar", width=15, command=lambda: self.agregar(mainWin))
        pos_x = 70
        pos_y = 300
        btnAgregar.place(x=pos_x, y=pos_y)

        btnBuscar= ttk.Button(mainWin, text="Buscar", width=15, command=lambda:self.buscar(mainWin))
        pos_x += 150
        btnBuscar.place(x=pos_x, y=pos_y)

        btnEliminar= ttk.Button(mainWin, text="Eliminar", width=15, command=self.eliminar)
        pos_x += 150
        btnEliminar.place(x=pos_x, y=pos_y)
        
        btnSalir= ttk.Button(mainWin, text="Salir", width=15, command=mainWin.destroy)
        pos_x += 150
        btnSalir.place(x=pos_x, y=pos_y)

        mainWin.focus_force()
        mainWin.mainloop()

    def agregar(self,master_win):
        winAgregar = Toplevel(master_win)
        winAgregar.grab_set()
        winAgregar.title("Agregar contacto")
        winAgregar.geometry(geometryCentrado(winAgregar, 300, 160))
        winAgregar.resizable(width=False, height=False)

        nombre_sv = StringVar(winAgregar)
        telefono_sv = StringVar(winAgregar)
        email_sv = StringVar(winAgregar)

        label1 = ttk.Label(winAgregar, text="Nombre:")
        label1.place(x=10, y=10)
        entry1 = tk.Entry(winAgregar, textvariable=nombre_sv, width=25)
        entry1.place(x=80, y=10)       

        label2 = ttk.Label(winAgregar, text="Teléfono:")
        label2.place(x=10, y=40)
        entry2 = tk.Entry(winAgregar, textvariable=telefono_sv, width=25)
        entry2.place(x=80, y=40)

        label3 = ttk.Label(winAgregar, text="email:")
        label3.place(x=10, y=70)
        entry3 = tk.Entry(winAgregar, textvariable=email_sv, width=25)
        entry3.place(x=80, y=70)

        btnAceptar = ttk.Button(winAgregar, text="Aceptar", width=13,
command=lambda: self._agregar_aprobado(winAgregar, nombre_sv, telefono_sv, email_sv))
        btnAceptar.place(x=30, y=110)
        btnCancelar = tk.Button(winAgregar, text="Cancelar", width=13, command=winAgregar.destroy)
        btnCancelar.place(x=170, y=110)
        winAgregar.focus_force()

    def _agregar_aprobado(self, master_win, nom_sv, tel_sv, em_sv):
        nombre = nom_sv.get().strip()
        teléfono = tel_sv.get().strip()
        email = em_sv.get().strip()
        if nombre == "" or teléfono == "":
            msg.showwarning("El contacto no se agregó","El nombre y el teléfono son obligatorios.")
        else:
            dicc = { 'nombre' : nombre, 'teléfono': teléfono, 'email': email }
            self.Datos.append(dicc)
            self.Archivo.ActualizarContenido(self.Datos)
            n = len(self.dg1.tvw1.get_children())
            n += 1
            self.dg1.agregarRenglon("", n, n, (nombre, teléfono, email))
            print("Total contactos registrados:", n)
            self._ubicar_contacto(nombre)
            msg.showinfo(App_Name,f"El contacto '{nombre}' ha sido agregado.")
        master_win.destroy()

    def buscar (self, MasterWin):
        winBuscar = Toplevel(MasterWin)
        winBuscar.grab_set()
        winBuscar.title("buscar contacto")
        winBuscar.geometry(geometryCentrado(winBuscar, 300, 120))
        winBuscar.resizable(width=False, height=False)

        info_sv = StringVar(winBuscar)
        label1 = ttk.Label(winBuscar, text="Introduzca el nombre a buscar:")
        label1.place(x=10, y=10)
        entry1 = ttk.Entry(winBuscar, textvariable=info_sv, width=38)
        entry1.place(x=10, y=35)
        btnAceptar = tk.Button(winBuscar, text="Aceptar", width=13, command=lambda: self._ubicar_contacto(info_sv.get()))
        btnAceptar.place(x=30, y=70)
        btnCancelar = tk.Button(winBuscar, text="Cancelar", width=13, command=winBuscar.destroy)
        btnCancelar.place(x=165, y=70)
        winBuscar.focus_force()

    def _ubicar_contacto(self, nom:str):
        nombre = nom.strip()
        encontrado = False
        if nombre !="":
            for parent in self.dg1.tvw1.get_children():
                if str(self.dg1.tvw1.item(parent)['values'][0]).__contains__(nombre):
                    self.dg1.tvw1.selection_set(parent)
                    encontrado = True
                    break
            if not encontrado:
                msg.showerror(App_Name, f"El contacto '{nombre}' no se encuentra.")

    def eliminar(self):
        indice = []
        for r in self.Datos:
            indice.append(r['nombre'])
        for selected_item in self.dg1.tvw1.selection():
            item = self.dg1.tvw1.item(selected_item)
            record = item['values']
            # print (record) 
            respuesta = msg.askquestion("¿Desea eliminar el contacto?", record)
            if respuesta == "yes":
                del self.Datos[ indice.index( str(record[0])) ]
                self.Archivo.ActualizarContenido(self.Datos)
                print("Se ha borrado el registro:",record)

                for r in self.dg1.tvw1.get_children():
                    self.dg1.tvw1.delete(r)     # Borrar renglores del treeview

                n = 0
                for r in self.Datos:    # Recargar el treeview con los datos que quedaron
                    n += 1
                    self.dg1.agregarRenglon("", n, n, (r['nombre'], r['teléfono'], r['email']))
#───────────────────────────────────────────────────────────────────────────────────────
main()
