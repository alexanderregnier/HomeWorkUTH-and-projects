# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 03/10/2024

from MisFunciones_2024 import *
from math import pi

Cls()

#Elabore un programa que reúna en una misma lista a cadenas y números, 
#y que después imprima por separado primero los números y luego las cadenas.

nyl = []

nyl.append("Es una string")
nyl.append(18)
nyl.append("El agua moja")
nyl.append("subir para arriba")
nyl.append(4)
nyl.append("El pobre es pobre porque quiere")
nyl.append("El pri robo mas")
nyl.append("me canso ganso")
nyl.append(pi)

print(nyl)

print("\nLos numeros de la lista son:")
for e in nyl:
    if type(e) is int or type(e) is float:
        print(e)

print("\nLas palabras de la lista son:")
for e in nyl:
    if type(e) is str:
        print(e)

pausa_final()