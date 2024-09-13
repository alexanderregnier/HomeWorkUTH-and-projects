#Autor: Sadrach Juan Diego Garcia Flores
#grupo: tids2-2

from mis_funciones import Cls
from cls_BD_MySQL import *
from winlogin import *
from MainWin import *
from WinUsuarios import *

import globales as gb

MODO = 1# Modo1: Acceso con logon // Cualquier otro valor : Acceso directo sin LogIn

class main:
    def __init__(Self) -> None:
        if MODO ==1:
            if gb.LABD.conectar():
                print("La conexion fue exitosa")
            else:
                exit("no se logro conectar. Fin del programa")

            acceso = WinLogin()
            if acceso.loginGranted():
                MainWin()
        else:
                MainWin()
                #WinUsuarios(Tk())

#───────────────────────────────────────────────────────────────────────────────
Cls()
main()