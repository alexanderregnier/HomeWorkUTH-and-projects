#Sadrach Juan Diego Garcia Flores
#Fecha: 22/11/24
#grupo: 4-2

from MisFunciones_2024 import *
from stack_and_queue import *

Cls()
stack = Stack()

limite = 18
N1 = 0
N2 = 1

for i in range(limite):
    stack.push(N1)
    temp = N1
    N1 = N2
    N2 = temp + N2

print("La serie de Fibonacci es:")
print(stack.all_items())
print(f"El tope es: {stack.peek()}\n")

pausa_final()