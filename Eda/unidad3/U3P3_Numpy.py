import numpy as np
from MisFunciones_2024 import *
import random

Cls()
tamaño = leer_int("introduzca el tamaño del arrerglo")

if tamaño <= 0:
    beep_error()
    print(f"El arreglo no puede tener un tamaño de {tamaño}")
    quit()
minimo = leer_int("Introduza el minimo: ")
maximo = leer_int("Introduce el valor maximo:")

if maximo > minimo:
    # arreglo = np.empty(tamaño, dtype=int)
    # for i in range(tamaño):
    #     arreglo[i] = random.randint(minimo, maximo)
    # print("Arreglo:", arreglo)
    arreglo = np.random.randint(minimo, maximo+1, tamaño)
    print("Arreglo:", arreglo)
else:
    beep_error()
    print("Los valores de minimo y maximo no son adecuados.")

pausa_final()

