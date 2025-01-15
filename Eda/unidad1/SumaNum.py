# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 20/09/2024

import os
os.system('cls')

Numero = int(input('Ingresa un número: '))

def SumaNum(Numero):#Sumar 1234 = 10 recursividad
    if Numero == 0:
        return 0
    else:
        return (Numero % 10) + SumaNum(Numero // 10)

print(f'La suma de los digitos del número {Numero} es: {SumaNum(Numero)}')

