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

    def eliminar(self):
        os.remove(self.nombre)

# ---------------------- Codigo Principal ------------------
os.system("CLS")
archi = Archivo("Datos.txt")
texto1 = "Bienbenid@ a los archivos de texto.\n"

print(f"texto inicial para el archivo '{archi.nombre}':")
print(texto1)

archi.abrir(ESCRITURA)
archi.escribir(texto1)
algo = input("escribe algo en el archivo: ")
if algo.strip() == "":
    print("ok tonoto porque no escribiste nada????\n")
    print("tontito >:C")
else:
    archi.escribir(algo)
    print("se ah escrito lo siguiente en el archivo: ", algo)

archi.cerrar()

print(f"\n EL contenido del archvivo '{archi.nombre}' es:")
print("———————————————————————————————————————————————")   #ALT 0151
archi.contenido()
print("———————————————————————————————————————————————")

print(f"ahora mataremos a '{archi.nombre}'.")
os.system("pause")
archi.eliminar()
print(f"R.I.P {archi.nombre} a muerto :C.")
