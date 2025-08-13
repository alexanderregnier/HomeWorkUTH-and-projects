# 9.- Un programa que permita crear un arreglo con 20 números SIN REPETIR entre el 1 y el 100.
# Los números los podrá introducir el usuario mediante el teclado o bien se pueden generar aleatorios de manera automática.

import numpy as np
from MisFunciones_2024 import *
import secrets

tamaño = 20
maximo = 100
minimo = 1
Arreglo = np.full(tamaño, -1, dtype=int)  # Inicializar con -1
while True:
    Cls()
    print("1.- Introducir numeros")
    print("2.- Generar numeros aleatorios")
    print("3.- ver arreglo")
    print("4.- borrar arreglo")
    print("5.- Salir")

    opcion = leer_int("Opcion: ")
    if opcion == 1:
        for i in range(tamaño):
            while True:
                numero = leer_int("Introduce un numero: ")
                if numero >= minimo and numero <= maximo:
                    if numero not in Arreglo:
                        Arreglo[i] = numero
                        break
                    else:
                        print("Numero repetido")
                else:
                    print("Numero fuera de rango")
    elif opcion == 2:
        numeros = set()
        while len(numeros) < 20:
            numero = secrets.SystemRandom().randint(1, 100)
            numeros.add(numero)
        
        for i, numero in enumerate(numeros):
            Arreglo[i] = numero

    elif opcion == 3:
        print(Arreglo)
        pausa()
    elif opcion == 4:
        Arreglo = np.full(tamaño, 0, dtype=int)
    elif opcion == 5:
        pausa("Bye bye")
        exit()
    else:
        print("Opcion incorrecta")
        pausa()
        exit()
