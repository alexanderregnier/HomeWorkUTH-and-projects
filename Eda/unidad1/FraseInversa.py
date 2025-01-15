# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 20/09/2024

import os
os.system('cls')

Frase = input('Ingresa una frase: ')

def alreves(oracion: str):#hola = aloh por recursibidad
    frase_invertida = ""
    if len(oracion) > 0:
        frase_invertida = alreves(oracion[1:]) + oracion[0] 
    return frase_invertida


print(alreves(Frase))
# alreves(Frase)