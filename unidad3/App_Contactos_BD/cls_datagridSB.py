'''
Archivo: cls_datagridSB.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 29-Febrero-2024

Objetivo: 
La clase DataGridSB se provee con el fin de emula el desempeño del widget DataGridView  que existe 
en Visual C# .NET. 

Debido a que tkinter no cuenta con un widget tal como lo es el DGV, se proporciona esta clase 
para gestionar un objeto TreeView en conjunto con un par de ScrollBars (derecha e inferior) 
que están agrupadas dentro de un Frame.
'''
import tkinter as tk
from tkinter import ttk

class DataGridSB():
    def __init__(self, master, x_:int, y_:int, width_, height_, background_) -> None:
        self.frame1 = tk.Frame(master, width=width_, height=height_, bg=background_)
        self.frame1.place(x=x_, y=y_, width=width_, height=height_)
        reglones_del_dg = int((height_-19)/21.9)
        print("Renglones del DataGridSB:", reglones_del_dg)
        self.tvw1 = ttk.Treeview( self.frame1, selectmode ='browse', height=reglones_del_dg)
        # Incorporamos también ↑↑ el TreeView como atributo de la clase DataGridSB
        self.tvw1.place(x=0, y=0)
        self.vsb = ttk.Scrollbar(self.frame1, orient="vertical", command=self.tvw1.yview)
        self.vsb.place(x=width_-19, y=1, height=height_-19)
        self.tvw1.configure(yscrollcommand=self.vsb.set)
        # self.tvw1.bind('<<TreeviewSelect>>', self.item_selected)  # ← Esta tal vez se ocupe más adelante
        self.hsb = ttk.Scrollbar(self.frame1, orient="horizontal", command=self.tvw1.xview)
        self.hsb.place(x=1, y=height_-18, width=width_-21)
        self.tvw1.configure(xscrollcommand=self.hsb.set)


    def crearColumnas(self, headers=[]):
        self.tvw1["columns"] = headers


    def anchoColumna(self, column_, width_, minwidth_, stretch_):
        self.tvw1.column(column=column_, width=width_, minwidth=minwidth_, stretch=stretch_)


    def encabezadoColumna(self, column_, text_, anchor_):
        self.tvw1.heading(column=column_, text=text_, anchor=anchor_)


    # def agregarRenglon(self, parent_, index_, text_, values_):    
    def agregarRenglon(self, index_, text_, values_):    
        self.tvw1.insert(parent="", index=index_, text=text_, values=values_)


    def muestraElUltimo(self):
        self.tvw1.yview_moveto(1)
        self.tvw1.selection_set( self.tvw1.get_children()[-1])


    def seleccionaRenglonPorNum(self, num_row:int):
        ''' Ubica el renglón número 'num_row' en el DataGrid y lo resalta. '''
        print("Seleccionando contacto No.:", num_row)
        self.tvw1.selection_set( self.tvw1.get_children()[num_row-1] )
        self.tvw1.yview_moveto( (num_row-1) / len(self.tvw1.get_children() ) )
        # Hay que restar 1 a num_row ↑ porque las posiciones en las listas son de 0 al total_de_elementos - 1

    def seleccionaRenglonPorParent(self, parent):
        ''' Ubica el renglón por el 'parent' en el DataGrid y lo resalta. '''
        self.seleccionaRenglonPorNum( int( self.tvw1.item(parent)["text"] ) )