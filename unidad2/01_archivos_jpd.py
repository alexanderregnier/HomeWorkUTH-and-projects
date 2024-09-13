'''
Autor:Sadrach Juan Diego Garcia Flores
Grupo: 2-2
Fecha: 09/01/2024

descripcion:
este prgrama muestra un manejo basico de arvhicos de texto texto
'''
import os
os.system("CLS")
print("crear un archivo: ")
print("8================D")
NOMBRE_ARCHIVO = 'datos.txt'
try:
    archivo = open (NOMBRE_ARCHIVO, 'w')   #habre el archivo datos.txt     #open sirve para tener un contenedor de archivo
    archivo.write("esto es una prueba \ny otra prueba.\n")
    archivo.write("Hola ¿como estas?\n")
    archivo.write("Consejo ¿millonario o 100 pesos?\n")
    
    archivo.close()
except Exception as ex:
    print("No se puede crear el archivo", ex)

if NOMBRE_ARCHIVO in os.listdir('.'):
    print(f"archivo creado en la ruta : {os.getcwd()}\\{NOMBRE_ARCHIVO}")
else:
    print("el archivo no fue creado")

print("\n leer un archivo: ")
print("====================")
archivo = open (NOMBRE_ARCHIVO, 'r')   #r=read
contenido = archivo.read()
print(contenido)
archivo.close()


print("\nIterar en un archivo: ")
print("========================")
archivo = open(NOMBRE_ARCHIVO, 'r')
for linea in archivo:
    print(linea)
archivo.close()


print("\nEliminar un archivo despues de la pausa ")
print("========================")
os.system("pause")
os.remove(os.getcwd()+"/"+NOMBRE_ARCHIVO) #concatenar
#os.remove(f"{os.getcwd()}/{NOMBRE_ARCHIVO}") #concatenar
print(f"Eliminando archivo desde la ruta: {os.getcwd}//{NOMBRE_ARCHIVO}")


