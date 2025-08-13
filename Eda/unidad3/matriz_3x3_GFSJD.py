#Sadrach Juan Diego Garcia Flores
#Fecha: 25/10/24
#grupo: 4-2

# 7.- Elaborar un programa que pida 9 números enteros y los vaya introduciendo en una matriz de 3x3. A continuación debe sumar cada una de las columnas y de los renglones. 
# Al final, imprimir la matriz con las sumas.

# 10  11  12 | 33
#  7   4  26 | 37
# 15   8   3 | 26
# ----------
# 32  23  41

import numpy as np
from MisFunciones_2024 import *
import secrets

Cls()

NF = 3 #Numero de Filas
NC = 3 #Numero de Columnas

# Arreglo = np.empty(8, dtype=int)
Matriz = np.empty((NF,NC), dtype=int)

for f in range(NF):
    for c in range(NC):
        # Matriz[f][c] = leer_int(f"Teclee un numero para [{f}][{c}]: ")
        # Matriz[f][c] = np.random.randint(1,100)
        Matriz[f][c] = secrets.SystemRandom().randint(1,100)

for f in range(NF):
    suma = 0
    for i in range(NC):
        print(f"{Matriz[f][c]:3}", end="")
        suma += Matriz[f][c]
    print(f" | {suma:3}")

print("—" * (NC+1)*3)
for c in range(NF):
    suma = 0
    for f in range(NC):
        suma += Matriz[f][c]
    print(f"{suma:3}", end=" ")

pausa("\nEl programa ah finalizado")
