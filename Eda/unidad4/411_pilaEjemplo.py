#Sadrach Juan Diego Garcia Flores
#Fecha: 25/10/24
#grupo: 4-2

from MisFunciones_2024 import *
from stack_and_queue import *
from random import randint

pila = Stack()
# for x in range(5):
#     pila.push(randint(1, 100))

while True:
    Cls()
    print("1.- Mostrar pila")
    print("2.- Insertar un elemnto (Push)")
    print("3.- Sacar un elemento (Pop)")
    print("4.- Salir del progrma\n")
    opcion = leer_int("Opción: ")

    match opcion:
        case 1:
            if pila.size() > 0:
                print("pila:")
                for e  in reversed(pila.all_items()): print(f"{e}")
                print("El Top es:", pila.peek())
                pausa("Presione para continuar...")
            else:
                beep_error()
                pausa("La pila está vacía...")
        case 2:
            pila.push(leer_int("Elemento a insertar: "))
        case 3:
            if pila.size() > 0:
                e = pila.pop()
                print(f"\nSe ah sacado un {e} elemento de la pila...")
                pausa("Presione para continuar...")
            else:
                beep_error()
                pausa("La pila está vacía...")
        case 4:
            break
        case _:
            beep_error()
            pausa("\nOpción no válida...")
        