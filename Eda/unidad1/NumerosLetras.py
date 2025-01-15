# sadrach Juan diego garcia flores
# grupo: 4-2
# fecha: 03/09/2024

import os
import sys

os.system('cls')
def leer(msj:str):
    while True:
        try:
            numero = int(input(msj))
            if  0 <= numero <= 999:
                return numero
            else:
                print("asi no mijito, del 0 al 999")
        except:
            print("NO NO asi no.")
            sys.exit("bye bye")

while True:
    cantidad = leer("Dame un numero del 0 al 999: ")
    os.system('cls')

    centenas = (cantidad%1000-cantidad%100)//100
    decenas = (cantidad%100-cantidad%10)//10
    unidades = cantidad%10

    if centenas > 0:
        if centenas == 9:
            buena1 =("Novecientos")
        elif centenas == 8:
            buena1 =("Ochocientos")
        elif centenas == 7:
            buena1 =("Setecientos")
        elif centenas == 6:
            buena1 =("Seisientos")
        elif centenas == 5:
            buena1 =("Quinientos")
        elif centenas == 4:
            buena1 =("Cuatrocientos")
        elif centenas == 3:
            buena1 =("tresientos")
        elif centenas == 2:
            buena1 =("docientos")
        elif centenas == 1 and decenas == 0 and unidades == 0:
            buena1 = "cien"
        elif centenas == 1:
            buena1 =("ciento")
    else:
        buena1 = ""
    if decenas > 0:
        if decenas == 9 and unidades == 0:
            buena2 =("Noventa")
        elif decenas == 9:
            buena2 =("Noventa y")
        elif decenas == 8 and unidades == 0:
            buena2 =("Ochenta")
        elif decenas == 8:
            buena2 =("Ochenta y")
        elif decenas == 7 and unidades == 0:
            buena2 =("setenta")
        elif decenas == 7:
            buena2 =("setenta y")
        elif decenas == 6 and unidades == 0:
            buena2 =("sesenta")
        elif decenas == 6 and unidades == 0:
            buena2 =("sesenta")
        elif decenas == 6:
            buena2 =("Sesenta y")
        elif decenas == 5 and unidades == 0:
            buena2 =("cincuenta")
        elif decenas == 5:
            buena2 =("cincienta y")
        elif decenas == 4 and unidades == 0:
            buena2 =("cuarenta")
        elif decenas == 4:
            buena2 =("Cuarenta y")
        elif decenas == 3 and unidades == 0:
            buena2 =("treinta")
        elif decenas == 3:
            buena2 =("treinta y")
        elif decenas == 2 and unidades == 0:
            buena2 =("veinte")
        elif decenas == 2:
            buena2 =("veinti")
        if decenas == 1 and unidades == 1:
            buena2 = ("once")
        elif decenas == 1 and unidades == 2:
            buena2 = ("Doce")
        elif decenas == 1 and unidades == 3:
            buena2 = ("trece")
        elif decenas == 1 and unidades == 4:
            buena2 = ("catorce")
        elif decenas == 1 and unidades == 5:
            buena2 = ("quince")
        elif decenas == 1 and unidades == 0:
            buena2 =("diez")
        elif decenas == 1:
            buena2 =("diez y")
    else:
        buena2 = ""
    if unidades> 0:
        if unidades == 9:
            buena3 =("Nueve")
        elif unidades == 8:
            buena3 =("Ocho")
        elif unidades == 7:
            buena3 =("Siete")
        elif unidades == 6:
            buena3 =("Seis")
        elif unidades == 5 and decenas == 1:
            buena3 = ("")
        elif unidades == 5:
            buena3 =("cinco")
        elif unidades == 4 and decenas == 1:
            buena3 = ("")
        elif unidades == 4:
            buena3 =("Cuatro")
        elif unidades == 3 and decenas == 1:
            buena3 = ("")
        elif unidades == 3:
            buena3 =("tres")
        elif unidades == 2 and decenas == 1:
            buena3 =("")
        elif unidades == 2:
            buena3 =("dos")
        elif unidades == 1 and decenas == 1:
            buena3 =("")
        else:
            buena3 =("uno")
    else:
        buena3 =("")
    print(f"{buena1} {buena2} {buena3}".strip())
    os.system('pause')