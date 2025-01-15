# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 27/09/2024

from MisFunciones_2024 import *

Cls()

Lista1 = ['Tomate','Cebolla','Huevos','Leche','Arroz']
Lista2 = [1,2,3,4,5]
Lista3 = [6,7,8,9,10]
Lista4 = ['d','f','a','b','e','c']

Lista1.append(50)
print(Lista1)
print()
del Lista1[3]
print(Lista1)
print()
Lista2.extend(Lista3)
print(Lista2)

Lista1.remove("Arroz")
print(Lista1)

Lista4.sort()
print(Lista4)

pausa_final()