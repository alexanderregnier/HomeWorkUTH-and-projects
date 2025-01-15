# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 03/09/2024
import os
import sys

def leer(msj:str):
    while True:
        try:
            cantidad = float(input(msj))
            return cantidad
        except:
            print("NO es un numero tontito")
            sys.exit("bye bye")

Resultado = {}
while True:
    os.system('cls')
    cantidad = leer("valor: ")
    billetesMonedas = {
        "Billete(s) de 1000": 1000,
        "Billete(s) de 500": 500,
        "Billete(s) de 200": 200,
        "Billete(s) de 100": 100,
        "Billete(s) de 50": 50,
        "Billete(s) de 20": 20,
        "Moneda(s) de 10": 10,
        "Moneda(s) de 5": 5,
        "Moneda(s) de 2": 2,
        "Moneda(s) de 1": 1,
        "centavo(s) de 0.5": 0.5
    }

    if cantidad < 0:
        print("no")
        os.system('pause')
    else:
        for tipo, valor in billetesMonedas.items():
            cantidad1 = cantidad // valor
            cantidad3 = cantidad % valor
            cantidad %= valor
            Resultado[tipo] = cantidad1

        os.system('cls')
        for tipo, cantidad in Resultado.items():
            if cantidad > 0 :
                print(f"{cantidad} {tipo} ")
        print(f"sobro {cantidad3}")
        os.system('pause')