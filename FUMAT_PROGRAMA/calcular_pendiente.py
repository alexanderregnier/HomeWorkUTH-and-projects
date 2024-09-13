import math
import sympy as sp
from mis_funciones import *
from tkinter import messagebox as msg
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

Cls
while True:
        print("——————— MENU DE OPCIONES ———————")
        print("1.- Calcular pendiente.")
        print("2.- calcular punto medio.")
        print("3.- Parabola.")
        print("4.- circunferencia.")
        print("5.- calcular cir. con diametro y punto medio.")
        print("6.- Hiperbola")
        print("7.- Elipse")
        print("8.- como resolver las formulas Generales a canonicas")
        print("9.- de fraccion a numero real")
        print("10.- SALIR.")
        opcion = leer_entero("\nTeclee la opcion deseada: ")

        match opcion:
            case 1: #PENDINTE
                def calcular_pendiente():
                    try:
                        x1 = float(input("Ingrese la coordenada x1: "))
                        y1 = float(input("Ingrese la coordenada y1: "))
                        x2 = float(input("Ingrese la coordenada x2: "))
                        y2 = float(input("Ingrese la coordenada y2: "))

                        pendiente = (y2 - y1) / (x2 - x1)
                        print("Pendiente={pendiente}")
                        return pendiente, x1, y1
                    except ZeroDivisionError:
                        print("Divisi0n por cero error")
                        return None, None, None
                    except ValueError:
                        print("Entrada invalida. Ingrese numeros validos.")
                        return None, None, None

                def calcular_y2(x2, x1, y1, m):
                    y2 = m * (x2 - x1) + y1
                    return y2

                pendiente_resultado, x1, y1 = calcular_pendiente()

                if pendiente_resultado is not None:
                    x2 = float(input("Ingrese el valor de x2 para calcular y2: "))
                    y2_calculado = calcular_y2(x2, x1, y1, pendiente_resultado)

                    print(f"Para x2={x2}, y2 calculado es: {y2_calculado}")
                pausa()

            case 2: #DISTANCIA PUNTO A UNA RECTA
                def distanciaPuntoRecta(x_punto, y_punto, a_recta, b_recta, c_recta):
                    try:
                        numerador = abs(a_recta * x_punto + b_recta * y_punto + c_recta)
                        denominador = math.sqrt(a_recta**2 + b_recta**2)
                        
                        distancia = numerador / denominador
                        return distancia
                
                    except ZeroDivisionError:
                        print("Division por cero error")
                        return None
                    except ValueError:
                        print("Entrada invalida. Ingrese numeros validos.")
                        return None
                    
                x_punto = float(input("Ingrese la coordenada 'X' del punto: "))
                y_punto = float(input("Ingrese la coordenada 'Y' del punto: "))
                a_recta = float(input("Ingrese el coeficiente 'A' de la recta: "))
                b_recta = float(input("Ingrese el coeficiente 'B' de la recta: "))
                c_recta = float(input("Ingrese el termino independiente 'C' de la recta: "))
                
                distancia = distanciaPuntoRecta(x_punto, y_punto, a_recta, b_recta, c_recta)
                print(f"La distancia entre el punto y la recta es: {distancia}")
                pausa()

            case 3: #PARABOLA
                def parabola():
                    Respuesta = input("La X esta primero o en segundo? (si x^2 sera arriba y abajo) (si y^2 sera a los lados) (1/2)").lower()
                    numero = float(input("Ingrese h: "))
                    numero2 = float(input("Ingrese k: "))
                    numero3 = float(input("Ingrese p: "))
                    if Respuesta == '1':
                        if numero3 > 0:
                            h = -numero
                            k = -numero2
                            p = (numero3 / 4)
                            PO = p * 2

                            focoX = h
                            focoY = k + p
                            directriz = k - p

                            print(f"Vertice=({h},{k})")
                            print(f"p=({p})")
                            print(f"Lr={PO}")
                            print(f"Foco=({focoX}, {focoY})")
                            print(f"Directriz = {directriz}")

                            x = np.linspace(h - 10, h + 10, 400)
                            y = ((x - h)**2) / (4 * p) + k

                            plt.plot(x, y, label='Parábola')
                            plt.scatter(focoX, focoY, color='red', label='Foco')
                            plt.axhline(y=directriz, color='green', linestyle='--', label='Directriz')
                            plt.axvline(x=h, color='blue', linestyle='--', label='Eje de simetría')
                            plt.scatter(h, k, color='orange', label='Vértice')
                            plt.xlabel('X')
                            plt.ylabel('Y')
                            plt.title('Gráfico de la parábola')
                            plt.legend()
                            plt.grid(True)
                            plt.show()
                        else:
                            h = -numero
                            k = -numero2
                            p = (numero3 / -4)

                            focoX = h
                            focoY = k - p
                            directriz = k + p
                            PO = p * 2

                            print(f"Vertice=({h},{k})")
                            print(f"p=({p})")
                            print(f"Foco=({focoX}, {focoY})")
                            print(f"Lr={PO}")
                            print(f"Directriz = {directriz}")
                            print("Abre abajo")

                            x = np.linspace(h - 10, h + 10, 400)
                            y = ((x - h)**2) / (-4 * p) + k

                            plt.plot(x, y, label='Parábola')
                            plt.scatter(focoX, focoY, color='red', label='Foco')
                            plt.axhline(y=directriz, color='green', linestyle='--', label='Directriz')
                            plt.axvline(x=h, color='blue', linestyle='--', label='Eje de simetría')
                            plt.scatter(h, k, color='orange', label='Vértice')
                            plt.xlabel('X')
                            plt.ylabel('Y')
                            plt.title('Gráfico de la parábola')
                            plt.legend()
                            plt.grid(True)
                            plt.show()

                    else:
                        if numero3 > 0:
                            h = -numero
                            k = -numero2
                            p = numero3 / 4

                            focoX = h + p
                            focoY = k 
                            directriz = h - p
                            PO = p * 2

                            print(f"Vertice=({h},{k})")
                            print(f"p=({p})")
                            print(f"Lr={PO}")
                            print(f"Foco=({focoX}, {focoY})")
                            print(f"Directriz = {directriz}")

                            x = np.linspace(k - 5, k + 5, 400)
                            y = p * (x - k)**2 + k

                            plt.plot(x, y, label='Parábola')
                            plt.plot(h, k, 'ro', label='Vértice')
                            plt.plot(focoX, focoY, 'go', label='Foco')
                            plt.axvline(x=directriz, color='b', linestyle='--', label='Directriz')  # Aquí se ajusta para una línea horizontal
                            plt.xlabel('y')  # Aquí se ajusta para y en lugar de x
                            plt.ylabel('x')  # Aquí se ajusta para x en lugar de y
                            plt.title('Gráfico de la Parábola')
                            plt.legend()
                            plt.grid(True)
                            plt.axis('equal')
                            plt.show()
                        else:
                            h = -numero
                            k = -numero2
                            p = (numero3 / -4)

                            focoX = h - p
                            focoY = k
                            directriz = h + p
                            PO = p * 2

                            print(f"Vertice=({h},{k})")
                            print(f"p=({p})")
                            print(f"Lr={PO}")
                            print(f"Foco=({focoX}, {focoY})")
                            print(f"Directriz = {directriz}")

                            x = np.linspace(h - 5, h + 5, 400)
                            y = p * (x - h)**2 + k

                            plt.plot(x, y, label='Parábola')
                            plt.plot(h, k, 'ro', label='Vértice')
                            plt.plot(focoX, focoY, 'go', label='Foco')
                            plt.axvline(x=directriz, color='b', linestyle='--', label='Directriz')
                            plt.xlabel('x')
                            plt.ylabel('y')
                            plt.title('Gráfico de la Parábola')
                            plt.legend()
                            plt.grid(True)
                            plt.axis('equal')
                            plt.show()
                    pausa()
                parabola()

            case 4: #CIRCUNFERENCIA
                def circunferencia():
                    centro = input("Tienes el centro?: (Si/No)").lower()
                    RadCuad = input("El radio esta al cuadrado? (Si/No)").lower()

                    if centro == 'si':
                        CX = float(input("ingrese cordenada H: "))
                        CY = float(input("ingrese cordenada K: "))

                        if RadCuad == 'si':
                            RadCuadCir = float(input("ingrese el radio al cuadrado de la circunferencia: "))
                            diametro = RadCuadCir*2
                            print(f"la ecuacion canonica es: (x{CX})^2+(y{CY})^2={RadCuadCir}(si no tiene signo es +)")
                            print(f"El Radio es :{RadCuadCir}")
                            print(f"El diametro es :{diametro}")
                        else:
                            RadCuadCir = float(input("ingrese el radio que NO esta al cuadrado de la circunferencia: "))
                            YaRaiz = math.sqrt(RadCuadCir)
                            diametro = YaRaiz*2
                            print(f"la ecuacion canonica es: (x{CX})^2+(y{CY})^2={YaRaiz} (si no tiene signo es +)")
                            print(f"El Radio es :{YaRaiz}")
                            print(f"El diametro es :{diametro}")

                    else:
                        CX = float(input("ingrese cordenada H: "))
                        CY = float(input("ingrese cordenada K: "))

                        CentroX = -CX
                        CentroY = -CY

                        if RadCuad == 'si':
                            RadCuadCir = float(input("ingrese el cuadrado del radio de la circunferencia: "))
                            diametro = RadCuadCir*2
                            print(f"la ecuacion canonica es: (x{CX})^2+(y{CY})^2={RadCuadCir} (si no tiene signo es +)")
                            print(f"El Radio es :{RadCuadCir}")
                            print(f"El diametro es :{diametro}")
                            print(f"El centro de la circunferencia es:(X,Y) {CentroX, CentroY}")
                        else:
                            RadCuadCir = float(input("ingrese el radio de la circunferencia: "))
                            YaRaiz = math.sqrt(RadCuadCir)
                            diametro = YaRaiz*2
                            print(f"la ecuacion canonica es:(x{CX})^2+(y{CY})^2={YaRaiz} (si no tiene signo es +)")
                            print(f"El Radio es :{YaRaiz}")
                            print(f"El diametro es :{diametro}")
                            print(f"El centro de la circunferencia es:(X,Y) {CentroX, CentroY}")
                    pausa()
                circunferencia()

            case 5: #DIAMETRO DE LA CIRCUNFERENICA PUNTO MEDIO Y RADIO Y CENTRO
                def diametro_circunferencia():
                    x1 = float(input("Ingrese la coordenada x1: "))
                    y1 = float(input("Ingrese la coordenada y1: "))
                    x2 = float(input("Ingrese la coordenada x2: "))
                    y2 = float(input("Ingrese la coordenada y2: "))

                    CenX = (x1 + x2)/2 
                    CenY = (y1 + y2)/2

                    X = (CenX - x1)**2
                    Y = (CenY + y2)**2

                    d = X + Y
                    Raiz = math.sqrt(d)

                    d1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                    print(f"distancia o P: {d1}")
                    print(f"El radio es: {Raiz} o √{d}")
                    print(f"punto medio o centro de la circunferencia es:({CenX},{CenY})")
                    pausa()
                diametro_circunferencia()

            case 6: #HIPERBOLA
                def hiperbola():
                    Respuesta3 = input("La ecuacion esta en (0,0)? (Si/No)").lower()
                    Respuesta2 = input("cual es positivo?:(donde se ubica el +) (X/Y)").lower()
                    Respuesta = input("La A y B tienen el ^2?: (Si/No)").lower()
                    A = float(input("escribe la a: ")) #9
                    B = float(input("escribe la b: ")) #4
                    
                    if Respuesta3 == "si":    
                        if Respuesta2 == "x":
                            if Respuesta == "si":

                                C2 = A**2 + B**2 
                                Pita = math.sqrt(C2)
                                L = B**2 
                                L2 = 2 * L 
                                LR = L2 / A
                                juan = -A
                                juanita = -B
                                PitaN = -Pita
                                LRD = LR / 2
                                Excentricidad = Pita / A

                                print("Esta hiperbola es hacia Derecha y izquierda")
                                print(f"los resultados son:\na={A}\nb={B}\nc={Pita}\nLR={LR} y {LRD} de cada lado de f y f'")
                                print(f"para las X:\nV=({A},0)\nv'=({juan},0)")
                                print(f"El f=({Pita},0) y f'=({PitaN},0)")
                                print(f"Se ubica en el eje Y:\n ({B},0) ({juanita},0) ponlo al lado de V y V' tambien")
                                print(f"Excentricidad: {Excentricidad}")
                            else:
                                RaizA = math.sqrt(A) #4
                                RaizB = math.sqrt(B) #3

                                C2 = A + B 
                                Pita = math.sqrt(C2)
                                LR = (2 * B) / RaizA
                                juan = -RaizA
                                juanita = -RaizB
                                PitaN = -Pita
                                LRD = LR / 2
                                Excentricidad = Pita / RaizA

                                print("Esta hiperbola es hacia arriba y abajo")
                                print(f"los resultados son:\na={RaizA}\nb={RaizB}\nc={Pita}\nLR={LR} O {LRD} de cada lado de f y f'")
                                print(f"Para las X:\nV=({RaizA},0)\nv'=({juan}.0)")
                                print(f"El f={Pita} y f'={PitaN}")
                                print(f"Se ubica en el eje X:\n ({RaizB},0) ({juanita},0) ponlo al lado de V y V' tambien")
                                print(f"Excentricidad: {Excentricidad}")
                        else:
                            if Respuesta == "si":
                                # a y c = Y   b = X             a = v   b =         c = 
                                C2 = A**2 + B**2  # A=9 B=4  == 13
                                Pita = math.sqrt(C2)
                                L = B**2 #4
                                L2 = 2 * L #8
                                LR = L2 / A
                                juan = -Pita
                                juanita = -B
                                PitaN = -Pita
                                LRD = LR / 2
                                Excentricidad = Pita / A

                                print("Esta hiperbola es hacia arriba y abajo")
                                print(f"los resultados son:\na={A}\nb={B}\nc={Pita}\nLR={LRD} de cada lado de f y f'")
                                print(f"V=(0,{A})\nv'=(0,{juan})")
                                print(f"El f=(0,{Pita}) y f'=(0,{PitaN})")
                                print(f"Se ubica en el eje X:\n ({B},0) ({juanita},0) ponlo al lado de V y V' tambien")
                                print(f"Excentricidad: {Excentricidad}")

                            else: #PARA LA ECUACION     y^2/a - x^2/b       para pasar de a = a^2       Ejemplo 9 = 3^2
                                RaizA = math.sqrt(A) #3
                                RaizB = math.sqrt(B) #2

                                # a y c = Y   b = X             a = v   b =         c = 
                                C2 = A + B  # A=9 B=4  == 13
                                Pita = math.sqrt(C2)
                                LR = (2 * B) / RaizA
                                juan = -RaizA
                                juanita = -RaizB
                                PitaN = -Pita
                                LRD = LR / 2
                                Excentricidad = Pita / RaizA

                                print("Esta hiperbola es hacia arriba y abajo")
                                print(f"los resultados son:\na={RaizA}\nb={RaizB}\nc={Pita}\nLR={LRD} de cada lado de f y f'")
                                print(f"V=(0,{RaizA})\nv'=(0,{juan})")
                                print(f"Se ubica en el eje y:\n (0,{RaizA}) (0,{juan}) ponlo al lado de V y V' tambien")
                                print(f"El f={Pita} y f'={PitaN}")
                                print(f"Excentricidad: {Excentricidad}")
                    else:
                        h = float(input("ingresa H:el que acompaña a x: "))#-4
                        k = float(input("ingresa K:el que acompaña a y: "))#2

                        if Respuesta2 == "x":
                            if Respuesta == "si":
                                h1 = -h
                                k1 = -k

                                C2 = A + B  # A=9 B=25  == 35
                                Pita = math.sqrt(C2) #5.8
                                LR = (2 * B) / RaizA
                                LRD = LR / 2
                                cen = h1 - RaizA
                                cenP = h1 + RaizA
                                f1 = h1 - Pita
                                f2 = h1 + Pita
                                Excentricidad = Pita / A

                                print(f"El Centro esta en :(x,y) ({h1},{k1})")
                                print(f"los resultados son:\na={RaizA}\nb={RaizB}\nc={Pita}\nLR={LR} y {LRD} de cada lado de f y f'")
                                print(f"Para las X:\nV=({cen},{k1})\nv'=({cenP},{k1})")
                                print(f"El foco es:\nf=({f1},{k1})\nf'=({f2},{k1})")
                                print(f"Excentricidad: {Excentricidad}")
                            else:
                                h1 = -h
                                k1 = -k

                                RaizA = math.sqrt(A) #a=9   raiz = 3
                                RaizB = math.sqrt(B) #b=25   raiz = 5
                                C2 = A + B  # A=9 B=25  == 35
                                Pita = math.sqrt(C2) #5.8
                                LR = (2 * B) / RaizA
                                LRD = LR / 2
                                cen = h1 - RaizA
                                cenP = h1 + RaizA
                                f1 = h1 - Pita
                                f2 = h1 + Pita
                                Excentricidad = Pita / RaizA

                                print(f"El Centro esta en :(x,y) ({h1},{k1})")
                                print(f"los resultados son:\na={RaizA}\nb={RaizB}\nc={Pita}\nLR={LR} y {LRD} de cada lado de f y f'")
                                print(f"Para las X:\nV=({cen},{k1})\nv'=({cenP},{k1})")
                                print(f"El foco es:\nf=({f1},{k1})\nf'=({f2},{k1})")
                                print(f"Excentricidad: {Excentricidad}")

                        else:
                            if Respuesta == "si":
                                h1 = -h
                                k1 = -k

                                C2 = A + B  # A=25 B=16  == 41
                                Pita = math.sqrt(C2) #6.4
                                LR = (2 * B) / A
                                LRD = LR / 2
                                cen = k1 + A
                                cenP = k1 - A
                                f1 = k1 + Pita
                                f2 = k1 - Pita
                                Excentricidad = Pita / A

                                print(f"El Centro esta en :(x,y) ({h1},{k1})")
                                print(f"los resultados son:\na={A}\nb={B}\nc={Pita}\nLR={LR} y {LRD} de cada lado de f y f'")
                                print(f"Para las Y:\nV=({h1},{cen})\nv'=({h1},{cenP})")
                                print(f"El foco es:\nf=({h1},{f1})\nf'=({h1},{f2})")
                                print(f"Excentricidad: {Excentricidad}")
                            else:
                                h1 = -h
                                k1 = -k

                                RaizA = math.sqrt(A) #a=9   raiz = 3
                                RaizB = math.sqrt(B) #b=25   raiz = 5
                                C2 = A + B  # A=25 B=16  == 41
                                Pita = math.sqrt(C2) #6.4
                                LR = (2 * B) / RaizA
                                LRD = LR / 2
                                cen = k1 + RaizA
                                cenP = k1 - RaizA
                                f1 = k1 + Pita
                                f2 = k1 - Pita
                                Excentricidad = Pita / RaizA

                                print(f"El Centro esta en :(x,y) ({h1},{k1})")
                                print(f"los resultados son:\na={RaizA}\nb={RaizB}\nc={Pita}\nLR={LR} y {LRD} de cada lado de f y f'")
                                print(f"Para las Y:\nV=({h1},{cen})\nv'=({h1},{cenP})")
                                print(f"El foco es:\nf=({h1},{f1})\nf'=({h1},{f2})")
                                print(f"Excentricidad: {Excentricidad}")
                    pausa()
                hiperbola()

            case 7:#ELIPSE
                def Elipse():
                    Respuesta3 = input("El centro esta en (0,0)? (Si/No)").lower()
                    Respuesta2 =input("En donde esta el numero mayor? (X/Y)").lower()
                    Respuesta =input("Estan con el signo de ^2? (Si/No)").lower()
                    a = float(input("Ingrese a:es el mayor "))
                    b = float(input("Ingrese b:es el menor "))

                    if Respuesta3 == "si": #RESPUESTA DE SI ESTA EN EL CENTRO
                        if Respuesta2 == "x":#RESPUESTA X SI NO ENTRA AL SIGUIENTE En donde esta el numero mayor? (X/Y)
                            if Respuesta == "si":# REPSUETA QUE SI A Estan con el signo de ^2? (Si/No)
                                c = a + b
                                c2 = math.sqrt(c)
                                c3 = -c2
                                LR = 2 * b**2 / a
                                LRD = LR / 2
                                AN = -a
                                BN = -b

                                print(f"El centro es: (0,0)")
                                print(f"los resultados son:\na={a}\nb={b}\nc={c2}")
                                print(f"Para las X:\nV={a}\nv'={AN}")
                                print(f"Para las Y:\nV={b}\nv'={BN}")
                                print(f"Para las X:\nF={c2}\nF'={c3}")
                                print(f"Lado recto={LR} y {LRD} arriba y abajo de f y f'")
                                print("Eje mayor X")

                            else: #RESPUESTA NO O OTRA
                                RaizA = math.sqrt(a)
                                RaizB = math.sqrt(b)
                                RaizAN = -RaizA
                                RaizBN = -RaizB
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2
                                LR = 2 * b / RaizA
                                LRD = LR / 2

                                print(f"El centro es: (0,0)")
                                print(f"los resultados son:\na=√{a}={RaizA}\nb={RaizB}\nc={c2}")
                                print(f"Para las X:\nV={RaizA}\nv'={RaizAN}")
                                print(f"Para las Y:\nV={RaizB}\nv'={RaizBN}")
                                print(f"Para las X:\nF={c2}\nF'={c3}")
                                print(f"Lado recto={LR} y {LRD} arriba y abajo de f y f'")
                                print("Eje mayor X")
                        else:#RESPUESTA DE Y O CUALQUIER OTRA A
                            if Respuesta == "si": # RESPUESTA SI A →→→→→→→→→→→→"Estan con el signo de ^2? (Si/No)"
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2
                                LR = 2 * b**2 / a
                                LRD = LR / 2
                                AN = -a
                                BN = -b

                                print(f"los resultados son:\na={a}\nb={b}\nc={c2}")
                                print(f"Para las Y:\nV={a}\nv'={AN}")
                                print(f"Para las X:\nV={b}\nv'={BN}")
                                print(f"Para las Y:\nF={c2}\nF'={c3}")
                                print(f"Lado recto={LR} y {LRD} arriba y abajo de f y f'")
                                print("Eje mayor Y")
                            else:# RESPUESTA DE NO O LO QUE SEA A →→→→→→→→→→→→"Estan con el signo de ^2? (Si/No)"
                                RaizA = math.sqrt(a)
                                RaizB = math.sqrt(b)
                                RaizAN = -RaizA
                                RaizBN = -RaizB
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2
                                LR = 2 * b / RaizA
                                LRD = LR / 2

                                print(f"El centro es: (0,0)")
                                print(f"los resultados son:\na=√{a}={RaizA}\nb={RaizB}\nc={c2}")
                                print(f"Para las X:\nV={RaizA}\nv'={RaizAN}")
                                print(f"Para las Y:\nV={RaizB}\nv'={RaizBN}")
                                print(f"Para las X:\nF={c2}\nF'={c3}")
                                print(f"Lado recto={LR} y {LRD} arriba y abajo de f y f'")
                                print("Eje mayor Y")
                    else:#RESPUESTA DE NO NO NO NO NO ESTA EN EL CENTRO
                        if Respuesta2 == "x":#RESPUESTA X O CUALQUIER OTRA COSA SI NO ENTRA AL SIGUIENTE En donde esta el numero mayor? (X/Y)
                            if Respuesta == "si":# REPSUETA QUE SI A Estan con el signo de ^2? (Si/No)
                                h = float(input("Ingrese h:acompaña x "))
                                k = float(input("Ingrese k:acompaña y "))
                                h1 = -h
                                k1 = -k
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2

                                print(f"El centro es: ({h1},{k1})")
                                print(f"los resultados son:\na={a}\nb={b}\nc={c2}")
                                print(f"Para las Y:\nV={RaizA}\nv'={RaizAN}")
                                print(f"Para las N:\nV={RaizB}\nv'={RaizBN}")
                                print(f"Para las Y:\nF={c2}\nF'={c3}")
                                print("Eje mayor x")
                            else:# REPSUETA QUE NO A Estan con el signo de ^2? (Si/No)
                                h = float(input("Ingrese h:acompaña x "))
                                k = float(input("Ingrese k:acompaña y "))
                                h1 = -h
                                k1 = -k
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2
                                LR = 2 * b**2 / a
                                LRD = LR / 2

                                RaizA = math.sqrt(a)
                                RaizB = math.sqrt(b)
                                RaizAN = -RaizA
                                RaizBN = -RaizB

                                print(f"El centro es: ({h1},{k1})")
                                print(f"los resultados son:\na=√{a}={RaizA}\nb={RaizB}\nc={c2}")
                                print(f"Para las X:\nV={RaizA}\nv'={RaizAN}")
                                print(f"Para las Y:\nV={RaizB}\nv'={RaizBN}")
                                print(f"Para las X:\nF={c2}\nF'={c3}")
                                print(f"Lado recto={LR} y {LRD} arriba y abajo de f y f'")
                                print("Eje mayor X")
                        else:#RESPIUESTA DE Y O OTRA EN "En donde esta el numero mayor? (X/Y)"
                            if Respuesta == "si":# REPSUETA QUE SI A Estan con el signo de ^2? (Si/No)
                                h = float(input("Ingrese h:acompaña x "))
                                k = float(input("Ingrese k:acompaña y "))
                                h1 = -h
                                k1 = -k
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2
                                AN = -a
                                BN = -b

                                print(f"los resultados son:\na={a}\nb={b}\nc={c2}")
                                print(f"Para las X:\nV={a}\nv'={AN}")
                                print(f"Para las Y:\nV={b}\nv'={BN}")
                                print(f"Para las X:\nF={c2}\nF'={c3}")
                                print(f"Lado recto={LR} y {LRD} arriba y abajo de f y f'")
                                print("Eje mayor Y")
                            else:# REPSUETA QUE NO A Estan con el signo de ^2? (Si/No)
                                h = float(input("Ingrese h:acompaña x "))
                                k = float(input("Ingrese k:acompaña y "))
                                h1 = -h
                                k1 = -k
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2

                                RaizA = math.sqrt(a)
                                RaizB = math.sqrt(b)
                                RaizAN = -RaizA
                                RaizBN = -RaizB
                                c = a - b
                                c2 = math.sqrt(c)
                                c3 = -c2
                                LR = 2 * b / RaizA
                                LRD = LR / 2

                                print(f"El centro es: ({h1},{k1})")
                                print(f"los resultados son:\na=√{a}={RaizA}\nb={RaizB}\nc={c2}")
                                print(f"Para las X:\nV={RaizA}\nv'={RaizAN}")
                                print(f"Para las Y:\nV={RaizB}\nv'={RaizBN}")
                                print(f"Para las X:\nF={c2}\nF'={c3}")
                                print(f"Lado recto={LR} y {LRD} arriba y abajo de f y f'")
                                print("Eje mayor Y")

                    pausa()
                Elipse()

            case 8: #DE GENERAL A CANONICAS
                def GeneralCanonica():
                    print("——————— MENU DE OPCIONES ———————")
                    print("1.- general a canonica de circunferencia")
                    print("2.- general a canonica de elipse")
                    print("3.- general a canonica de parabola")
                    print("4.- general a canonica de hiperbola")
                    opcion = leer_entero("\nTeclee la opcion deseada: ")
                    
                    match opcion:
                        case 1:#general a canonica de circunferencia
                            print("para resolver una Euacion general de la circunferencia necesitas saber como se ve una ecuacion general")
                            print("La ecuacion general se mira de esta forma        X^2+Y^2+Dx+Ey+F     ('Las Letras mayusculas se pueden cambiar excepto X y Y')")
                            print("Siempre tiene que estar la X,Y al cuadrado X^2   Y^2")
                            print("Las reglas para que sea una canonica de circunferencia son")
                            print("1.-la X , Y deben de estar al ^2")
                            print("2.-pueden estar acompañadas por un numero SOLO SI ES IGUAL EJEMPLO 5x^2+5x^2")
                            print("3.-si tiene un numero 5x^2+5x^2 si es circunferencia pero no de la forma general")
                            print("4.-X , Y deben de ser positivos")
                            print("5.-debe de ser = 0")
                            print("X^2+Y^2+Dx+Ey+F Si no tiene coeficiente es 1 y si F no tiene es 0 ")
                            print("-(D/2)=h")
                            print("-(E/2)=k")
                            print("r=1/2√D^2+E^2-4F  (si da raiz negativa NO es una circunferencia)")
                            print("\n\nPara volver de canonica a general la formula es:       X^2-2xh+h^2+y^2-2yk^2+k^2-r^2=0")
                            print("primero tiene que estar ordenada Primero la X^2+Y^2")
                            print("segundo -2hX")
                            print("tercero -2kY")
                            print("y por ultimo las variables sin termino osea +h^2+k^2-r^2")
                            print("al final quedaria asi        X^2+Y^2 -2hX^2 -2kY^2 +h^2 +k^2 -r^2 = 0")
                            print("general:\nX^2+Y^2+Dx+Ey+F")
                            print("para volver de canonica a general:\nX^2+Y^2-2hX^2-2kY^2+h^2+k^2-r^2=0")
                            print("D=-2h")
                            print("-(D/2)=h")
                            print("E=-2k")
                            print("-(E/2)=k")
                            print("r=1/2√D^2+E^2-4F  (si da raiz negativa NO es una circunferencia)")
                            print("ya con esto tienes todo para poder grficar (si te da fraccion usa la funcion numero 9 pra volver la fraccion a numero real)")

                        case 2:#general a canonica de elipse
                            print("general:3x2+6y^2-36=0")
                            print("canonica: x^2/a^2+y^2/b^2")
                            print("3x^2+6y^2=36")
                            print("lo divides todo por 36")
                            print("3x^2/36+6y^2/36=1")
                            print("En este ejemplo sacamos tercera de 3x2 para poder obtener un 1x^2 que se puede colocar solamente como x^2 si le sacas tercera u otra la misma le sacas a la de abajo en ele ejemplo seria 36/3=12")
                            print("al igual que con el segund podemos sacar 6ta y termina en 1y^2/6")
                            print("para al final quedar como:")
                            print("x^2/12+y^2/6=1 esta tendria centro en (0,0)")
                            print("40x^2+3y^2-30=0")
                            print("40x^2+3y^2=30")
                            print("40x^2/(30)+3y^2(30)=30/30")
                            print("cuando termine en 40x^2/30 podemos eliminar un cero para que quede como 4x^2/3 y esa ya no se puede simplificar")
                            print("x^2/3+y^2/10=1")
                            print("1/(3/4) es lo mismo que 4/3")
                            print("entonces se baja el 4/3 y quedaria como   x^2/(3/4) se coloca alreves si es 6/5 seria 5/6")
                            print("y al final la formula quedaria como x2/(3/4) + y^2/10")
                            print("x^2/(3/4)+y^2/10=1 (si te da fraccion usa la funcion numero 9 pra volver la fraccion a numero real)")
                            print("\n 4X^2+9Y^2-40x+54y+145")
                            print("Pasamos todas los terminos semejantes a los lados quedaria como:")
                            print("4x2-40x      +9y^2+54y   =-145")
                            print("divides el 40/4 para sacar el 10")
                            print("4(x^2-10x+25) + 9(y^2+6y+9)=-145")
                            print("ahora divides el numero del centro entre 2 y lo elevas al cuadrado ahora multiplicas el numero de fuera por el numero que acabs deobtener ejemplo 4*25=100 y lo colocas al final")
                            print("4(x^2-10x+25) + 9(y^2+6y+9)=-145+100+81")
                            print("bajas el 10/2=5 y lo elevas al cuadrado")
                            print("4(x^2-5x)^2 + 9(y^2+3)=36")
                            print("lo divides por el numero final osea 36 en este caso")
                            print("4(x^2-5x)^2/36 + 9(y^2+3)^2/36=36/36")
                            print("sacas 4 en este caso apra colver el 4 en 1 y el 36 en 9")
                            print("(x^2-5x)^2/9 + (y^2+3)^2/9 = 1")

                        case 3:#general a canonica de parabola
                            print("x^2-6x-8y-7=0")
                            print("si se psa al otro lado del = se cambia el signo en este se cambian Y")
                            print("sacas el tercer dato(9) al sacar la mitad del numeor de enmedio elevarlo al cuadrado")
                            print("x^2-6x+9 = 8y+7+9")
                            print("sumas los datos si x o y y eso lo divides por el numero de fuera en este caso 8")
                            print("(x-3)^2 = 8(y+2)")
                            print("(x-h)^2 = 4p(y-k)")
                            print("(x-h)^2 = -4p(y-k)")
                            print("\ny^2-7x-8y-5=0")
                            print("y^-8y =7x+5")
                            print("y^-8y+16 =7x+5+16")
                            print("(y-4)^2 = 7x+21")
                            print("(y-4)^2 = 7(x+3)")

                        case 4:#general a canonica de hiperbola
                            print("-4x^2+7y^2+8x+42y+31=0")
                            print("Acomodas los terminos X de un lado y Y del otro y pasas el que no tiene afuera el = en su contrario si es + se vuelve - y viseversa")
                            print("-4x^2+8x +7y^2+42y = -31")
                            print("divides todo por el numero de fuera respetando signos")
                            print("-4(x^2-2x+   )+7(y^2+6y+   )=-31")
                            print("divides el numero de enmedio y le sacas al cuadrado y lo multiplicas por el numero de afuera y el resultado lo pones fuera del =")
                            print("-4(x^2-2x+1)+7(y^2+6y+9)=-31-4+63")
                            print("Factorizamos")
                            print("-4(x-1)^2 + 7(y+3)^2=28")
                            print("dividimos todo por el numero de fuera del =")
                            print("-4(x-1)^2/28 + 7(y+3)^2/28=28/28")
                            print("(x-1)^2/7 + (y+3)^2/4=1")
                            print("(y+3)^2/4 - (x-1)^2/7")
                            print("\n8x^2-12y^2+112x+120y-4=0")
                            print("8x^2+112x-12y^2+120y=4")
                            print("8(x^2+14x+  )-12(y^2-10y+  )=4")
                            print("8(x^2+14x+49)-12(y^2+10y+25)=4+392-300")
                            print("8(x+7)^2-12(y-5)^2=96")
                            print("8(x+7)^2/96-12(y-5)^2/96=96/96")
                            print("8(x+7)^2/12-12(y-5)^2/8=1")
                            print("\n Para sacar centro Sacas C=(fx+fx/2) , (fy+fy/2)")
                            print("Longitud distancia entre vertices 2a=x  x/2 = a")
                            print("(x1,y1)-(x2,y2)=C            El primero es f1 y el segundo es Centro")
                            print("b^2=C^2-A^2          pitagoras al cuadrado")
                            print("SOLO OCUPAS A , B Y EL CENTRO PARA SACAR LA FORMULA CANONICA Y CON ESO CAMBIA A LA HIPERBOLA Y SACALO DE ALLI")
                    pausa()
                GeneralCanonica()

            case 9: #pasar de fraccion a numero real
                def fraccion_a_decimal(numerador, denominador):
                    return numerador / denominador

                try:
                    numerador = int(input("Ingresa el numerador de la fracción: "))
                    denominador = int(input("Ingresa el denominador de la fracción: "))
                    
                    if denominador == 0:
                        print("Error: El denominador no puede ser cero.")
                    else:
                        resultado = fraccion_a_decimal(numerador, denominador)
                        print("El resultado de la fracción {}/{} es: {}".format(numerador, denominador, resultado))

                except ValueError:
                    print("Error: Por favor ingresa solo números enteros.")
                pausa()

            case 10:
                print("bye")
                pausa()

            case _:
                BeepError()
                print("La opcion no es valida.")
                pausa()