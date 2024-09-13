#Sadrach juan diego Garcia flores
#Grupo TIDSM 2-2
#09/02/24
import os
import json

# Forma 3 de tener un json-. apartir de una clase propia .
os.system("CLS")

class curso:
    def __init__(self, Codigo:str, Nombre:str, Creditos:int) -> None:
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Creditos = Creditos

#----------------------------------------------------------------------------
curso1 = curso("c128", "Fundamnetos de matematica", 5)
print(curso.__dict__)
print(type(curso.__dict__))
print()

Datos_json = json.dumps(curso1.__dict__, ensure_ascii = False)
print(Datos_json)
print("Datos_json es:", type(Datos_json))

print("Nombre del curso:", curso1.__dict__['Nombre'])
# print("Nombre del curso:", Datos_json['Nombre']) #No funciona, porque datos_json es un str.