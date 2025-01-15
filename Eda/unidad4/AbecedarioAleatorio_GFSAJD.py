# Sadrach Juan Diego Garcia Flores
# Fecha: 15/11/24
# grupo: 4-2

from MisFunciones_2024 import *
from stack_and_queue import Queue
import random as rnd

abd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

cola = Queue()
fecuencia = {}

Cls()
for i in range(25):
    num = rnd.choice(abd)
    cola.enqueue(num)

print(f"Alfabeto disponible: {abd}")
print(f"Cola con letras aleatorias:\n{cola.all_items()}")

for i in range(25):
    letra = cola.dequeue()
    if letra in fecuencia:
        fecuencia[letra] += 1
    else:
        fecuencia[letra] = 1

print("\nFrecuencia de las letras en la cola:")

for num in fecuencia:
    print(f"{num} -> {fecuencia[num]}", end="\t")

print("\n")
pausa_final()