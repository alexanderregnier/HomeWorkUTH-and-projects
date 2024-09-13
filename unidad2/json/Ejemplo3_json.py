#Sadrach juan diego Garcia flores
#Grupo TIDSM 2-2
#08/02/24
import os
import json

# Forma 3 de tener un json-. apartir de la clase JSONEncoder().
os.system("CLS")

#                                                       0          1           2
datos_json = json.JSONEncoder().encode({"languages":["spanish", "english", "French"]})

print(datos_json)
print("Datos_json es", type(datos_json))

print("\nCon JSONDecoder( podemos volcar el json a un diccionario:)")
dicc = json.JSONDecoder().decode(datos_json)

print(dicc)
print("Datos_json es ", type(dicc))

try:
    print(dicc['languages'][3])
except:
    print("no exsiste el idioma")
