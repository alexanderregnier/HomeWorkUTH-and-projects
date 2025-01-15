#Sadrach Juan Diego Garcia Flores
#Fecha: 25/10/24
#grupo: 4-2

# 8. Un programa que inicialice una matriz con su diagonal principal en 1’s y el resto de los elementos con 0’s.
# La matriz debe tener el mismo número de renglones que de columnas. (El programa debe preguntar al usuario de que tamaño será la matriz):

import numpy as np
from MisFunciones_2024 import *

Cls()
while True:
    NF = int(input("Ingresa el tamaño de la matriz simetrica: "))
    if NF < 86:
        Matriz = np.empty((NF,NF), dtype=int)

        for f in range(NF):
            for c in range(NF):
                if f == c:
                    Matriz[f][c] = 1
                else:
                    Matriz[f][c] = 0

        for f in range(NF):
            for c in range(NF):
                print(f"{Matriz[f][c]:2}", end="")
            print()

        pausa("\nEl programa ah finalizado")
        Cls()
    else:
        print("El tamaño de la matriz debe ser menor a 86")
        continue