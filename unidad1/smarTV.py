#Autor:Sadrach Juan Diego Garcia Flores
#Grupo: 2-2
#Fecha: 09/01/2024
import os

#---------------------------- Clases ----------------------------
class TV:
    def __init__(self, marca:str, pulgadas:int, color:str, resolucion:str = "4k"):
        self.marca = marca
        self.pulgadas = pulgadas
        self.color = color
        self.resolucion = resolucion
        self.encendido = False

    def imprimirInfo(self):
        print("informacion de la TV:")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
        print()

    def asignarPropietario(self, propietario:str):
        self.propietario = propietario

    def encender(self):
        try:
            print(f"tv de {self.propietario} encendido")
            self.encendido = True
        except:
            print("no se puede encender una pc que no tiene propietario")

    def apagado(self):
        try:
            print(f"tv de {self.propietario} apagado")
            self.encendido = False
        except:
            print("no se puede apagar una tv que no tiene propietario")

    def subirvolumen(self):
        if self.subirvolumen:
            print(f"tv de {self.propietario}subio volumen ↑")
        else:
            print("operacion no valida: subir volumen ↑")

    def bajarVolumen(self):
        if self.bajarVolumen:
            print(f"tv de {self.propietario}bajar volumen ↓")
        else:
            print("operacion no valida: bajar volumen ↓")

    def cambiarCanal(self):
        if self.cambiarCanal:
            print(f"tv de {self.propietario}cambio canal")
        else:
            print("operacion no valida: cambiar canal")

    def iniciarAplicacion(self,aplic:str):
        if self.iniciarAplicacion :
            print(f"tv de {self.propietario} ah ejecutado la aplicacion {aplic}.")
        else:
            print("operacion no valida:inicar aplicacion")


#----------------------- Codigo Principal------------------------
os.system("CLS")

miTV = TV("samsung", 40, "negro", "FullHD")
miTV.asignarPropietario("Sadrach Garcia")
miTV.encender()
miTV.imprimirInfo()

alanTV = TV("heisen", 40, "negro", "")
alanTV.asignarPropietario("Alan mada")
alanTV.apagado()
alanTV.imprimirInfo()

adrnianaTv = TV ("roku", 40, "Negro", "fullHD")
adrnianaTv.asignarPropietario("Adriana martinez")
adrnianaTv.encender()
adrnianaTv.imprimirInfo()

alanTV.subirvolumen()
miTV.bajarVolumen()
miTV.cambiarCanal()
miTV.iniciarAplicacion("Youtube")
print()

adrnianaTv.subirvolumen()
adrnianaTv.bajarVolumen()
adrnianaTv.cambiarCanal()
adrnianaTv.iniciarAplicacion("Netflix")

