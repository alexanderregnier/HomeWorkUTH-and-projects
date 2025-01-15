#Sadrach Juan Diego Garcia Flores
#Fecha: 08/11/24
#grupo: 4-2

import numpy as np
from MisFunciones_2024 import *

arreglo = np.empty(0, dtype=int)
Cls()
while True:
    NF = leer_int("Ingresa el tamaño de la matriz: ")
    if NF < 86:
        Matriz = np.empty((NF,NF), dtype=int)
        
        for f in range(NF):
            for c in range(NF):
                Matriz[f][c] = f + 1

        for f in range(NF):
            for c in range(NF):
                print(f"{Matriz[f][c]:2}", end="")
                arreglo = np.append(arreglo, Matriz[f][c])
            print()

        print("\nArreglo:", arreglo)
        pausa_final()
        break
