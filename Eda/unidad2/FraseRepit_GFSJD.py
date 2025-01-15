# Elaborar un programa al que se le introduzca un párrafo completo (mínimo 20 palabras), y meta las palabras en una lista sin
# símbolos ortográficos. Después hay que imprimir la lista con cada una de las palabras que ingresó en orden alfabético, y 
# cuántas veces está repetida. 

from MisFunciones_2024 import *

Cls()

frase = input("Escribe una frase: ").lower()
SigPun = "*/?!.,;:[]{}'\"@?¡=*¨()¿.+-=<>_$&%#"
# frase = "Más que amor, lo que siento por ti. Es el mal del animal, no la terquedad del jabalí, ni la furia del chacal... Es el alma que se encela con instinto criminal, es amar, hasta que duela como un golpe de puñal... ay amor, ay dolor... yo te quiero con alevosía... Necesito confundir tu piel con el frío del metal o tal vez con el destello cruel de un fragmento de cristal... Quiero que tus sentimientos sean puro mineral polvo de cometa al viento del espacio sideral... ay amor, ay dolor... yo te quiero con alevosía.".lower()

# Separar puntos como el * / ? etc y colocarlos como una palabra separada
for e in SigPun:
    frase = frase.replace(e, " ")

Lista = frase.split()

frecuencias = {}

# Contar las palabras
for palabra in Lista:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

# Mostrar las palabras y sus frecuencias
Cls()
print("Palabras   →    Veces")
print("=====================")
for palabra, count in sorted(frecuencias.items()):
    print(f"{palabra[0:20]:<12} -> {count:5,.2f}")
pausa()
Cls()

pausa_final()