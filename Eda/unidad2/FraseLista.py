# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 03/10/2024

#Elabore un programa que pida una frase de entrada, luego separe las palabras y las ponga en una lista.
#Al final imprimir la lista de palabras de tres maneras: en el orden en que escribieron en la frase,
#en el orden alfabético y el orden alfabético descendente.

from MisFunciones_2024 import *

Cls()

frase = input("Escribe una frase: ")
SigPun = "*/?!.,;:[]{}'\"@?¡=*¨()¿.+-"
# frase = "hola como estas?"

#separar putnos como el * / ? etc y colocarlos como una palabra separada
for e in SigPun:
    frase = frase.replace(e, " ")
    frase.append(e)

Lista = frase.split()

print("Normal:\n", Lista)
Lista.sort(key=str.casefold)
print("Alfabetico:\n", Lista)
Lista.sort(reverse=True)
print("Alfabetico Descendente:\n", Lista)

pausa_final()
