'''
Archivo: utilerias.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 09-noviembre-2021

Objetivo: Proveer de funciones sencillas de uso recurrente para la programación con 
interfaz tkinter.
'''

def limpiar_consola():
    print("\033[2J", end="", flush=True)    # limpia la pantalla
    print("\033[1;1f", end="", flush=True)  # Mueve el cursos a la pos. 1,1 (esquina superior izquierda)
    print()
    
def geometryCentrado(tk_obj, ancho_ventana, alto_ventana):
    ancho_pantalla = tk_obj.winfo_screenwidth()
    alto_pantalla = tk_obj.winfo_screenheight()
    w_pos = int(ancho_pantalla/2 - ancho_ventana/2)
    h_pos = int(alto_pantalla/2 - alto_ventana/2)
    return f"{ancho_ventana}x{alto_ventana}+{w_pos}+{h_pos}"