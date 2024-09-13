import cmath
import sympy as sp
import tkinter as tk
from mis_funciones import *
from tkinter import messagebox as msg
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Cls()#LIMPIAMOS PANTALLA
print("ADVERTENCIA: LEE TODO")
pausa()#Nos detenemos un momento para admirar el paisaje y despues sacarle su derivada
Cls()#LIMPIAMOS PANTALLA

def Calcular_3_terminos():#Cuadraticas
    print("Si no tiene X coloca potencia 0")

    Primero = float(input("Primer valor: "))
    PrimeroPote = float(input("Primera potencia: "))

    Segunda = float(input("Segundo valor: "))
    segundaPote = float(input("Segunda potencia: "))

    Tercera = float(input("tercer valor: "))
    TerceraPote = float(input("tercera potencia: "))

    Cls()#LIMPIAMOS PANTALLA

    #DERIVAR
    FormulaDer1 = Primero * PrimeroPote
    FormulaDer2 = Segunda * segundaPote
    FormulaDer3 = Tercera * TerceraPote

    #Despeje de X
    MINIMO1 = 0 - FormulaDer2
    MINIMO2 = MINIMO1/FormulaDer1
    print(f"Cordenada X:F'({MINIMO2})=0")

    #Cordeada de Y
    Cord_Y = Primero * MINIMO2**PrimeroPote + Segunda * MINIMO2**segundaPote + Tercera
    print(f"Cordenada Y:F'({Cord_Y})")

    # Verificar si es creciente o decreciente
    if Primero < 0:
        print("Es máximo")
        tipo_punto = "Máximo"
    elif Primero > 0:
        print("Es mínimo")
        tipo_punto = "Mínimo"
    else:
        print("No se puede determinar")
        tipo_punto = "Indeterminado"
    
    #FORMULA GENERAL
    Discriminante = FormulaDer2**2 - 4*FormulaDer1*FormulaDer3

    formulaGenMas = -FormulaDer2 + cmath.sqrt(Discriminante)/(2*FormulaDer1)
    formulaGenMen = -FormulaDer2 - cmath.sqrt(Discriminante)/(2*FormulaDer1)

    print(f'Derivadas:{FormulaDer1}X+{FormulaDer2}+{FormulaDer3}')
    print(f'Formula general +: {formulaGenMas} ')
    print(f'Formula general -: {formulaGenMen}')

    return Primero, Segunda, Tercera, MINIMO2, Cord_Y, tipo_punto

def Calcular_4_terminos():# 4 terminos no recuerdso el nombre
    Primero = float(input("Primer valor: "))
    PrimeroPote = 3

    Segunda = float(input("Segundo valor: "))
    segundaPote = 2

    Tercera = float(input("tercer valor: "))
    TerceraPote = 1

    Cuarto = float(input("Cuarto valor: "))
    CuartaPote = 0

    Cls()#LIMPIAMOS PANTALLA

    #DERIVAR
    FormulaDer1 = Primero * PrimeroPote
    FormulaDer2 = Segunda * segundaPote
    FormulaDer3 = Tercera * TerceraPote
    FormulaDer4 = Cuarto * CuartaPote

    #FORMULA GENERAL
    Discriminante = FormulaDer2**2 - 4*FormulaDer1*FormulaDer3

    formulaGenMas = (-FormulaDer2 + cmath.sqrt(Discriminante))/(2*FormulaDer1)#X1
    formulaGenMen = (-FormulaDer2 - cmath.sqrt(Discriminante))/(2*FormulaDer1)#X2

    if formulaGenMas.imag == 0:
        FraccionGenMas = Fraction(formulaGenMas.real)
        print(f"X1 como fracción: {FraccionGenMas}")
    else:
        print(f"X1 es un número complejo: {formulaGenMas}")

    if formulaGenMen.imag == 0:
        FraccionGenMen = Fraction(formulaGenMen.real)
        print(f"X2 como fracción: {FraccionGenMen}")
    else:
        print(f"X2 es un número complejo: {formulaGenMen}")

    print(f'Derivadas:{FormulaDer1}X^2+{FormulaDer2}X+{FormulaDer3}+{FormulaDer4}')
    print(f'Formula general +: {formulaGenMas}')
    print(f'Formula general -: {formulaGenMen}')

    return Primero, Segunda, Tercera, Cuarto

