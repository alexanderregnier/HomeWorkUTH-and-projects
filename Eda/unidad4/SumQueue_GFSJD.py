from MisFunciones_2024 import *
from stack_and_queue import Queue
import random as rnd
import numpy as np

class Queue(Queue):
    def sum(self):
        return np.sum(self.all_items())

Cls()
cola = Queue()
for i in range(15):
    cola.enqueue(rnd.randint(1,1000))

print(cola.all_items(),"<--ultimo elemento",cola.last())
print("La suma de los elementos de la cola es:",np.sum(cola.all_items())) #Numpy
print("La suma de los elementos de la cola es:",cola.sum()) #Método de la clase Queue eredada

pausa_final()