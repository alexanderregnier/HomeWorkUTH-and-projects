# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 27/09/2024

from MisFunciones_2024 import * 

Cls()

Lista1 = ['Tomate','Cebolla','Huevos','Leche','Arroz']
Lista2 = [0,1,2,3,4,5,6,7,8,9]
Lista3 = [10,11,12,13,14,15,16,17,18,19]

print(Lista1)
print(*Lista1) #Imprime los valores de las listas
print(Lista2)
print(Lista3)
print()
print(Lista1[1])
print(Lista2[4])
print(Lista3[0])
print()
print("Leche" in Lista1)        #operador in → da true si el valor esta en la Lista 1

print(Lista2[:4])
print(Lista2 + Lista3)

Lista1[0] = "ajo"
print(Lista1)

pausa_final()