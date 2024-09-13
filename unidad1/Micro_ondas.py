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
        print(f"el microondas esta descongelando pollo.")
        while pollo > 0:
            print(pollo, end=' ', flush = True)
            pollo -=1
            sleep(1)
        Beep(880,250)
        Beep(880,250)
        print("\nEND")

#----------------------- Codigo Principal-------------------
os.system("CLS")

micro1=MicroOndas("pepe", "Gris")
micro1.Calentar("una maruchan", 10)
micro1.descongelar("huevo", 10)
micro1.pizza(10)
micro1.palomitas(10)
micro1.pollo(10)