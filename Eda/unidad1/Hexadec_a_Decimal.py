# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 20/09/2024

import os
os.system('cls')

Numero = int(input('Ingresa un número: '))
def Hexadecimal(Numero): #Convertir un número decimal a hexadecimal con recursividad
    if Numero == 0:
        return ''
    else:
        Hexa ='0123456789ABCDEF'
        if Numero < 10:
            return Hexa[Numero]
        else:
            return Hexadecimal(Numero // 16) + Hexa[Numero % 16]
    
print(f'El número {Numero} en hexadecimal es: {Hexadecimal(Numero)}')