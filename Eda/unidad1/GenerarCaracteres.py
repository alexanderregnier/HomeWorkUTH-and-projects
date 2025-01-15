# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 08/09/2024

from os import *
system("cls")

#Escribir una función recursiva para un programa de Python que genere cadenas repetidas:
Caracteres = input("Ingrese una cadena: ")
cantidad = input("Ingrese la cantidad a repetir: ")

def GenerarCaracteres(Caracteres, cantidad):
    if cantidad == 0:
        return ""
    else:
        return Caracteres + GenerarCaracteres(Caracteres, cantidad-1)

print(GenerarCaracteres(Caracteres, int(cantidad)))