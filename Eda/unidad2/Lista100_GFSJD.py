# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 11/10/2024

from MisFunciones_2024 import *
import secrets

Cls()

# 1) Crear lista con 100 números aleatorios
# 2) Mostrar lista
# 3) Mostrar frecuencias   
# 4) Reemplazar elementos
# 5) Eliminar elemento indicando su posición
# 6) Eliminar elementos indicando su valor
# 7) Salir


ListNumeros = []
while True:
    Cls()
    print("Opciones a elegir: ")
    print("===============================================")
    print(1, "Crear lista con 100 números aleatorios")
    print(2, "Mostrar lista")
    print(3, "Mostrar frecuencias")
    print(4, "Reemplazar elementos")
    print(5, "Eliminar elemento indicando su posición")
    print(6, "Eliminar elementos indicando su valor")
    print(7, "Salir")
    opcion = leer_int("Ingrese la opcion deseada: ")

    match opcion:
        case 1: # Crear lista con 100 números aleatorios
            if len(ListNumeros) > 0:
                Cls()
                print("La lista ya tiene elementos")
                pausa()
                Cls()
                continue
            else:
                for i in range(100):
                    ListNumeros.append(secrets.SystemRandom().randint(1, 100))
                Cls()
                print("Lista de 100 numeros aleatorios creada")
                pausa()
                Cls()
        case 2: # Mostrar lista"
            if len(ListNumeros) == 0:
                Cls()
                print("La lista esta vacia")
                pausa()
                Cls()
            else:
                Cls()
                print("Lista de 100 numeros aleatorios:\n",*ListNumeros)
                pausa()
                Cls()
        case 3: # Mostrar frecuencias
            frecuencias = {}

            for num in ListNumeros:
                if num in frecuencias:
                    frecuencias[num] += 1
                else:
                    frecuencias[num] = 1

            Cls()
            print("Numeros repetidos:")
            for num, count in sorted(frecuencias.items()):
                print(f"{num}->{count}", end="  ")
            pausa()
            Cls()
        case 4: # Reemplazar elementos
            Cls()
            
            NumRem = leer_int("La posicion de el numero que quiere remplazar en la lista es: ")
            if 0 <= NumRem < len(ListNumeros):
                print(f'El numero de la posicion {NumRem} es:', ListNumeros[NumRem])
                Remplazo = leer_int("por cual numero lo vas a remplazar? ")
                ListNumeros[NumRem] = Remplazo
                ListNumeros.insert(NumRem , Remplazo)

                Cls()
                print(f"{NumRem} ha sido remplazado por {Remplazo}")
            else:
                print("Posicion no valida")
            pausa()
            Cls()
        case 5: # Eliminar elemntos indicando su valor
            Cls()
            NumElim = leer_int("La posicion de el numero que quiere eliminar en la lista es: ")
            if 0 <= NumElim < len(ListNumeros):
                print(f'El numero de la posicion {NumElim} es:', ListNumeros[NumElim])
                ListNumeros.pop(NumElim)
                print(f"{NumElim} ha sido Eliminado")
            else:
                print("Posicion no valida")
            pausa()
        case 6: #Eliminar elementos indicando su valor
            Cls()
            Numero_eliminar = leer_int("todos los numeros seran elimados, cual desea eliminar? ")
            ListNumeros = [num for num in ListNumeros if num != Numero_eliminar]
            Cls()
            print(f"Todos los elementos con el valor {Numero_eliminar} han sido eliminados.")
            pausa()
            Cls()

        case _:
            print("Opcion no valida")
