# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 03/10/2024

from MisFunciones_2024 import *

Cls()

# Un programa que, mediante el uso de una lista, podamos meter números, cadenas y objetos de la clase Billete
# Después que imprima por separado, primero los objetos que son billetes y después los que no son billetes.

class Billete:
    def __init__(self, _moneda, _valor):
        self.moneda = _moneda
        self.valor = _valor

    def info(self):
        return self.moneda, self.valor

Euros = Billete('Euro',500)
Dolar = Billete('Dolar',200)
Mxn= Billete('Peso',1)

Lista = []
Lista.append(1)
Lista.append("billete 20")
Lista.append(2)
Lista.append("billete 50")
Lista.append(3)
Lista.append("billete 100")
Lista.append(4)
Lista.append("billete 200")
Lista.append(5)
Lista.append("billete 500")
Lista.append(6)
Lista.append("billete 1000")
Lista.append(Euros)
Lista.append(Dolar)
Lista.append(Mxn)

print(Lista)
print("\nclase Billetes: ")
for e in Lista:
    if type(e) == Billete:
        print(e.info())
print()
for e in Lista:
    if type(e) is int or type(e) is float:
        print("Numero: ",e)
    
for e in Lista:
    if type(e) is str:
        print("str: ",e)

pausa_final()