# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 27/09/2024

# import MisFunciones_2024          #Forma1
from MisFunciones_2024 import *     #Forma2
# from MisFunciones_2024 import CLS   #Forma3

Cls()
# MisFunciones_2024.CLS()
# MisFunciones_2024.pausa_final()

#Como se crean las listas en python
Colores = []                    #Forma1
Colores = list()                #Froma1

Colores.append("Azul")  #Elemento 0
Colores.append('Rojo')  #Elemento 1
Colores.append('Verde')  #Elemento 2
Colores.append('Amarillo')  #Elemento 3
Colores.append('morado')  #Elemento 4
Colores.append('negro')  #Elemento 5
Colores.append('cafe')  #Elemento 6
Colores.append('rosa')  #Elemento 7
Colores.append('gris')  #Elemento 8
Colores.append('naranja')  #Elemento 9

print("Lista de colores:", Colores)
print("\nLista de colores:")
for e in Colores:
    print(e,end=', ')

print("\n\nEl segundo elemento de la lista es:",Colores[1])
Colores[2] = "guinda"
print("Lista de colores:", Colores)
Colores.insert(2,"Blanco")

print("Lista de colores:", Colores)

print("\nTenemos:", len(Colores),"elemntos en la lista")
print("Tenemos:", Colores.__len__(),"elemntos en la lista")

print("\n¿Tenemos guinda ->", Colores.__contains__("guinda"))
print("¿Tenemos pepe ->", Colores.__contains__("pepe"))

if Colores.__contains__("negro"):
    print("El negro esta en la posicion:", Colores.index("negro"))

if Colores.__contains__("pepe"):
    print("El rosa esta en la posicion:", Colores.index("pepe"))
else:
    print("no hay sonso JAJAJAJAJAJAJAJJJAJ en tonto el tonto JAJAJAJJAJAJA")

print("\nAhora limpiaremos la lsita:")
Colores.clear()
print("Tenemos:", len(Colores),"elemntos en la lista")
print("Lista de colores:", Colores)

pausa_final()