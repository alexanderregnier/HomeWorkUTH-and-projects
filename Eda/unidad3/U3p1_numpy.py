# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 22/10/2024

import numpy as np
from MisFunciones_2024 import *

Cls()

arreglo = np.empty(10, dtype=int)
for i in range(10):
    arreglo[i] = leer_int(f"Dame el valor {i+1}: ")

print("El arreglo entrante es: ",arreglo)
pausa("\nAhora te muestro los numeros en orden inverso:\n")

for e in reversed(arreglo):
    print(e, end=", ", flush=True)

print()
pausa_final()