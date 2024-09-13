#Autor:Sadrach Juan Diego Garcia Flores
#Grupo: 2-2
#Fecha: 15/01/2024

import os
from time import sleep
from winsound import Beep

#---------------------------- Clases -----------------------
class MicroOndas:
    def __init__(self, marca:str, color:str,):
        self.marca = marca
        self.Color = color

    def tiempos(self):
        
        pass

    def Calentar(self, producto:str, tiempo:int, potencia:int=100):
        print(f"el microondas esta calentando {producto} por {tiempo} y esta usando una potencia de {potencia}% de potencia.")
        while tiempo > 0:
            print(tiempo, end=' ', flush = True)
            tiempo -=1
            sleep(1)
        Beep(880,250)
        Beep(880,250)
        print("\nEND")

    def descongelar(self, producto:str, tiempo3:int):
        print(f"el microondas esta descongelando {producto} por {tiempo3}.")
        while tiempo3 > 0:
            print(tiempo3, end=' ', flush = True)
            tiempo3 -=1
            sleep(1)
        Beep(880,250)
        Beep(880,250)
        print("\nEND")

    def pizza(self, rebanadas:int):
        print(f"el microondas esta calentando {rebanadas} de pizza.")
        while rebanadas > 0:
            print(rebanadas, end=' ', flush = True)
            rebanadas -=1
            sleep(3)
        Beep(880,250)
        Beep(880,250)
        print("\nEND")

    def palomitas(self, Palomitas:int):
        print("el microondas esta hacendo palomitas")
        while Palomitas > 0:
            print(Palomitas, end=' ', flush = True)
            Palomitas-=1
            sleep(2)
        Beep(880,250)
        Beep(880,250)
        print("\nEND")

    def pollo(self, pollo:int):
        print(f"el microondas esta descongelando {pollo} pollo.")
        tiempo = int(pollo/100)
        if tiempo==0: tiempo=1
        while pollo > 0:
            print(pollo, end=' ', flush = True)
            pollo -=1
            sleep(2.5)
        Beep(880,250)
        Beep(880,250)
        print("\nEND")

# ----------------------- Codigo Principal -----------------------
os.system("CLS")

#Crear un ejemplo del microondas
marca = input("Introduce la marca del microondas: ")
color = input("Introduce el color del microondas: ")
micro1 = MicroOndas(marca, color)

#Ejemplos de uso del microondas

#Ejemplo de microondas(modelo, color, tiempo, potencia, producto)
producto = input("Introduce el producto a calentar: ")
tiempo = int(input("Introduce el tiempo en segundos: "))
potencia = int(input("introduce la potencia del microondas: "))
micro1.Calentar(producto, tiempo, potencia)

#Ejemplo descongenlando
producto_descongelar = input("Introduce el producto a descongelar: ")
tiempo_descongelar = int(input("Introduce el tiempo en segundos: "))
micro1.descongelar(producto_descongelar, tiempo_descongelar)

#ejemplo de pizza
Tiempo_pizza = int(input("Introduce el tiempo en segundos que necsita la pizza: "))
micro1.pizza(Tiempo_pizza)

#ejemplo de palomitas
Tiempo_palomitas = int(input("Introduce el tiempo en segundos que necsita las palomitas: "))
micro1.palomitas(Tiempo_palomitas)

#ejemplo de pollo
Tiempo_pollo = int(input("Introduce el tiempo en segundos que necsita el pollo: "))
micro1.pollo(Tiempo_pollo)
