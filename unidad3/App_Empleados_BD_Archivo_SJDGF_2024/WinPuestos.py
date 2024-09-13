from mis_funciones import geometryCentrado
from cls_BD_MySQL import *
from cls_datagridSB import *
from tkinter import *
from tkinter import messagebox as msb
import globales as gb


TITLE_HERE = "Puestos "

class WinPuestos:
    def __init__(self, masterTk) -> None:
        puestosTk = Toplevel(masterTk)
        puestosTk.title(TITLE_HERE)
        puestosTk.geometry(geometryCentrado(puestosTk, 450, 340))
        puestosTk.resizable(False, False)
        puestosTk.grab_set()   # Deshabilita todas las otras ventanas hasta que esta ventana sea destruida.
        puestosTk.transient(masterTk)  # Indica que la ventana es de tipo transient, lo que significa que la ventana aparece al frente del padre.

        info_sv = StringVar()
        ttk.Label(puestosTk, text="Buscar:").place(x=10, y=10)
        entryBuscar = ttk.Entry(puestosTk, textvariable=info_sv, width=38)
        entryBuscar.place(x=70, y=10)
        btnBuscar1 = ttk.Button(puestosTk, text="🔎", state='select', width=4, command=lambda: self._ubicar( info_sv.get().strip() ))
        btnBuscar1.place(x=360, y=8)
        entryBuscar.bind('<Return>', lambda e: self._ubicar( info_sv.get().strip() ))
        
        self.datagrid = DataGridSB(puestosTk, 10, 40, 430, 250, "gray")
        self.datagrid.crearColumnas(("nombre_puesto"))

        stHeadings = ttk.Style()
        # stHeadings.theme_use("default")   # 'clam', 'alt', 'default', 'classic'
        stHeadings.configure("Treeview.Heading", font=("", 11, "bold"), background="#CCCCCC")
        
        self.datagrid.anchoColumna("#0", width_=40, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("nombre_puesto", width_=300, minwidth_=100, stretch_= False)
        self.datagrid.encabezadoColumna("#0", " #", 'w')
        self.datagrid.encabezadoColumna("nombre_puesto", "Nombre del Puesto", 'w')

        self.actualizarDataGrid()

        btnAgregar = ttk.Button(puestosTk, text="Agregar", width=10, command=lambda: self.agregar(puestosTk))
        pos_x = 20  ;  pos_y = 300
        btnAgregar.place(x=pos_x, y= pos_y)
        btnEditar = ttk.Button(puestosTk, text="Editar", width=10, command=lambda: self.editar(puestosTk))
        pos_x += 110
        btnEditar.place(x=pos_x, y= pos_y)     
        btnEliminar = ttk.Button(puestosTk, text="Eliminar", width=10, command=self.eliminar)
        pos_x += 110
        btnEliminar.place(x=pos_x, y= pos_y)      
        btnSalir = ttk.Button(puestosTk, text="Salir", width=10, command=puestosTk.destroy)
        pos_x += 110
        btnSalir.place(x=pos_x, y= pos_y)

        puestosTk.focus_force() 
        puestosTk.wait_window(puestosTk)

    def actualizarDataGrid(self):
        self.datagrid.vaciarDataGrid()
        registros = gb.LABD.consultar("Select * from puestos ORDER BY nombre_puestos;")
        n = 0
        for r in registros:
            n += 1
            if n%2 == 0:
                self.datagrid.agregarRenglon(n, n, r, "par")
            else:
                self.datagrid.agregarRenglon(n, n, r, "impar")

        self.datagrid.tvw1.tag_configure("impar", background="par")

    def agregar(self, master_win):
        winAgregar = Toplevel(master_win)
        winAgregar.grab_set()
        winAgregar.title("Agregar Puesto")
        winAgregar.geometry(geometryCentrado(winAgregar, 350, 120))
        winAgregar.resizable(width=False, height=False)
        
        nombre_puesto_sv = StringVar(winAgregar)

        label1 = ttk.Label(winAgregar, text="Nombre del puesto:")
        label1.place(x=10, y=10)
        entry1 = ttk.Entry(winAgregar, textvariable=nombre_puesto_sv, width=27)
        entry1.place(x=140, y=10)

        def agregar_aprobado():
            nombre_puesto = nombre_puesto_sv.get().strip()
            if nombre_puesto == "":
                msb.showwarning("El puesto no se agregó","El nombre del puesto es obligatorio.")
            else:
                iSql = f"INSERT INTO puestos (nombre_puesto) VALUES ('{nombre_puesto}'); "
                if gb.LABD.ejecutar(iSql):
                    self.actualizarDataGrid()
                    self._ubicar(nombre_puesto)
                    msb.showinfo(TITLE_HERE,f"El puesto '{nombre_puesto}' ha sido agregado.")
                winAgregar.destroy()

        btnAceptar = ttk.Button(winAgregar, text="Aceptar", width=13, command=agregar_aprobado)
        btnAceptar.place(x=50, y=70)
        btnCancelar = ttk.Button(winAgregar, text="Cancelar", width=13, command=winAgregar.destroy)
        btnCancelar.place(x=200, y=70)

        winAgregar.bind('<Return>', lambda e: agregar_aprobado())
        winAgregar.bind("<Escape>", lambda e: winAgregar.destroy())
        winAgregar.focus_force()
        entry1.focus()

    def _ubicar(self, nombre_:str):
        encontrado = False
        if nombre_ != "":
            for parent in self.datagrid.tvw1.get_children():
                if str(self.datagrid.tvw1.item(parent)['values'][0]).__contains__(nombre_) :
                    self.datagrid.seleccionaRenglonPorParent( parent )
                    encontrado = True
                    break
            if not encontrado:
                msb.showerror(TITLE_HERE,f"El puesto '{nombre_}' no se encuentra.")

    def eliminar(self):
        for selected_item in self.datagrid.tvw1.selection():
            item = self.datagrid.tvw1.item(selected_item)
            nombre_puesto = item['values'][0]
            respuesta = msb.askquestion("¿Desea eliminar el puesto?", nombre_puesto)
            if respuesta == "yes":
                iSql = f"DELETE FROM puestos WHERE nombre_puesto = '{nombre_puesto}';"
                if gb.LABD.ejecutar(iSql):
                    print("Se ha borrado el puesto:", nombre_puesto)
                    self.actualizarDataGrid()
                        
    def editar(self, master_win):
        for selected_item in self.datagrid.tvw1.selection():
            item = self.datagrid.tvw1.item(selected_item)
            nombre_puesto_pre = item['values'][0]

            winEditar = Toplevel(master_win)
            winEditar.grab_set()
            winEditar.title("Editar usuario")
            winEditar.geometry(geometryCentrado(winEditar, 350, 120))
            winEditar.resizable(width=False, height=False)
            
            nombre_puesto_sv = StringVar(winEditar)
            nombre_puesto_sv.set( item['values'][0] )

            label1 = ttk.Label(winEditar, text="Nombre del puesto:")
            label1.place(x=10, y=10)
            entry1 = ttk.Entry(winEditar, textvariable=nombre_puesto_sv, width=27)
            entry1.place(x=140, y=10)

            def editar_aprobado():
                nombre_puesto = nombre_puesto_sv.get().strip()
                if nombre_puesto == "":
                    msb.showwarning("El puesto no se modificó","El nombre del puesto es obligatorio.")
                else:
                    iSql = f"UPDATE puestos SET nombre_puesto='{nombre_puesto}' WHERE nombre_puesto='{nombre_puesto_pre}' ;"
                    if gb.LABD.ejecutar(iSql):
                        self.actualizarDataGrid()
                        self._ubicar(nombre_puesto)
                    winEditar.destroy()

            btnAceptar = ttk.Button(winEditar, text="Aceptar", width=13, command=editar_aprobado)
            btnAceptar.place(x=50, y=70)
            btnCancelar = ttk.Button(winEditar, text="Cancelar", width=13, command=winEditar.destroy)
            btnCancelar.place(x=200, y=70)

            winEditar.bind('<Return>', lambda e: editar_aprobado())
            winEditar.bind("<Escape>", lambda e: winEditar.destroy())
            winEditar.focus_force()
            entry1.focus()