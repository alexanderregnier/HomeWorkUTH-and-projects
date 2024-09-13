'''
Autor:Sadrach Juan Diego Garcia Flores
Grupo: 2-2
Fecha: 25/01/2024
'''
import os
ESCRITURA = 'w'
LECTURA = 'r'
#---------------------------- Clases -----------------------
class Archivo:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
    
    def abrir(self, modo:str):
        self.archivo = open(self.nombre, modo, encoding="utf-8")

    def escribir(self,texto:str):
        self.archivo.write(texto)

    def cerrar(self):
        self.archivo.close()

    def contenido(self):
        self.abrir(LECTURA)
        print(self.archivo.read())
        self.cerrar()

# ---------------------- Codigo Principal ------------------
os.system("CLS")

arch= Archivo("datos.txt")
arch.abrir(ESCRITURA)
arch.escribir("ola tonoto :D\n")
arch.escribir("ola tonoto :D\n")
arch.escribir("ola tonoto :D\n")
for x in range(10):
    arch.escribir(f"{x}\n")
arch.cerrar()

print(f"\n EL contenido del archvivo {arch.nombre} es:")
print("===============================================")
arch.contenido()
print("===============================================")