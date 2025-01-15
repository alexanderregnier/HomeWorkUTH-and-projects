'''
Autor: José Padilla Duarte
Grupo: TIDS4-_
Fecha de última modificación: 25-noviembre-2024
'''
from random import randint
from MisFunciones_2024 import *
from treenode import TreeNode
import time

a1 = TreeNode()     # a1 es la raíz del árbol

while True:
    CLS()
    print("Ejemplo 5.1.- Árbol binario")
    print("┌────────────── Menú de opciones ─────────────┐")    # •-=-•
    print("1. Insertar elemento en árbol")
    print("2. Hacer recorrido in-orden")
    print("3. Hacer recorrido pre-orden")
    print("4. Hacer recorrido post-orden")
    print("5. Imprimir la raiz")
    print("6. Insertar 5 números aleatorios en el árbol")
    print("7. Buscar un elemento en el árbol")
    print("8. Eliminar un elemento del árbol")
    print("9. Salir")
    opcion = leer_int("\nTeclee la opción deseada: ")

    match opcion:
        case 0:
            continue
        
        case 1: # Insertar
            num = leer_int("Introduzca el número a insertar: ")
            if num == 0:
                beep_error()
            else:
                a1.insert(num)
                print("Se insertó un:", num)
                time.sleep(1)

        case 2:
            if a1.value == None:
                beep_error()
                pausa("\nEl árbol está vacío.")
            else:
                datos = []
                a1.inorden(datos)
                print("\nEste es el recorrido in-orden:", datos)
                pausa("\nPresione una tecla para continuar...")

        case 3:
            if a1.value == None:
                beep_error()
                pausa("\nEl árbol está vacío.")
            else:
                datos = []
                a1.preorden(datos)
                print("\nEste es el recorrido pre-orden:", datos)
                pausa("\nPresione una tecla para continuar...")

        case 4:
            if a1.value == None:
                beep_error()
                pausa("\nEl árbol está vacío.")
            else:
                datos = []
                a1.postorden(datos)
                print("\nEste es el recorrido post-orden:", datos)
                pausa("\nPresione una tecla para continuar...")

        case 5:
            if a1.value == None:
                beep_error()
                pausa("\nEl árbol está vacío.")
            else:
                print("La raíz del árbol es:", a1.value)
                pausa("\nPresione una tecla para continuar...")

        case 6:
            datos = []
            for x in range(5):
                e = randint(1,100)
                datos.append(e)
                a1.insert(e)
            print("Se agregaron:", datos)
            pausa("\nPresione una tecla para continuar...")

        case 7: #Opción buscar
            CLS()
            if a1.value == None:
                beep_error()
                pausa("\nEl árbol está vacío.")
            else:
                num = leer_int("Introduzca el número a buscar: ")
                if num == 0:
                    beep_error()
                else:
                    if a1.search(num):
                        print(f"El número {num} SI se encontró en el árbol.")
                    else:
                        beep_error()
                        print(f"El número {num} NO se encontró en el árbol.")
                    pausa("\nPresione una tecla para continuar...")

        case 8: #Opción eliminar
            if a1.value == None:
                beep_error()
                pausa("\nEl árbol está vacío.")
            else:
                num = leer_int("Introduzca el número a eliminar: ")
                if num == 0:
                    beep_error()
                else:
                    if a1.delete(num):
                        print("Se eliminó el número:", num)
                    else:
                        beep_error()
                        print("El número no se encontró en el árbol.")
                    pausa("\nPresione una tecla para continuar...")

        case 9: # Salida
            print("El programa ha finalizado.")
            break   # Salir del while True

        case _:
            beep_error()
            print("La opción no es válida.")
            time.sleep(1.5)
