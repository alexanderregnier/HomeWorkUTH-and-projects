'''
Archivo: cls_datagridSB.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 09-marzo-2022

Objetivo: Proporcionar una clase para gestionar un objeto TreeView en conjunto con 
un par de ScrollBars (derecha e inferior) que están agrupadas dentro de un Frame.
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DataGridSB():
    def __init__(self, master, _x:int, _y:int, _width, _height, _background) -> None:
        self.frame1 = tk.Frame(master, width=_width, height=_height, bg=_background)
        self.frame1.place(x=_x, y=_y, width=_width-20, height=_height)
        self.tvw1 = ttk.Treeview(self.frame1, selectmode ='browse', height=12)    # ← incorporamos también el TreeView como atributo:
        self.tvw1.place(x=0, y=0)
        vsb = ttk.Scrollbar(self.frame1, orient="vertical", command=self.tvw1.yview)
        vsb.place(x=_width-39, y=1, height=_height-2)
        self.tvw1.configure(yscrollcommand=vsb.set)
        # # self.tvw1.bind('<<TreeviewSelect>>', self.item_selected)  # ← Esta tal vez se ocupe más adelante
        hsb = ttk.Scrollbar(self.frame1, orient="horizontal", command=self.tvw1.xview)
        hsb.place(x=0, y=_height-17, width=_width-40)
        self.tvw1.configure(xscrollcommand=hsb.set)


    def crearColumnas(self, headers=[]):
        self.tvw1["columns"] = headers


    def anchoColumna(self, _column, _width, _minwidth, _stretch):
        self.tvw1.column(column=_column, width=_width, minwidth=_minwidth, stretch=_stretch)


    def encabezadoColumna(self, _column, _text, _anchor):
        self.tvw1.heading(column=_column, text=_text, anchor=_anchor)


    def agregarRenglon(self, _parent, _index, _text, _values):    
        self.tvw1.insert(parent=_parent, index=_index, text=_text, values=_values)


    # def ajustarAltura(self, num_renglones):
    #     # self.tvw1['height'] = num_renglones
    #     pass


    def item_selected(self, event):
        for selected_item in self.tvw1.selection():
            item = self.tvw1.item(selected_item)
            record = item['values']
            messagebox.showinfo(title='Information', message=record) #    ','.join(record))