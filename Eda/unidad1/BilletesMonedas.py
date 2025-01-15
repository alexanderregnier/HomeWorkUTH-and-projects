# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 03/09/2024

import os
os.system('cls')
try:
    cantidad = int(input("valor: "))
except:
    print("NO es un numero tontito")
    quit()

billetesMonedas = {
        "Billete(s) de 500": 500,
        "Billete(s) de 200": 200,
        "Billete(s) de 50": 50,
        "Moneda(s) de 10": 10,
        "Moneda(s) de 5": 5,
        "Moneda(s) de 1": 1,
    }

Resultado = {}

for tipo, valor in billetesMonedas.items():
    cantidad1 = cantidad // valor
    cantidad %= valor
    Resultado[tipo] = cantidad1

os.system('cls')
for tipo, cantidad in Resultado.items():
    if cantidad > 0 : print(f"{cantidad} {tipo}") 