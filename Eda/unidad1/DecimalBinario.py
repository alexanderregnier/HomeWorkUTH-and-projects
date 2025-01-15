# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 20/09/2024

import os
os.system('cls')

Numero = int(input('Ingresa un número: '))

def Binario(Numero): #Convertir un número decimal a binario con recursividad
    if Numero == 0:
        return ''
    else:
        return Binario(Numero // 2) + str(Numero % 2)
    
print(f'El número {Numero} en binario es: {Binario(Numero)}')