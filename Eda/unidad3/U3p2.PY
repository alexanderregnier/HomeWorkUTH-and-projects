# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 22/10/2024

import numpy as np
from MisFunciones_2024 import *

#Elaborar un programa que permita capturar nombre y calificaciones de 8 personas ficticias, en dos arreglos diferentes, uno para nombres y otro para calificaciones. Posteriormente, se deberá mostrar el nombre de la persona con la calificación más alta y la calificación más baja.

Cls()

Tamaño = 8
nombres = []
calificaciones = list()

for i in range(Tamaño):
    nombres.append(input("Dame el nombre de la persona: "))
    calificaciones.append(leer_int(f"Dame la calificación de {nombres[i]}: "))

Cls()
print("Lista de alumnos")
print("==================================")
for x in range(Tamaño):
    print(f"{nombres[x]:<20} -> {calificaciones[x]:>3}")

pausa_final()