# Autor: Sadrach juan Diego Garcia Flores
# Grupo: TIDS2-2
# Fecha: 05/03/2024

from mis_funciones import *
from cls_BD_MySQL import *
from cls_datagridSB import *

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb

APP_NAME = "Mis Contactos - SJDGF"

def geometryCentrado(tk_obj, ancho_ventana, alto_ventana):
    ancho_pantalla = tk_obj.winfo_screenwidth()
    alto_pantalla = tk_obj.winfo_screenheight()
    w_pos = int(ancho_pantalla/2 - ancho_ventana/2)
    h_pos = int(alto_pantalla/2 - alto_ventana/2)
    return f"{ancho_ventana}x{alto_ventana}+{w_pos}+{h_pos}"


def imprimirInfoDeDicc(un_dicc:dict):
    print(f"Información del objeto: ")
    for key, value in un_dicc.items():   # <-- Accediendo a los elementos de un diccionario
        print(f"{key:<15} : {value}")
    print()


class Main():
    def __init__(self) -> None:
        # Conectar a la BD aquí:
        self.midb = BD_MySQL('contactos_user','user1234', '127.0.0.1', 'info_db')
        Cls()

        # Validar conexión a la BD aquí
        if self.midb.conectar():
            print("conexion exitosa a la base de datos ")
            numContacotos = self.midb.consultarFunc("SELECT COUNT(*) FROM contactos;")
            msb.showinfo(APP_NAME, f"hay {numContacotos} contactos en la base de datos." )
        else:
            exit("no se logro una conexion exitosa a la bd.Fin del progrma.")

        mainWin = Tk()
        mainWin.title(APP_NAME)
        mainWin.geometry(geometryCentrado(mainWin, 700, 340))
        mainWin.resizable(width=False, height=False)        
        self.dg1 = DataGridSB(mainWin, x_=10, y_=10, width_=680, height_=284, background_="gray")
        self.dg1.crearColumnas(("nombre","teléfono","email"))
        
        self.dg1.anchoColumna("#0", width_=40, minwidth_=40, stretch_=tk.NO)
        self.dg1.anchoColumna("nombre", width_=200, minwidth_=40, stretch_=tk.NO)
        self.dg1.anchoColumna("teléfono", width_=200, minwidth_=40, stretch_=tk.NO)
        self.dg1.anchoColumna("email", width_=200, minwidth_=40, stretch_=tk.NO)

        self.dg1.encabezadoColumna("#0", "No.", 'w')
        self.dg1.encabezadoColumna("nombre", "Nombre", 'w')
        self.dg1.encabezadoColumna("teléfono", "Teléfono", 'w')
        self.dg1.encabezadoColumna("email", "Email", 'w')
        
        self.actualizarDataGrid()
        
        btnAgregar = ttk.Button(mainWin, text="Agregar", width=15, command=lambda: self.agregar(mainWin))
        pos_x = 70
        pos_y = 300
        btnAgregar.place(x=pos_x, y= pos_y)
        btnBuscar = ttk.Button(mainWin, text="Buscar", width=15, command=lambda: self.buscar(mainWin))
        pos_x += 150
        btnBuscar.place(x=pos_x, y= pos_y)
        btnEliminar = ttk.Button(mainWin, text="Eliminar", width=15, command=self.eliminar)
        pos_x += 150
        btnEliminar.place(x=pos_x, y= pos_y)      
        btnSalir = ttk.Button(mainWin, text="Salir", width=15, command=mainWin.destroy)
        pos_x += 150
        btnSalir.place(x=pos_x, y= pos_y)
        
        mainWin.focus_force() 
        mainWin.mainloop()


    def agregar(self, master_win):
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
        entry1 = ttk.Entry(winAgregar, textvariable=nombre_sv, width=25)
        entry1.place(x=80, y=10)       
        label2 = ttk.Label(winAgregar, text="Teléfono:")
        label2.place(x=10, y=40)
        entry2 = ttk.Entry(winAgregar, textvariable=telefono_sv, width=25)
        entry2.place(x=80, y=40)
        label3 = ttk.Label(winAgregar, text="email:")
        label3.place(x=10, y=70)
        entry3 = ttk.Entry(winAgregar, textvariable=email_sv, width=25)
        entry3.place(x=80, y=70)
        
        btnAceptar = Button(winAgregar, text="Aceptar", width=13, command=lambda: self._agregar_aprobado(winAgregar, nombre_sv, telefono_sv, email_sv))
        btnAceptar.place(x=30, y=110)
        btnCancelar = Button(winAgregar, text="Cancelar", width=13, command=winAgregar.destroy)
        btnCancelar.place(x=170, y=110)

        winAgregar.bind('<Return>', lambda e: self._agregar_aprobado(winAgregar, nombre_sv, telefono_sv, email_sv) )
        winAgregar.bind("<Escape>", lambda e: winAgregar.destroy())
        winAgregar.focus_force()
        entry1.focus()


    def _agregar_aprobado(self, master_win, nom_sv, tel_sev, em_sv):
        nombre = nom_sv.get().strip()
        teléfono = tel_sev.get().strip()
        email = em_sv.get().strip()
        # Validar nombre y teléfono del contacto aquí
        if nombre== "" or teléfono=="":
            msb.showerror("El contacto no se agrego", "El telefono y el nombre son obligatorios.")
        else:
            isql = f"Insert into contactos ( nombre, telefono, email) values ('{nombre}', '{teléfono}', '{email}');"
            if self.midb.ejecutar(isql):
                self.actualizarDataGrid()
                self._ubicar_contacto(nombre)
                msb.showinfo(APP_NAME, f"El contacto '{nombre}' ha sido agregado.")

        master_win.destroy()


    def actualizarDataGrid(self):
        for r in self.dg1.tvw1.get_children(): self.dg1.tvw1.delete(r)
        registros = self.midb.consultar("select * from contactos order by nombre;")
        n = 0
        for r in registros:
            n +=1
            self.dg1.agregarRenglon(n,n,(r[0], r[1], r[2]))

    def buscar(self, master_win):
        winBuscar = Toplevel(master_win)
        winBuscar.grab_set()
        winBuscar.title("Búsqueda")
        winBuscar.geometry(geometryCentrado(winBuscar, 300, 120))
        winBuscar.resizable(width=False, height=False)

        info_sv = StringVar(winBuscar)
        label1 = ttk.Label(winBuscar, text="Introduzca el nombre a buscar:")
        label1.place(x=10, y=10)
        entry1 = ttk.Entry(winBuscar, textvariable=info_sv, width=38)
        entry1.place(x=10, y=35)
        btnAceptar = ttk.Button(winBuscar, text="Aceptar", width=13, command=lambda: self._ubicar_contacto(info_sv.get()))
        btnAceptar.place(x=30, y=70)
        btnCancelar = ttk.Button(winBuscar, text="Cancelar", width=13, command=winBuscar.destroy)
        btnCancelar.place(x=165, y=70)

        winBuscar.bind('<Return>', lambda e: self._ubicar_contacto( info_sv.get() ) )
        winBuscar.bind("<Escape>", lambda e: winBuscar.destroy())
        winBuscar.focus_force()
        entry1.focus()


    def _ubicar_contacto(self, nom):
        nombre = nom.strip()
        encontrado = False
        if nombre != "":
            for parent in self.dg1.tvw1.get_children():
                if str(self.dg1.tvw1.item(parent)['values'][0]).__contains__(nombre) :
                    encontrado = True
                    self.dg1.seleccionaRenglonPorParent( parent )
                    break
            if not encontrado:
                msb.showerror("",f"El contacto '{nombre}' no se encuentra.") 


    def eliminar(self):
        for selected_item in self.dg1.tvw1.selection():
            item = self.dg1.tvw1.item(selected_item)
            record = item['values']
            respuesta = msb.askquestion("¿Desea eliminar el registro?", record)
            if respuesta == "yes":
                iSql = f"Delete from contactos where nombre = '{record[0]}';"
                if self.midb.ejecutar(iSql):
                    print("se ha borrado su contacto")


#-------------------------------------------------------
Main()