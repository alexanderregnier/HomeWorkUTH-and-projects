#Sadrach Juan Diego Garcia Flores
#Fecha: 25/10/24
#grupo: 4-2

# 3.4.- Un programa que diga cuál es el mayor y cuál es el menor de todos los elementos de un arreglo.
# IMPORTANTE: Hacerlo con numpy, no con listas.

import numpy as np
from MisFunciones_2024 import *

Cls()
N = int(input("INTRUCUCE EL ALOR"))
arreglo = np.random.randint(1, 100, N)

print("Arreglo:",*arreglo)

#Mean

print(f"El mayor es: {np.max(arreglo)}")
print(f"El menor es: {np.min(arreglo)}")