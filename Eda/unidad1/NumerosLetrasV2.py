# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 08/09/2024

import os
import sys

os.system('cls')    

def leer(msj: str):
    while True:
        try:
            numero = int(input(msj))
            if 0 <= numero <= 999:
                return numero
            else:
                print("Así no, mijito. El número debe estar entre 0 y  999.")
        except ValueError:
            print("NO, NO, así no. Debes dar un número válido sonsito.")
            sys.exit("Bye bye")

while True:
    cantidad = leer("Dame un número del 0 al 999: ")
    os.system('cls')

    centenas = (cantidad % 1000 - cantidad % 100) // 100
    decenas = (cantidad % 100 - cantidad % 10) // 10
    unidades = cantidad % 10

    if centenas > 0:
        if centenas == 9:
            buena1 = "Novecientos"
        elif centenas == 8:
            buena1 = "Ochocientos"
        elif centenas == 7:
            buena1 = "Setecientos"
        elif centenas == 6:
            buena1 = "Seiscientos"
        elif centenas == 5:
            buena1 = "Quinientos"
        elif centenas == 4:
            buena1 = "Cuatrocientos"
        elif centenas == 3:
            buena1 = "Trescientos"
        elif centenas == 2:
            buena1 = "Doscientos"
        elif centenas == 1 and decenas == 0 and unidades == 0:
            buena1 = "Cien"
        elif centenas == 1:
            buena1 = "Ciento"
    else:
        buena1 = ""

    if decenas > 0:
        if decenas == 9 and unidades == 0:
            buena2 = "Noventa"
        elif decenas == 9:
            buena2 = "Noventa y  "
        elif decenas == 8 and unidades == 0:
            buena2 = "Ochenta"
        elif decenas == 8:
            buena2 = "Ochenta y  "
        elif decenas == 7 and unidades == 0:
            buena2 = "Setenta"
        elif decenas == 7:
            buena2 = "Setenta y "
        elif decenas == 6 and unidades == 0:
            buena2 = "Sesenta"
        elif decenas == 6:
            buena2 = "Sesenta y "
        elif decenas == 5 and unidades == 0:
            buena2 = "Cincuenta"
        elif decenas == 5:
            buena2 = "Cincuenta y "
        elif decenas == 4 and unidades == 0:
            buena2 = "Cuarenta"
        elif decenas == 4:
            buena2 = "Cuarenta y "
        elif decenas == 3 and unidades == 0:
            buena2 = "Treinta"
        elif decenas == 3:
            buena2 = "Treinta y "
        elif decenas == 2 and unidades == 0:
            buena2 = "Veinte"
        elif decenas == 2:
            buena2 = "Veinti"
        elif decenas == 1 and unidades == 1:
            buena2 = "Once"
        elif decenas == 1 and unidades == 2:
            buena2 = "Doce"
        elif decenas == 1 and unidades == 3:
            buena2 = "Trece"
        elif decenas == 1 and unidades == 4:
            buena2 = "Catorce"
        elif decenas == 1 and unidades == 5:
            buena2 = "Quince"
        elif decenas == 1 and unidades == 0:
            buena2 = "Diez"
        elif decenas == 1:
            buena2 = "Diez y "
    else:
        buena2 = ""

    if unidades > 0:
        if unidades == 9:
            buena3 = "Nueve"
        elif unidades == 8:
            buena3 = "Ocho"
        elif unidades == 7:
            buena3 = "Siete"
        elif unidades == 6:
            buena3 = "Seis"
        elif unidades == 5 and decenas == 1:
            buena3 = ""
        elif unidades == 5:
            buena3 = "Cinco"
        elif unidades == 4 and decenas == 1:
            buena3 = ""
        elif unidades == 4:
            buena3 = "Cuatro"
        elif unidades == 3 and decenas == 1:
            buena3 = ""
        elif unidades == 3:
            buena3 = "Tres"
        elif unidades == 2 and decenas == 1:
            buena3 = ""
        elif unidades == 2:
            buena3 = "Dos"
        elif unidades == 1 and decenas == 1:
            buena3 = ""
        else:
            buena3 = "Uno"
    else:
        buena3 = ""

    resultado = f"{buena1} {buena2}{buena3}".strip()
    print(resultado)
    os.system('pause')