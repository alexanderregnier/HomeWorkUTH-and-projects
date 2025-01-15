from collections import Counter
import re

# # Lista de elementos
# lista = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'manzana']
# conteo = Counter(lista)
# print(conteo)

text = """
Más que amor, lo que siento por ti. Es el mal del animal, no la terquedad del jabalí, ni la furia del chacal... Es el alma que se encela con instinto criminal, es amar, hasta que duela como un golpe de puñal... ay amor, ay dolor... yo te quiero con alevosía... Necesito confundir tu piel con el frío del metal o tal vez con el destello cruel de un fragmento de cristal... Quiero que tus sentimientos sean puro mineral polvo de cometa al viento del espacio sideral... ay amor, ay dolor... yo te quiero con alevosía.
"""

words = re.findall(r'\b\w+\b', text.lower())

word_freq = Counter(words)

sorted_word_freq = sorted(word_freq.items())

sorted_word_freq

print("Palabras   →    Veces")
print("=====================")
for palabra, veces in sorted_word_freq:
    print(f"{palabra:<12} -> {veces:.2f}")