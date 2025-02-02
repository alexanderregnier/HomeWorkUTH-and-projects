#Sadrach Juan Diego Garcia Flores
#Fecha: 05/11/24
#grupo: 4-2

# 4.1.3.- Elaborar un programa que realice lo siguiente: Cargar 2 pilas A y B con 10 números enteros aleatorios cada una de ellas.
# Después crear una tercera pila C con los números contenidos intercalados de las pilas A y B, es decir, ir sacando alternadamente 1
# elemento de A y luego 1 elemento de B, y así sucesivamente.
# Haga que el programa muestre los contenidos de las pilas A y B antes de mezclarlas en C; y luego, después de una pausa, que muestre el
# contenido de C. Favor de mostrar los contenidos de manera horizontal (en la misma línea todos los elementos de la pila)

from MisFunciones_2024 import *
from stack_and_queue import *
import secrets

Cls()
pilaA = Stack()
pilaB = Stack()

for i in range(10):
    pilaA.push(secrets.SystemRandom().randint(1, 100))
    pilaB.push(secrets.SystemRandom().randint(1, 100))

print("Pila A: ", pilaA.all_items(), "<--Tope: ",pilaA.peek(), "\n")
print("Pila B: ", pilaB.all_items(), "<--Tope: ",pilaB.peek(),"\n")

pausa("Precione para continuar...")
PilaC = Stack()
for i in range(10):
    PilaC.push(pilaA.pop())
    PilaC.push(pilaB.pop())

PilaC.all_items().reverse()
print("Pila C: ", PilaC.all_items(),"<--Tope: ",PilaC.peek())

pausa_final()
