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

Cls() # LIMPIAMOS PANTALLA
print("ADVERTENCIA: LEE TODO")
pausa() # Nos detenemos un momento para admirar el paisaje y despues sacarle su derivada ñaca ñaca
Cls() # LIMPIAMOS PANTALLA

def calcular():
    # Solicitar la cantidad de términos
    n = int(input("¿Cuántos términos tiene?: "))

    # Obtener los coeficientes y potencias
    terminos = []
    for i in range(n):
        coeficiente = float(input(f"Introduce el coeficiente del término {i+1}: "))
        potencia = float(input(f"Introduce la potencia del término {i+1}: "))
        terminos.append((coeficiente, potencia))

    # Derivar cada término
    derivada = [(coef * pot, pot - 1) for coef, pot in terminos if pot != 0]

    # Mostrar la derivada
    derivada_str = " + ".join([f"{coef}X^{pot}" for coef, pot in derivada])
    print(f"Derivada: F'(X) = {derivada_str}")

    # Despeje de X para encontrar puntos críticos
    if len(derivada) > 1:
        a, b = derivada[0][0], derivada[1][0] #Se eblista en tupals (((EXPLICACIONES)))
        x_critico = -b / a
        print(f"Coordenada X: F'({x_critico})=0")

        # Coordenada Y
        y_critico = sum(coef * (x_critico ** pot) for coef, pot in terminos)
        print(f"Coordenada Y: F({x_critico}) = {y_critico}")

        # Verificar si es máximo o mínimo
        if a < 0:
            print("Es un máximo.")
            tipo_punto = "Máximo"
        elif a > 0:
            print("Es un mínimo.")
            tipo_punto = "Mínimo"
        else:
            print("No se puede determinar.")
            tipo_punto = "Indeterminado"

        # Formula General (Discriminante)
        if len(derivada) > 2:
            c = derivada[2][0]
            discriminante = b**2 - 4*a*c
            formula_gen_mas = (-b + cmath.sqrt(discriminante)) / (2*a)
            formula_gen_men = (-b - cmath.sqrt(discriminante)) / (2*a)

            print(f'Fórmula general +: {formula_gen_mas} ')
            print(f'Fórmula general -: {formula_gen_men}')
        else:
            print("No se puede aplicar la fórmula general con los términos dados.")
    else:
        print("La derivada no es suficiente para determinar puntos críticos.")

    return terminos, derivada_str, x_critico, y_critico, tipo_punto

def graficar(terminos, x_critico=None, y_critico=None):
    max_potencia = max(pot for coef, pot in terminos)
    x = np.linspace(x_critico - 10, x_critico + 10, 400) if x_critico is not None else np.linspace(-10, 10, 400)
    y = sum(coef * x**pot for coef, pot in terminos)

    fig, ax = plt.subplots(figsize=(10, 6))
    formula_str = " + ".join([f"{coef}x^{pot}" for coef, pot in terminos])
    ax.plot(x, y, label=formula_str)

    if x_critico is not None and y_critico is not None:
        ax.scatter([x_critico], [y_critico], color='red')
        ax.text(x_critico, y_critico, f'({x_critico}, {y_critico})', fontsize=12, ha='right')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_title(f'Gráfica de la función de grado {max_potencia}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    return fig, x, y

def mostrar_resultados(terminos, derivada_str, x_critico, y_critico, tipo_punto):
    root = tk.Tk()
    root.title("Resultados y Gráfica")

    # Frame para los resultados
    result_frame = ttk.Frame(root, padding="10")
    result_frame.grid(row=0, column=0, sticky=(tk.N, tk.S))

    ttk.Label(result_frame, text=f"Derivada: {derivada_str}").grid(row=0, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Coordenada X del mínimo/máximo: {x_critico}").grid(row=1, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Coordenada Y del mínimo/máximo: {y_critico}").grid(row=2, column=0, sticky=tk.W)
    ttk.Label(result_frame, text=f"Tipo de punto: {tipo_punto}").grid(row=3, column=0, sticky=tk.W)

    # Frame para la gráfica
    graph_frame = ttk.Frame(root, padding="10")
    graph_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

    fig, x, y = graficar(terminos, x_critico=x_critico, y_critico=y_critico)
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Frame para la tabla de coordenadas
    table_frame = ttk.Frame(root, padding="10")
    table_frame.grid(row=0, column=2, sticky=(tk.N, tk.S))

    tree = ttk.Treeview(table_frame, columns=("X", "Y"), show="headings", height=15)
    tree.heading("X", text="X")
    tree.heading("Y", text="Y")
    tree.pack()

    for xi, yi in zip(x, y):
        tree.insert("", tk.END, values=(round(xi, 2), round(yi, 2)))

    root.mainloop()

while True:#CReo el ciclo para que se repita el programa hasta que lo cierre :D pd:dejo de funcionar y no se porque chales asi lo dejo mejor me da flojera
    opcion = input("Empezamos? (s/n) ")

    if opcion == "s":
        terminos, derivada_str, x_critico, y_critico, tipo_punto = calcular()
        mostrar_resultados(terminos, derivada_str, x_critico, y_critico, tipo_punto)
    elif opcion == "n":
        print("ok")
        exit
    else:
        opcion
