#Sadrach Juan Diego Garcia Flores
#Fecha: 25/10/24
#grupo: 4-2

# 4.1.2.- Elabore un programa que introduzca 10 números en una lista y que mediante el uso de una pila los ponga en la lista de vuelta
# en orden inverso al que tenían. Imprimir la lista final.

from stack_and_queue import *
from MisFunciones_2024 import *
import random as rnd

Cls()
pila = Stack()
lista = []

for x in range(10):
    lista.append(rnd.randint(1, 100))

print("Lista original:")
print(lista)

for x in lista:
    pila.push(x)

lista.clear()

while pila.size() > 0:
    lista.append(pila.pop())

print("\nLista invertida:")
print(lista)

pausa_final()