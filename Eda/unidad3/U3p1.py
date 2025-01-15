# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 22/10/2024

import numpy
from MisFunciones_2024 import *

Cls()

ps_arreglo = []

for i in range(10):
    ps_arreglo.append(leer_int(f"Dame el valor {i+1}: "))

print("El arreglo entrante es: ",ps_arreglo)
pausa("\nAhora te muestro los numeros en orden inverso:\n")

for e in reversed(ps_arreglo):
    print(e, end=", ", flush=True)

print()
pausa_final()