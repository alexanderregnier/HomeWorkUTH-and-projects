#Sadrach Juan Diego Garcia Flores
#Fecha: 25/10/24
#grupo: 4-2

# 3.5.- Un programa que tome arreglo de n números y los imprima ordenados de menor a mayor.
# IMPORTANTE: Hacerlo con numpy, no con listas.

import numpy as np
from MisFunciones_2024 import *
import secrets

Cls()
n = secrets.SystemRandom().randint(1,100)

arreglo = np.random.randint(0, 100, n)

print("Arreglo:",*arreglo)
print("Arreglo ordenado:",*np.sort(arreglo))
