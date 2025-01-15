# Sadrach Juan Diego García Flores
# Grupo: 4-2
# Fecha: 10/09/2024

import os
import sys

os.system('cls')

def leer(msj: str):
    while True:
        try:
            numero = int(input(msj))
            if 0 <= numero <= 999999999999:
                return numero
            else:
                print("Así no, mijito. El número debe estar entre 0 y  999,999,999,999.")
        except ValueError:
            print("NO, NO, así no. Debes dar un número válido sonsito.")
            sys.exit("Bye bye")

def Calcular_1(cantidad):
    if cantidad == 0:
        return "Cero"

    unidades = cantidad % 1000
    miles = (cantidad % 1000000 - unidades) // 1000
    millones = (cantidad % 1000000000 - miles - unidades) // 1000000
    billones = (cantidad - millones - miles - unidades) // 1000000000

    resultado = ""
    
    if billones > 0:
        resultado += Calcular_2(billones) + " mil de millones "
    if millones > 0:
        resultado += Calcular_2(millones) + " Millones "
    if miles > 0:
        if miles == 1:
            resultado += "Mil "
        else:
            resultado += Calcular_2(miles) + " Mil "
    if unidades > 0:
        resultado += Calcular_2(unidades)

    return resultado

def Calcular_2(cantidad):
    if cantidad == 0:
        return "Cero"

    centenas = (cantidad % 1000 - cantidad % 100) // 100
    decenas = (cantidad % 100 - cantidad % 10) // 10
    unidades = cantidad % 10

    # Calcular centenas
    match centenas:
        case 9: buena1 = "Novecientos"
        case 8: buena1 = "Ochocientos"
        case 7: buena1 = "Setecientos"
        case 6: buena1 = "Seiscientos"
        case 5: buena1 = "Quinientos"
        case 4: buena1 = "Cuatrocientos"
        case 3: buena1 = "Trescientos"
        case 2: buena1 = "Doscientos"
        case 1: buena1 = "Cien" if decenas == 0 and unidades == 0 else "Ciento"
        case 0: buena1 = "" 

    # Calcular decenas y numeros especiales
    match decenas:
        case 9: buena2 = "Noventa"
        case 8: buena2 = "Ochenta"
        case 7: buena2 = "Setenta"
        case 6: buena2 = "Sesenta"
        case 5: buena2 = "Cincuenta"
        case 4: buena2 = "Cuarenta"
        case 3: buena2 = "Treinta"
        case 2:
            match unidades:
                case 0: buena2 = "Veinte"
                case _: buena2 = f"Veinti{unidades_si(unidades)}"
        case 1:
            match unidades:
                case 0: buena2 = "Diez"
                case 1: buena2 = "Once"
                case 2: buena2 = "Doce"
                case 3: buena2 = "Trece"
                case 4: buena2 = "Catorce"
                case 5: buena2 = "Quince"
                case _: buena2 = f"Dieci{unidades_si(unidades)}"
        case 0: buena2 = ""
    
    # Calcular unidades
    if decenas not in {1, 2}:
        match unidades:
            case 9: buena3= "nueve"
            case 8: buena3= "ocho"
            case 7: buena3= "siete"
            case 6: buena3= "seis"
            case 5: buena3= "cinco"
            case 4: buena3= "cuatro"
            case 3: buena3= "tres"
            case 2: buena3= "dos"
            case 1: buena3= "uno"
            case 0: buena3= "" if (centenas > 0 or decenas > 0) else "cero"
    else:
        buena3 = ""

    if decenas > 2 and unidades > 0:
        resultado = f"{buena1} {buena2} y {buena3}".strip()
    else:
        resultado = f"{buena1} {buena2}{buena3}".strip()

    return resultado

def unidades_si(unidades, centenas=0, decenas=0):
    match unidades:
        case 9: return "nueve"
        case 8: return "ocho"
        case 7: return "siete"
        case 6: return "seis"
        case 5: return "cinco"
        case 4: return "cuatro"
        case 3: return "tres"
        case 2: return "dos"
        case 1: return "uno"
        case 0: return "" if (centenas > 0 or decenas > 0) else "cero"
        case _: return unidades_si()

while True:
    cantidad = leer("Dame un número del 0 al 999,999,999,999: ")
    os.system('cls')
    resultado2 = Calcular_1(cantidad)
    print(f"{resultado2}")
    os.system('pause')