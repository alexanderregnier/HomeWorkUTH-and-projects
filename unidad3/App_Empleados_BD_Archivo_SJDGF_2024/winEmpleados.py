# Autor: Sadrach Juan Diego Garcia Flores
# Grupo: 2-2
# Fecha: 21/03/2024

from mis_funciones import geometryCentrado
from cls_BD_MySQL import *
from cls_datagridSB import *
from tkinter import *
from tkinter import messagebox as msb
from carta_Rec import crearPDFCartaRec
from tkcalendar import Calendar,DateEntry
import globales as gb

TITLE_HERE = "Empleados"

class WinEmpleados:
    def __init__(self, masterTk:Tk) -> None:
        empleadosTk = Toplevel(masterTk)
        empleadosTk.title(TITLE_HERE)
        empleadosTk.geometry(geometryCentrado(empleadosTk, 800, 340))
        empleadosTk.resizable(False, False)
        empleadosTk.grab_set()   # Deshabilita todas las otras ventanas hasta que esta ventana sea destruida.
        empleadosTk.transient(masterTk)  # Indica que la ventana es de tipo transient, lo que significa que la ventana aparece al frente del padre.

        info_sv = StringVar()
        ttk.Label(empleadosTk, text="Buscar por Apellido Paterno:").place(x=10, y=10)
        entryBuscar = ttk.Entry(empleadosTk, textvariable=info_sv, width=38)
        entryBuscar.place(x=188, y=10)
        btnBuscar1 = ttk.Button(empleadosTk, text="🔎", state='select', width=4, command=lambda: self._buscar_por_apellido( info_sv.get().strip() ))
        #btnBuscar1.place(x=470, y=8)
        entryBuscar.bind('<Return>', lambda e: self._buscar_por_apellido( info_sv.get().strip() ))
        
        self.datagrid = DataGridSB(empleadosTk, 10, 40, 780, 250, "gray")
        self.datagrid.crearColumnas(('id', 'nombre', 'apellido_pat', 'apellido_mat', 'correo', 'puesto', 'fecha_ingreso'))

        stHeadings = ttk.Style()
        # stHeadings.theme_use("clam")   # 'clam', 'alt', 'default', 'classic'
        stHeadings.configure("Treeview.Heading", font=("", 10, "bold"), background="#CCCCCC")
        
        self.datagrid.anchoColumna("#0", width_=1, minwidth_=1, stretch_=tk.NO)
        self.datagrid.anchoColumna("id", width_=40, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("nombre", width_=120, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("apellido_pat", width_=120, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("apellido_mat", width_=120, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("correo", width_=130, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("puesto", width_=120, minwidth_=40, stretch_=tk.NO)
        self.datagrid.anchoColumna("fecha_ingreso", width_=120, minwidth_=40, stretch_=tk.NO)

        self.datagrid.encabezadoColumna("#0", "No.", 'w')
        self.datagrid.encabezadoColumna("id", "Id", 'w')
        self.datagrid.encabezadoColumna("nombre", "Nombre", 'w')
        self.datagrid.encabezadoColumna("apellido_pat", "Apellido Paterno", 'w')
        self.datagrid.encabezadoColumna("apellido_mat", "Apellido Materno", 'w')
        self.datagrid.encabezadoColumna("correo", "Correo", 'w')
        self.datagrid.encabezadoColumna("puesto", "Puesto", 'w')
        self.datagrid.encabezadoColumna("fecha_ingreso", "Fecha de Ingreso", 'w')

        self.actualizarDataGrid()

        btnAgregar = ttk.Button(empleadosTk, text="Agregar", width=15, command=lambda: self.agregar(empleadosTk))
        # pos_x = 115  ;  pos_y = 300
        pos_x = 42  ;  pos_y = 300
        btnAgregar.place(x=pos_x, y= pos_y)
        btnEditar = ttk.Button(empleadosTk, text="Editar", width=15, command=lambda: self.editar(empleadosTk))
        pos_x += 150
        btnEditar.place(x=pos_x, y= pos_y)

        btnCarta = ttk.Button(empleadosTk, text="Carta Rec.", width=15, command= self.generarCartaRec)
        pos_x += 150
        btnCarta.place(x=pos_x, y= pos_y)

        btnEliminar = ttk.Button(empleadosTk, text="Eliminar", width=15, command=self.eliminar)
        pos_x += 150
        btnEliminar.place(x=pos_x, y= pos_y)      
        btnSalir = ttk.Button(empleadosTk, text="Salir", width=15, command=empleadosTk.destroy)
        pos_x += 150
        btnSalir.place(x=pos_x, y= pos_y)

        empleadosTk.focus_force() 
        empleadosTk.wait_window(empleadosTk)
    def actualizarDataGrid(self):
        self.datagrid.vaciarDataGrid()
        registros = gb.LABD.consultar("SELECT * FROM empleados ORDER BY apellido_pat;")
        n = 0
        for r in registros:
            n += 1
            if n%2 == 0:
                self.datagrid.agregarRenglon(n, n, r, "par")
            else:
                self.datagrid.agregarRenglon(n, n, r, "impar")
        self.datagrid.tvw1.tag_configure("impar", background="lightgray")

    def generarCartaRec(self):
        for selected_item in self.datagrid.tvw1.selection():
            row = self.datagrid.tvw1.item(selected_item)['values']
            nombre = f"{row[1]} {row[2]} {row[3]}"
            puesto = row[5]
            fecha = row[6]
            crearPDFCartaRec(nombre, fecha, puesto)
            #msb.showinfo(TITLE_HERE, f"Imprimiendo Carta de Recomendación de {row}.")

    def eliminar(self):
        for selected_item in self.datagrid.tvw1.selection():
            item = self.datagrid.tvw1.item(selected_item)
            id = item['values'][0]
            empleado = item['values'][1] + " " + item['values'][2] + " " + item['values'][3]
            respuesta = msb.askquestion(gb.APP_NAME,f"¿Desea eliminar al empleado? \n\n{empleado} ")
            if respuesta == "yes":
                iSql = f"DELETE FROM empleados WHERE id = {id} ;"
                if gb.LABD.ejecutar(iSql):
                    print("Se ha borrado el empleado:", empleado)
                    self.actualizarDataGrid()
    
    def agregar(self, master_win):
        def agregar_aprobado():
            nombre = nombre_sv.get().strip()
            apellido_pat = apellido_pat_sv.get().strip()
            apellido_mat = apellido_mat_sv.get().strip()
            correo = correo_sv.get().strip()
            puesto = puesto_sv.get().strip()
            fecha_ingreso = dateEntry1.get()

            if nombre == "" or apellido_pat == "" or puesto == "":
                msb.showwarning("El empleado no se agregó","El nombre, el apellido paterno y el puesto son obligatorios.")
            else:
                query = (
                    f"INSERT INTO empleados VALUES "
                    f"(NULL, '{nombre}', '{apellido_pat}', '{apellido_mat}', '{correo}', '{puesto}', '{fecha_ingreso}');"
                )
                if gb.LABD.ejecutar(query):
                    self.actualizarDataGrid()
                    for parent in self.datagrid.tvw1.get_children():
                        if str(self.datagrid.tvw1.item(parent)['values'][1]).__contains__(nombre) and \
                            str(self.datagrid.tvw1.item(parent)['values'][2]).__contains__(apellido_pat) :
                            self.datagrid.seleccionaRenglonPorParent( parent )
                            break
                    msb.showinfo(TITLE_HERE,f"El empleado '{nombre} {apellido_pat}' ha sido agregado.")
                winAgregar.destroy()
                
        winAgregar = Toplevel(master_win)
        winAgregar.grab_set()
        winAgregar.title("Agregar empleado")
        winAgregar.geometry(geometryCentrado(winAgregar, 360, 260))
        winAgregar.resizable(width=False, height=False)
        
        nombre_sv = StringVar(winAgregar)
        apellido_pat_sv = StringVar(winAgregar)
        apellido_mat_sv = StringVar(winAgregar)
        correo_sv = StringVar(winAgregar)
        puesto_sv = StringVar(winAgregar)

        pos_y = 10
        label1 = ttk.Label(winAgregar, text="Nombre:")
        label1.place(x=10, y=pos_y)
        entry1 = ttk.Entry(winAgregar, textvariable=nombre_sv, width=25)
        entry1.place(x=130, y=pos_y)

        pos_y += 30
        label2 = ttk.Label(winAgregar, text="Apellido Paterno:")
        label2.place(x=10, y=pos_y)
        entry2 = ttk.Entry(winAgregar, textvariable=apellido_pat_sv, width=25)
        entry2.place(x=130, y=pos_y)

        pos_y += 30
        label3 = ttk.Label(winAgregar, text="Apellido Materno:")
        label3.place(x=10, y=pos_y)
        entry3 = ttk.Entry(winAgregar, textvariable=apellido_mat_sv, width=25)
        entry3.place(x=130, y=pos_y)

        pos_y += 30
        label4 = ttk.Label(winAgregar, text="Correo:")
        label4.place(x=10, y=pos_y)
        entry4 = ttk.Entry(winAgregar, textvariable=correo_sv, width=30)
        entry4.place(x=130, y=pos_y)

        pos_y += 30
        label5 = ttk.Label(winAgregar, text="Puesto:")
        label5.place(x=10, y=pos_y)
        cbo1 = ttk.Combobox(winAgregar, textvariable=puesto_sv, width=28)
        lista_de_puestos = []
        for reg in gb.LABD.consultar("SELECT nombre_puesto FROM puestos ORDER BY nombre_puesto;"):
            lista_de_puestos.append(reg[0])
        cbo1['value'] = lista_de_puestos
        cbo1.place(x=130, y=pos_y)

        pos_y += 30
        label6 = ttk.Label(winAgregar, text="Fecha de Ingreso:")
        label6.place(x=10, y=pos_y)
        dateEntry1 = DateEntry(winAgregar, width=15, justify='center', selectmode='day', locale='es_MX', date_pattern="Y-mm-dd", background="gray")
        dateEntry1.place(x=130, y=pos_y)

        btnAceptar = ttk.Button(winAgregar, text="Aceptar", width=13, command=agregar_aprobado)
        btnAceptar.place(x=60, y=210)
        btnCancelar = ttk.Button(winAgregar, text="Cancelar", width=13, command=winAgregar.destroy)
        btnCancelar.place(x=200, y=210)

        winAgregar.bind('<Return>', lambda e: agregar_aprobado())
        winAgregar.bind("<Escape>", lambda e: winAgregar.destroy())
        winAgregar.focus_force()
        entry1.focus()

    def _buscar_por_apellido(self, apellido_pat_:str):
        encontrado = False
        if apellido_pat_ != "":
            for parent in self.datagrid.tvw1.get_children():
                if str(self.datagrid.tvw1.item(parent)['values'][2]).__contains__(apellido_pat_) :
                    self.datagrid.seleccionaRenglonPorParent( parent )
                    encontrado = True
                    break
            if not encontrado:
                msb.showerror(TITLE_HERE,f"El empleado '{apellido_pat_}' no se encuentra.")

    def editar(self, master_win):
        def editar_aprobado():
            nombre = nombre_sv.get().strip()
            apellido_pat = apellido_pat_sv.get().strip()
            apellido_mat = apellido_mat_sv.get().strip()
            correo = correo_sv.get().strip()
            puesto = puesto_sv.get().strip()
            fecha_ingreso = dateEntry1.get()

            if nombre == "" or apellido_pat == "":
                msb.showwarning("El empleado no se agregó","El nombre y el apellido paterno son obligatorios.")
            else:
                query = (
                    f"UPDATE empleados "
                    f"SET nombre='{nombre}', apellido_pat='{apellido_pat}', "
                    f"apellido_mat='{apellido_mat}', correo='{correo}', "
                    f"puesto='{puesto}', fecha_ingreso='{fecha_ingreso}' "
                    f" WHERE id='{ID_pre}' ;"  
                )
                if gb.LABD.ejecutar(query):
                    self.actualizarDataGrid()
                    self._buscar_por_ID(ID_pre)
                winEditar.destroy()

        for selected_item in self.datagrid.tvw1.selection():
            winEditar = Toplevel(master_win)
            winEditar.grab_set()
            winEditar.title("Editar usuario")
            winEditar.geometry(geometryCentrado(winEditar, 360, 260))
            winEditar.resizable(False, False)

            item = self.datagrid.tvw1.item(selected_item)
            # print(item['values'][6])
            ID_pre = item['values'][0]
            nombre_sv = StringVar(winEditar)        ;  nombre_sv.set( item['values'][1] )
            apellido_pat_sv = StringVar(winEditar)  ;  apellido_pat_sv.set( item['values'][2] )
            apellido_mat_sv = StringVar(winEditar)  ;  apellido_mat_sv.set( item['values'][3] )            
            correo_sv = StringVar(winEditar)        ;  correo_sv.set( item['values'][4] ) 
            puesto_sv = StringVar(winEditar)        ;  puesto_sv.set( item['values'][5] ) 
            # fecha_ingreso_sv = StringVar(winEditar) 
            
            pos_y = 10
            label1 = ttk.Label(winEditar, text="Nombre:")
            label1.place(x=10, y=pos_y)
            entry1 = ttk.Entry(winEditar, textvariable=nombre_sv, width=25)
            entry1.place(x=130, y=pos_y)
            pos_y += 30
            label2 = ttk.Label(winEditar, text="Apellido Paterno:")
            label2.place(x=10, y=pos_y)
            entry2 = ttk.Entry(winEditar, textvariable=apellido_pat_sv, width=25)
            entry2.place(x=130, y=pos_y)
            pos_y += 30
            label3 = ttk.Label(winEditar, text="Apellido Materno:")
            label3.place(x=10, y=pos_y)
            entry3 = ttk.Entry(winEditar, textvariable=apellido_mat_sv, width=25)
            entry3.place(x=130, y=pos_y)
            pos_y += 30
            label4 = ttk.Label(winEditar, text="Correo:")
            label4.place(x=10, y=pos_y)
            entry4 = ttk.Entry(winEditar, textvariable=correo_sv, width=30)
            entry4.place(x=130, y=pos_y)
            pos_y += 30
            label5 = ttk.Label(winEditar, text="Puesto:")
            label5.place(x=10, y=pos_y)

            cbo1 = ttk.Combobox(winEditar, textvariable=puesto_sv, width=28)
            lista_de_puestos = []
            for reg in gb.LABD.consultar("SELECT nombre_puesto FROM puestos ORDER BY nombre_puesto;"):
                lista_de_puestos.append(reg[0])
            cbo1['value'] = lista_de_puestos
            cbo1.place(x=130, y=pos_y)

            pos_y += 30
            label6 = ttk.Label(winEditar, text="Fecha de Ingreso:")
            label6.place(x=10, y=pos_y)
            dateEntry1 = DateEntry(winEditar, width=15, justify='center', 
                selectmode='day', locale='es_MX', date_pattern="Y-mm-dd", background="gray")
            dateEntry1.place(x=130, y=pos_y)
            # dateEntry1.set_date( item['values'][6] )

            btnAceptar = ttk.Button(winEditar, text="Aceptar", width=13, command=editar_aprobado)
            btnAceptar.place(x=60, y=210)
            btnCancelar = ttk.Button(winEditar, text="Cancelar", width=13, command=winEditar.destroy)
            btnCancelar.place(x=200, y=210)

            winEditar.bind('<Return>', lambda e: editar_aprobado())
            winEditar.bind("<Escape>", lambda e: winEditar.destroy())
            winEditar.focus_force()
            entry1.focus()


    def _buscar_por_ID(self, ID_):
        encontrado = False
        if ID_ != "":
            for parent in self.datagrid.tvw1.get_children():
                if self.datagrid.tvw1.item(parent)['values'][0] == ID_ :
                    self.datagrid.seleccionaRenglonPorParent( parent )
                    encontrado = True
                    break
            if not encontrado:
                msb.showerror(TITLE_HERE,f"El empleado no se encuentra.")