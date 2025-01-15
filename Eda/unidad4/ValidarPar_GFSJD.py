#Sadrach Juan Diego Garcia Flores
#Fecha: 08/11/24
#grupo: 4-2

from MisFunciones_2024 import *
from stack_and_queue import *

def validar_parentesis(expresion: str):
    pila = Stack()
    for i in expresion:
        if i == "(":
            pila.push(i)
        elif i == ")":
            if pila.size() == 0:
                return False
            pila.pop()
    return pila.size() == 0

while True:
    Cls()
    print("Validación de paréntesis en una expresión matemática.")
    expresion = input("Introduzca la expresión: ")
    if validar_parentesis(expresion):
        print("La expresión es correcta.")
        pausa("Puchale para continuar...")
    else:
        print("La expresión tiene error en los paréntesis.")
        pausa("Puchale para continuar...")