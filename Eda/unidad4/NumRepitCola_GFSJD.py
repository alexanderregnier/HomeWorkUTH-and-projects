# Sadrach Juan Diego Garcia Flores
# Fecha: 11/11/24
# grupo: 4-2

# 4.2.2.- Elaborar un programa que cargue 20 números enteros aleatorios (entre el 1 y el 100) en una cola SIN REPETIR.
# Después imprimir la cola completa, el valor mayor, el menor, el promedio, el primero de la cola y el último.

from MisFunciones_2024 import *
from stack_and_queue import Queue
import numpy as np
import secrets

class Queue(Queue):
    def promedio(self, items):
        suma = 0
        for i in items:
            suma += i
        return suma/len(items)

Cls()
cola = Queue()
# cola2 = Queue()
for i in range(20):
    while True:
        num = secrets.SystemRandom().randint(1,100)
        if num not in cola.all_items():
            cola.enqueue(num)
            break
        # else:
        #     cola2.enqueue(num)


print(f"Cola: {cola.all_items()}")
print(f"Mayor: {max(cola.all_items())}")
print(f"Menor: {min(cola.all_items())}")
# print(f"Promedio: {np.mean(cola.all_items())}")
print(f"Promedio: {cola.promedio(cola.all_items())}")
print(f"Primero: {cola.first()}")
print(f"Ultimo: {cola.last()}")

# print(f"Repetidos: {cola2.all_items()}")
