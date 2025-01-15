#Sadrach Juan Diego Garcia Flores
#Fecha: 25/10/24
#grupo: 4-2

import numpy as np
from MisFunciones_2024 import *

Cls()

#OPCION 1
Nombres = np.empty(8, dtype=object)
Calificaciones = np.empty(8, dtype=np.int64)

for i in range(8):
    Nombres[i] = input("Nombre: ")
    Calificaciones[i] = int(input("Calificación: "))
    Cls()

Aprobados = np.sum(Calificaciones >= 70)
Reprobados = np.sum(Calificaciones < 70)
Promedio = np.mean(Calificaciones)
Maxima = np.max(Calificaciones)
Minima = np.min(Calificaciones)
#=============================================================

# OPCION 2
# Nombres = ["Carlos Lopez", "Manuel Martinez", "Marcela Aguilera", "Gonzalo Teran", "Julia De la Rosa", "Martin Moreno", "Ana Maria Rivas", "Juan Perez"]
# Calificaciones = [67, 87, 91, 65, 70, 69, 95, 71]

# Aprobados = np.sum(np.array(Calificaciones) >= 70)
# Reprobados = np.sum(np.array(Calificaciones) < 70)
# Promedio = np.mean(Calificaciones)
# Maxima = np.max(Calificaciones)
# Minima = np.min(Calificaciones)

print(f"Promedio: {Promedio:10}")
print(f"Máxima: {Maxima:8}\tAlumno con máxima: {Nombres[np.argmax(Calificaciones)]}")
print(f"Mínima: {Minima:8}\tAlumno con mínima: {Nombres[np.argmin(Calificaciones)]}")
print(f"Aprobados: {Aprobados:4}")
print(f"Reprobados: {Reprobados:3}")