def graficar(Primero, Segunda, Tercera, Cuarto=None, MINIMO2=None, Cord_Y=None):#Gaficara dependiendo de la funcion
    if Cuarto is None:
        # Generar valores X para la función cuadrática
        x = np.linspace(MINIMO2 - 10, MINIMO2 + 10, 400)
        y = Primero * x**2 + Segunda * x + Tercera

        # Crear la figura
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x, y, label=f'{Primero}x^2 + {Segunda}x + {Tercera}')

        # Punto mínimo o máximo
        ax.scatter([MINIMO2], [Cord_Y], color='red')
        ax.text(MINIMO2, Cord_Y, f'({MINIMO2}, {Cord_Y})', fontsize=12, ha='right')

        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        ax.legend()
        ax.set_title('Gráfica de la función cuadrática')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        return fig
    else:
        # Generar valores X para la función cúbica
        x = np.linspace(-10, 10, 400)
        y = Primero * x**3 + Segunda * x**2 + Tercera * x + Cuarto
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f'{Primero}x^3 + {Segunda}x^2 + {Tercera}x + {Cuarto}')
        
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.title('Gráfica de la función cúbica')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

def mostrar_resultados(Primero, Segunda, Tercera, MINIMO2, Cord_Y, tipo_punto, Cuarto=None):#Muestra los resultados en pantalla junto a la grafica SE PIERDEN LOS CONTROLES DE LA GRAFICA
    root = tk.Tk()
    root.title("Resultados y Gráfica")

    # Mostrar resultados en la GUI
    result_frame = ttk.Frame(root, padding="10")
    result_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    ttk.Label(result_frame, text=f"Coeficiente Primero: {Primero}").grid(row=0, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Coeficiente Segunda: {Segunda}").grid(row=1, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Coeficiente Tercera: {Tercera}").grid(row=2, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Coordenada X del mínimo/máximo: {MINIMO2}").grid(row=3, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Coordenada Y del mínimo/máximo: {Cord_Y}").grid(row=4, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Tipo de punto: {tipo_punto}").grid(row=5, column=0, sticky=tk.W)

    # Graficar en la GUI
    if Cuarto is None:
        fig = graficar(Primero, Segunda, Tercera, MINIMO2=MINIMO2, Cord_Y=Cord_Y)
    else:
        fig = graficar(Primero, Segunda, Tercera, Cuarto=Cuarto, MINIMO2=MINIMO2, Cord_Y=Cord_Y)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    root.mainloop()

while True:#CReo el ciclo para que se repita el programa hasta que lo cierre :D
    opcion = input("¿Cuántos términos tiene? (3/4): ")

    if opcion == "3":
        Primero, Segunda, Tercera, MINIMO2, Cord_Y, tipo_punto = Calcular_3_terminos()
        mostrar_resultados(Primero, Segunda, Tercera, MINIMO2, Cord_Y, tipo_punto)
    elif opcion == "4":
        Primero, Segunda, Tercera, Cuarto = Calcular_4_terminos()
        mostrar_resultados(Primero, Segunda, Tercera, 0, 0, "", Cuarto)
    else:
        print("Opción no válida. Introduce '3' o '4'.")
    opcion = input("¿Cuántos términos tiene? (3/4): ")

    if opcion == "3":
        Primero, Segunda, Tercera, MINIMO2, Cord_Y, tipo_punto = Calcular_3_terminos()
        mostrar_resultados(Primero, Segunda, Tercera, MINIMO2, Cord_Y, tipo_punto)
    elif opcion == "4":
        Primero, Segunda, Tercera, Cuarto = Calcular_4_terminos()
        mostrar_resultados(Primero, Segunda, Tercera, 0, 0, Cuarto)
    else:
        print("Opción no válida. Introduce '3' o '4'.")

    # for i in range(20):# Itera desde 0 hasta 4
    #     Ciclo = V1 + V2
    #     Nuevo = (Ciclo / 2)  
    #     if i in range(20):
    #         print(f"Iteración {i + 1}: {Nuevo}")  