#Sadrach juan diego Garcia flores
#Grupo TIDSM 2-2
#01/02/24

import os
import json

#Formaa 1 de tener un objeto JSON.- A partir de una String(STR)

Json_str = '{"nombre":"Sadrach Juan Diego", "Apellido": "Garcia Flores", "pais":"Mexico"}'
#↑ Esta variable es de tipo str pero su contenido es un JSON, porque el contenido esta en el formato JSON

os.system("CLS")
print(Json_str)
print(type(Json_str))
print("    ↑ es una str conteniendo un JSON")

print("\n-————————————————————————————————————")
dicc = json.loads(Json_str) #convertimos un str en un diccionario de python
print(dicc)
print(type(dicc))
print("    ↑ es un diccionario de python")

print("\nComo dicc ya es un diccionario, podemos acceder a los valores asi:")
print(dicc["nombre"])     #print(dicc.get('nombre'))
print(dicc["Apellido"])
print(dicc["pais"])

'''
json.loads(s) Deseraliza s un objeto python mediante la siguiente tabla de conversion*
            s puede ser una instancia de str, bytes o batearray que contiene un documenti json

*   python | JSON
    dict    <->  objeto
    list    <->  Array
    tuple   <->  Array
    str     <->  String
    int     <->  Number
    float   <->  Number
    true    <->  true
    false   <->  false
    none    <->  null
'''