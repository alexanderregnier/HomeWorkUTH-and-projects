#Sadrach juan diego Garcia flores
#Grupo TIDSM 2-2
#02/02/24
import os
import json

#Formaa 2 de tener JSON.- A partir de un diccionario de datos

datos_dic = {
    "youtuber": "WACHI WACHI WA",
    "Nombre": "Sadrach Juan Diego",
    "Apellido": "Garcia Flores",
    "email": "Jdiego0805@gmail.com",
    "Cursos":["php","Python", "JavaScript", "C#", "Node.js"]
    # ↑ JSON admite listas dentro.
}

os.system("CLS")
#Datos_json = json.dumps(datos_dic, ensure_ascii = False)  #VOLVAR EL CONTENIDO EN UN JSON
#Datos_json = json.dumps(datos_dic, indent=4, ensure_ascii = False)
#Datos_json = json.dumps(datos_dic, indent=4, separators=(", ", ":  "), ensure_ascii = False)
Datos_json = json.dumps(datos_dic, indent=4, separators=(", ", ":  "), sort_keys= True, ensure_ascii = False)

print(Datos_json)
print(type(Datos_json))
print("recuerda: ↑ un json en python se almacena momentanemente en una str para darle tratamiento")



# para los diccionario se usa siempre los {}