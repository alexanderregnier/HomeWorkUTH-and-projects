#Autor:Sadrach Juan Diego Garcia Flores
#Grupo: 2-2
#Fecha: 15/01/2024

import os
from time import sleep
from winsound import Beep

#---------------------------- Clases -----------------------
class consola:
    def __init__(self, Nconsola:str, juego:str, propietrario:str):
        self.Nconsola=Nconsola
        self.juego=juego
        self.propietario=propietrario
        self.encendido = False

    def asignarPropietario(self, propietario:str):
        self.propietario = propietario

    def encender(self):
        try:
            print(f"consola {self.Nconsola} de {self.propietario} encendido")
            self.encendido = True
            Beep(888,55)
        except:
            print("no se puede encender una consola que no tiene propietario")

    def apagar(self):
        try:
            print(f"consola {self.Nconsola} de {self.propietario} apagado")
            self.encendido = False
        except:
            print("no se puede apagar una tv sin propietario")
            Beep(588,25)


    def ejecutarJuego(self, juego:str):
        print(f"Se esta ejecutando el juego {juego}")
        juego = 2
        while juego>0:
            print(juego, end=' ', flush=True)
            juego -=1
            sleep(2.5)


# ---------------------- Codigo Principal -----------------------
os.system("CLS")

mi_consola = consola("Nintendo Dsi", "", "Sadrach")
mi_consola.asignarPropietario("Sadrach Garcia")
mi_consola.encender()

juego_nuevo = input("Introduce el juego que deseas jugar: ")
Beep(888,55)
mi_consola.juego = juego_nuevo
mi_consola.ejecutarJuego(juego_nuevo)
print()

mi_consola.apagar()
Beep(222,80)
