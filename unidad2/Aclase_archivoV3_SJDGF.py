'''
Autor:Sadrach Juan Diego Garcia Flores
Grupo: 2-2
Fecha: 25/01/2024
'''
import os
ESCRITURA = 'w'
LECTURA = 'r'

def InfoExeption():
    import traceback
    stack = traceback.extract_stack()[:-2]
    return traceback.format_list(stack)
#---------------------------- Clases -----------------------
class Archivo:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self.stream = None
    
    def abrir(self, modo:str):
        try:
            self.stream = open(self.nombre, modo, encoding="utf-8")
        except Exception as e:
            if (str(e).__contains__("NO such file")):
                print(f"el archivo '{self.nombre}' no existe")
            else:
                print(e)
            exit("exit , se ah interrumpido la ejecucion del programa.\n")

    def escribir(self,texto:str):
        try:
            self.stream.write(texto)
        except Exception as e:
            if str(e).__contains__("None type"):
                print(f"El archivo '{self.nombre}' no se ah abierto")
            elif str(e).__contains__("I/o operations on closed file"):
                print(f"El archivo '{self.nombre}' no esta cerrado")
            else:
                print(f"El archivo ' {self.nombre}' esta cerrado")

    def cerrar(self):
        self.stream.close()

    def contenido(self):
        self.abrir(LECTURA)
        print(self.stream.read())
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

print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ")
print("   /////////             //          ////      ////    //////////            ////////    //             //   //////////    //////      ")
print(" ///                   //  //        //  //  //  //    //                  ///      ///   //          //     //           //    //     ")
print(" ///                 //      //      //    //    //    ///////            ///        ///   //       //       ///////      //    //    ")
print(" ///      ///       ////////////     //          //    //                 ///        ///    //     //        //           //////     ")
print(" ////      ///    //           //    //          //    //                  ///     ///       //  //          //           //    //    ")
print("  //////////     //             //   //          //    ///////////          ////////          ////           ///////////  //     //   ")
print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ")


