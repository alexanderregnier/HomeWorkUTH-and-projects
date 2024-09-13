from mis_funciones import geometryCentrado
from cls_BD_MySQL import *
from tkinter import *
from cls_datagridSB import *
from tkinter import messagebox as msb
from winEmpleados import WinEmpleados
import globales as gb

TITLE_HERE = "Usuarios"

class WinUsuarios:
    def __init__(self, masterTk:Tk) -> None:
        UsuariosTk= Toplevel(masterTk)
        UsuariosTk.title(TITLE_HERE)
        UsuariosTk.geometry(geometryCentrado(UsuariosTk,700,340))
        UsuariosTk.resizable(False,False)
        UsuariosTk.grab_set()   # Deshabilita todas las otras ventanas hasta que esta ventana sea destruida.
        UsuariosTk.transient(masterTk)  # Indica que la ventana es de tipo transient, lo que significa que la ventana aparece al frente del padre.

        info_sv= StringVar()
        info_sv = StringVar()
        ttk.Label(UsuariosTk, text="Buscar:").place(x=10, y=10)
        entryBuscar = ttk.Entry(UsuariosTk, textvariable=info_sv, width=38)
        entryBuscar.place(x=70, y=10)
        btnBuscar1 = ttk.Button(UsuariosTk, text="🔎", state='select', width=4, command=lambda: self._ubicar(info_sv.get().strip()))
        btnBuscar1.place(x=360, y=8)
        entryBuscar.bind('<Return>', lambda e: self._ubicar(info_sv.get().strip()))

        self.datagrid = DataGridSB(UsuariosTk, 10, 40, 680, 250, "gray")
        self.datagrid.crearColumnas(("nombre","password","correo"))

        stHeadings = ttk.Style()
        # stHeadings.theme_use("clam")   # 'clam', 'alt', 'default', 'classic'
        stHeadings.configure("Treeview.Heading", font=("", 11, "bold"), background="#CCCCCC")
        
        self.datagrid.anchoColumna("#0", width_=40, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("nombre", width_=140, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("password", width_=250, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("correo", width_=200, minwidth_=40, stretch_=tk.NO)

        self.datagrid.encabezadoColumna("#0", "No.", 'w')
        self.datagrid.encabezadoColumna("nombre", "Nombre", 'w')
        self.datagrid.encabezadoColumna("password", "Password", 'w')
        self.datagrid.encabezadoColumna("correo", "Correo", 'w')

        self.actualizarDataGrid()

        btnAgregar = ttk.Button(UsuariosTk, text="Agregar", width=15, command=lambda: self.agregar(UsuariosTk))
        pos_x = 70  ;  pos_y = 300
        btnAgregar.place(x=pos_x, y= pos_y)
        btnEditar = ttk.Button(UsuariosTk, text="Editar", width=15, command=lambda: self.editar(UsuariosTk))
        pos_x += 150
        btnEditar.place(x=pos_x, y= pos_y)     
        btnEliminar = ttk.Button(UsuariosTk, text="Eliminar", width=15, command= self.eliminar)
        pos_x += 150
        btnEliminar.place(x=pos_x, y= pos_y)      
        btnSalir = ttk.Button(UsuariosTk, text="Salir", width=15, command=UsuariosTk.destroy)
        pos_x += 150
        btnSalir.place(x=pos_x, y= pos_y)

        UsuariosTk.focus_force()
        UsuariosTk.wait_window(UsuariosTk)

    def agregar(self, master_win):
        winAgregar = Toplevel(master_win)
        winAgregar.grab_set()
        winAgregar.title("Agregar usuario")
        winAgregar.geometry(geometryCentrado(winAgregar, 300, 160))
        winAgregar.resizable(width=False, height=False)
        
        nombre_sv = StringVar(winAgregar)
        password_sv = StringVar(winAgregar)
        correo_sv = StringVar(winAgregar)

        label1 = ttk.Label(winAgregar, text="Nombre:")
        label1.place(x=10, y=10)
        entry1 = ttk.Entry(winAgregar, textvariable=nombre_sv, width=25)
        entry1.place(x=80, y=10)       
        label2 = ttk.Label(winAgregar, text="Password:")
        label2.place(x=10, y=40)
        entry2 = ttk.Entry(winAgregar, textvariable=password_sv, width=25)
        entry2.place(x=80, y=40)
        label3 = ttk.Label(winAgregar, text="Correo:")
        label3.place(x=10, y=70)
        entry3 = ttk.Entry(winAgregar, textvariable=correo_sv, width=25)
        entry3.place(x=80, y=70)

        def agregar_aprobado():
            nombre = nombre_sv.get().strip()
            password = password_sv.get().strip()
            correo = correo_sv.get().strip()
            if nombre == "" or password == "":
                msb.showwarning("El usuario nos se agrego", "el nombre y el password son obligatiorios")
            else:
                query = f"INSERT INTO usuarios (nombre, password, correo) values('{nombre}',MD5('{password}'), '{correo}');"
                # query = f"INSERT INTO usuarios values('{nombre}',MD5('{password}'), '{correo}');"
                if gb.LABD.ejecutar(query):
                    self.actualizarDataGrid()
                    self._ubicar(nombre)
                    msb.showinfo(TITLE_HERE, f"el usuario '{nombre}' ha sido creado.")
                winAgregar.destroy()

        btnAceptar = ttk.Button(winAgregar, text="Aceptar", width=13, command= agregar_aprobado)
        btnAceptar.place(x=30, y=110)
        btnCancelar = ttk.Button(winAgregar, text="Cancelar", width=13, command=winAgregar.destroy)
        btnCancelar.place(x=170, y=110)

        winAgregar.bind('<Return>', lambda e: agregar_aprobado())
        winAgregar.bind("<Escape>", lambda e: winAgregar.destroy())
        winAgregar.focus_force()
        entry1.focus()

    def actualizarDataGrid(self):
        self.datagrid.vaciarDataGrid()
        registros = gb.LABD.consultar("SELECT * FROM labd.usuarios ORDER BY nombre;") 
        n = 0 
        for r in registros:
            n += 1
            if n%2 == 0:
                self.datagrid.agregarRenglon(n,n,r, "par")
            else:
                self.datagrid.agregarRenglon(n,n,r, "Impar")

        # for p in self.datagrid.tvw1.get_children():  print(self.datagrid.tvw1.item(p))
        # self.datagrid.tvw1.tag_configure("par", background="white")
        self.datagrid.tvw1.tag_configure("impar", background="lightgray")

    def _ubicar(self, nombre_:str):
        encontrado = False
        if nombre_ != "":
            for parent in self.datagrid.tvw1.get_children():
                if str(self.datagrid.tvw1.item(parent)['values'][0]).__contains__(nombre_):
                    self.datagrid.seleccionaRenglonPorParent( parent )
                    encontrado = True
                    break
            if not encontrado:
                msb.showerror(TITLE_HERE,f"El usuario '{nombre_}' no se ah encontrado.")

    def eliminar(self):
        for selected_item in self.datagrid.tvw1.selection():
            item = self.datagrid.tvw1.item(selected_item)
            nombre = item['values'][0]
            respuesta = msb.askquestion("¿Deseas eliminar el usuario?",nombre)
            if respuesta == "yes":
                query = f"DELETE FROM usuarios WHERE nombre='{nombre}';"
                if gb.LABD.ejecutar(query):
                    print("se ah borrado el usuario:",nombre)
                    self.actualizarDataGrid()


    def editar(self, master_win):
        for selected_item in self.datagrid.tvw1.selection():
            item = self.datagrid.tvw1.item(selected_item)
            nombre_pre = item['values'][0]
            password_pre = item['values'][1]
            correo_pre = item['values'][2]

            winEditar = Toplevel(master_win)
            winEditar.grab_set()
            winEditar.title("Editar usuario")
            winEditar.geometry(geometryCentrado(winEditar, 300, 160))
            winEditar.resizable(width=False, height=False)

            nombre_sv = StringVar(winEditar)    ;    nombre_sv.set(nombre_pre)
            password_sv = StringVar(winEditar)
            correo_sv = StringVar(winEditar)    ;    correo_sv.set(correo_sv)

            label1 = ttk.Label(winEditar, text="Nombre:")
            label1.place(x=10, y=10)
            entry1 = ttk.Entry(winEditar, textvariable=nombre_sv, width=25)
            entry1.place(x=80, y=10)       
            label2 = ttk.Label(winEditar, text="Password:")
            label2.place(x=10, y=40)
            entry2 = ttk.Entry(winEditar, textvariable=password_sv, width=25)
            entry2.place(x=80, y=40)
            label3 = ttk.Label(winEditar, text="Correo:")
            label3.place(x=10, y=70)
            entry3 = ttk.Entry(winEditar, textvariable=correo_sv, width=25)
            entry3.place(x=80, y=70)

            def editar_aprobado():
                nombre = nombre_sv.get().strip()
                password = password_sv.get().strip()
                correo = correo_sv.get().strip()
                if nombre == "" or password == "":
                    msb.showwarning("El usuario no se modificó", "El nombre y el password son obligatorios.")
                else:
                    query = f"UPDATE usuarios SET nombre='{nombre}', password=MD5('{password}'), correo='{correo}' WHERE nombre='{nombre_pre}';"
                    if gb.LABD.ejecutar(query):
                        self.actualizarDataGrid()
                        self._ubicar(nombre)
                    winEditar.destroy()

            btnAceptar = ttk.Button(winEditar, text="Aceptar", width=13, command=editar_aprobado)
            btnAceptar.place(x=30, y=110)
            btnCancelar = ttk.Button(winEditar, text="Cancelar", width=13, command=winEditar.destroy)
            btnCancelar.place(x=170, y=110)

            # winEditar.bind('<Return>', lambda e: )
            winEditar.bind("<Escape>", lambda e: winEditar.destroy())
            winEditar.focus_force()
            entry1.focus()