
#Autor:Sadrach Juan Diego Garcia Flores
#Grupo: 2-2
#Fecha: 09/01/2024
import os

#---------------------------- Clases ----------------------------
class Celular:
    def __init__(self, marca:str, modelo:str, almaGB:int, memoriaGB:int, SistOp:str):
        self.marca = marca
        self.modelo = modelo
        self.almaGb = almaGB
        self.memoriaGB = memoriaGB
        self.SistOp = SistOp

    def asignarPropietario(self, propietario:str):
        self.propietario = propietario

    def activar(self, compañia:str, numero:str):
        self.compañia = compañia
        self.numero = numero

    def tomarFoto(self):
        print(f"El celular de {self.propietario} ah tomado una foto")

    def ejecutarapp(self, nombreApp):
        print(f"El celular de {self.propietario} ah ejecutado la {nombreApp}")

    def Llamar(self, destinatario):
        if type(destinatario) == Celular:
            print(f"{self.numero} esta llamando a {destinatario.numero}.\n")
        else:
            print("El destinatario debe ser un celular invalido.\n")

    def enviarSMS(self, destinatario, mensaje:str):
        if type(destinatario) == Celular:
            print(f"{self.numero} esta enviado el mensje {mensaje} a {destinatario.numero}.\n")
            destinatario.__recibirSMS(self,mensaje)
        else:
            print("El destinatario debe ser un celular invalido.\n")

    def __recibirSMS(self, emisor, mensaje:str): #metodo privado
        print(f"{self.numero} recibiendo mensaje '{mensaje}' de {emisor.numero}.\n")

    def imprimirInfo(self):
        print("Informacion del celular:")
        # print(self.__dict__)
        # for key in self.__dict__:
            # print(f"{key}: {self.__dict__[key]}")

        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
        print()

#----------------------- Codigo Principal------------------------
os.system("CLS")
mi_cel = Celular("Oppo","A50", 64, 4,"Android 12.0")
mi_cel.asignarPropietario("Sadrach Garica")
mi_cel.activar("telcel", "6623514542")
mi_cel.imprimirInfo()
mi_cel.tomarFoto()

alan_cel = Celular("oppo", "Reno 10 5G", 256, 16, "Android 13, ColorOs")
alan_cel.asignarPropietario("Alan Fernandez")
alan_cel.activar("unefon", "6621555555")
alan_cel.imprimirInfo()
alan_cel.tomarFoto()
alan_cel.ejecutarapp("youtube")

juan_cel = Celular("oppo", "A50", 64, 4, "android 12, colorOS")
juan_cel.asignarPropietario("Juan Garcia")
juan_cel.activar("telcel", "6623888888")
juan_cel.Llamar(alan_cel)
juan_cel.enviarSMS(mi_cel,"hola, ¿como estas?")