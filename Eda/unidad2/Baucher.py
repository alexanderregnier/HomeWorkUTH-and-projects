# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 03/10/2024

from MisFunciones_2024 import *

Cls()

# Un programa que tenga una clase "Artículo" que contenga los atributos de: Nombre, Cantidad, Precio.
# Después crear una lista de objetos de esa clase y un método que calcule el total a pagar por todos los artículos de la lista.
# Debe imprimirse también la lista de los artículos sus cantidades y precios (como si fuera un ticket de compras).

class Articulo:
    def __init__(self, _nombre, _cantidad, _precio):
        self.nombre = _nombre
        self.cantidad = float(_cantidad)
        self.precio = float(_precio)
    
    def info(self):
        return self.nombre, self.cantidad, self.precio

Lista = []
while True:
    NomArti = input('Nombre del artículo: ')
    Precio = input('Precio: ')
    Cantidad = input('Cantidad: ')

    Lista.append(Articulo(NomArti, Precio, Cantidad))

    d = input('¿Desea agregar otro artículo? (s/n): ').lower()
    if d == 'n':
        break

total = 0
print('Ticket de compra:')
for i in Lista:
    # print(i.info())
    total += i.cantidad * i.precio

print('lista de articulos:')
print('Articulos         Precios         Cantidad  subtotal')
print('================= =============== ========= =========')
for i in Lista:
    print(f'{i.nombre[0:20]:<18} $ {i.precio:4,.2f} {i.cantidad:14,.2f} $ {i.cantidad * i.precio:,.2f}')

print(f'Total a pagar: ${total:.2f}')

pausa_final()