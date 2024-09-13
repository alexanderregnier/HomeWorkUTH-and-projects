'''
Archivo: mis_funciones.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 08-febrero-2024

Objetivo: Reunir algunas funciones de utilería de uso frecuente.
'''
import os
import winsound
from msvcrt import getch
from tkinter import Tk

# -------------------- Funciones --------------------
def Cls():
    ''' Limpiar la consola. '''
    if os.name == 'nt':
        os.system("CLS")        # Windows
    else:
        os.system("Clear")      # Linux


def BeepError():
    ''' Emite un sonido para indicar algo anormal en la ejecución. '''
    winsound.Beep(880,125)
    winsound.Beep(700,125)


def leer_entero(mensaje:str):
    ''' Entrada validada de un número entero. '''
    while True:
        try:
            return int(input(mensaje))
        except:
            BeepError()
            print("Error! Debe dar un número entero. Intente de nuevo.")


def leer_float(mensaje:str):
    ''' Entrada validada de un número con decimales. '''
    while True:
        try:
            return float(input(mensaje))
        except:
            BeepError()
            print("Error! Debe dar un número entero. Intente de nuevo.")


def pausa(mensaje:str=""):
    ''' Muestra un mensaje en la consola mientras hace una pausa esperando 
        por una tecla. Si mensaje no se proporciona, se imprime 
        "Presione una tecla para continuar." . '''
    if mensaje == "":  mensaje = "Presione una tecla para continuar."
    print(mensaje, end="", flush=True)
    return getch()


def geometryCentrado(tk_obj:Tk, ancho_ventana:int, alto_ventana:int):
    ancho_pantalla = tk_obj.winfo_screenwidth()
    alto_pantalla = tk_obj.winfo_screenheight()
    w_pos = int(ancho_pantalla/2 - ancho_ventana/2)
    h_pos = int(alto_pantalla/2 - alto_ventana/2)
    return f"{ancho_ventana}x{alto_ventana}+{w_pos}+{h_pos}"