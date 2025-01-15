#Sadrach Juan Diego Garcia Flores
#Fecha: 08/11/24
#grupo: 4-2

# Escribir un método o función "Reemplazar" para las pilas al que se le den como argumentos dos valores: nuevo y viejo, y que 
# funcione de forma que si el valor viejo aparece una o más veces en algún lugar de la pila, estos sean reemplazados por el valor nuevo.
# def replace(self, old_value, new_value):
# NOTA: Entregar los 2 archivos, tanto el del programa como el de la clase donde hayas creado el método .replace()

from MisFunciones_2024 import *
from stack_and_queue import *
import random as rnd

Cls()
pila = Stack()
for e in range(20):
    pila.push(rnd.randint(1,100))

while True:
    print(f'Pila: {pila.all_items()}')
    opcion = input("¿Desea remplazar algun numero?(S/N): ").lower()
    if opcion == "s":
        opcion2 = leer_int("Qué valor desea reemplazar? ")
        if opcion2 in pila.all_items():
            opcion3 = leer_int("Nuevo valor: ")
            pila.replace(opcion2, opcion3)
        else:
            print(f'La pila no contiene el valor {opcion2}\n')
    elif opcion == "n":
        break
    else:
        print("Opción no válida\n")
