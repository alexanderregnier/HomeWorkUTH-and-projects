'''
Archivo: cls_archivo_JSON.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 16-febrero-2022

Objetivo: Proporcionar una clase para gestionar un archivo contenedor de JSONs.
'''
import os
import json

ESCRITURA = 'w'
LECTURA = 'r'

def InfoExcepcion():
    import traceback
    stack = traceback.extract_stack()[:-2]
    return traceback.format_list(stack)
    # Checar:
    # https://stackoverflow.com/questions/6086976/how-to-get-a-complete-exception-stack-trace-in-python


class ArchivoJSON:
    ''' Archivo contenedor de una lista de JSONs. '''
    def __init__(self, _nombre:str) -> None:
        self.nombre = _nombre
        self.__stream = None

    def Existe(self):
        ''' Devuelve True si el archivo existe, False si no.'''
        return os.path.isfile(self.nombre)

    def Abrir(self, _modo):
        ''' Abrir el archivo en modo ESCRITURA o LECTURA. '''
        try:
            self.__stream = open(self.nombre, _modo, encoding="UTF-8")
        except Exception as e:
            if str(e).__contains__("No such file") :
                print(f"El archivo '{self.nombre}' no existe.")
            else:
                print(e, "↓↓") 
            print(*InfoExcepcion())
            exit("EXIT: Se ha interrumpido la ejecución del programa.\n")


    def Escribir(self, _texto):
        ''' Escribir texto en un archivo que se ha abierto en modo ESCRITURA. '''
        try:
            self.__stream.write(_texto)
        except Exception as e:
            if str(e).__contains__("NoneType") :
                print(f"El archivo '{self.nombre}' no se ha abierto.")
            elif str(e).__contains__("I/O operation on closed file") :        
                print(f"El archivo '{self.nombre}' está cerrado.")
            else:
                print(e, "↓↓")     
            print(*InfoExcepcion())
            exit("EXIT: Se ha interrumpido la ejecución del programa.\n")


    def Cerrar(self):
        self.__stream.close()


    def CrearNuevo(self):
        ''' Crear un archivo nuevo con una lista vacía: [] . Si el archivo 
            ya estaba creado, su contenido anterior se pierde. '''
        self.Abrir(ESCRITURA)
        self.Escribir("[]")
        self.Cerrar()


    def TomarContenido(self) -> list:
        ''' Devuelve una lista con los JSONs que están en el archivo. '''
        self.Abrir(LECTURA)
        datos_json = self.__stream.read()
        self.Cerrar()
        try:
            lista_json = json.loads(datos_json)
            return lista_json
        except Exception as e:
            # if str(e).__contains__("Expecting value"):
            #     print("ArchivoJSON vacío.")
            # else:
            #     print(e)
            print(e)
            return []


    def ActualizarContenido(self, lista:list):
        ''' Vuelve a crear el archivo JSON con datos de la lista. '''
        self.Abrir(ESCRITURA)
        json.dump(lista, self.__stream, indent=4, separators=(", ", " : "), ensure_ascii=False)
        self.Cerrar()


    def Eliminar(self):
        os.remove(self.nombre)