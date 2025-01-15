# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 20/09/2024

import os
os.system('cls')

def Numeros(c):
    if c <= 100:
        print(c, end=',')
        Numeros(c+1)

Numeros(1)
print()

os.system("Pause")