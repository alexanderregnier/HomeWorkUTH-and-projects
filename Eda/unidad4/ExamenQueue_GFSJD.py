#Sadrach Juan Diego Garcia Flores
#Fecha: 22/11/24
#grupo: 4-2

from MisFunciones_2024 import *
from stack_and_queue import *
import secrets

Cls()
queue1 = Queue()
queue2 = Queue()
queueRepit = Queue()

for i in range(20):
    queue1.enqueue(secrets.SystemRandom().randint(1,100))

print("Cola1:")
print(queue1.all_items())

for i in range(20):
    queue2.enqueue(secrets.SystemRandom().randint(1,100))

print("\nCola2:")
print(queue2.all_items())

print("\nElementos comunes:")
for i in range(20):
    num = queue1.dequeue()
    if num in queue2.all_items():
        queueRepit.enqueue(num)

print(queueRepit.all_items())
