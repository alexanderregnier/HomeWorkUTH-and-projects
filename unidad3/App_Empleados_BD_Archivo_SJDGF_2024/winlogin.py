from mis_funciones import geometryCentrado
from cls_BD_MySQL import *

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb
import tkinter.font as tkFont
import globales as gb


TITLE_HERE = gb.APP_NAME

class WinLogin:
    def __init__(self) -> None:
        self.__login_granted = False

        loginTk = Tk()
        loginTk.title(TITLE_HERE)
        loginTk.geometry(geometryCentrado(loginTk, 400, 220))
        loginTk.resizable(width=False, height=False)

        #───────────────────────── FUENTES ─────────────────────────
        fnArial16Bold = tkFont.Font(family="Arial", size=16, weight="bold" )
        fnSize12 = tkFont.Font(size=12)
        fnBold = tkFont.Font(weight="bold")
        fnSize12Bold = tkFont.Font(size=12, weight="bold")

        #───────────────────────── ESTILOS ─────────────────────────
        s1 = ttk.Style().configure( 'TButton', font = fnBold )
        stAceptar = ttk.Style().configure("Aceptar.TButton", background ="#00FF00")
        stCancelar = ttk.Style().configure("Cancelar.TButton", background="#FF0000")

        user_sv = StringVar()
        password_sv = StringVar()

        ttk.Label(loginTk, text="Introduzca sus datos", font=fnArial16Bold).place(x=85, y=10)
        lb1 = ttk.Label(loginTk, text="Usuario:", font=fnSize12).place(x=20, y=60)
        entryUser = ttk.Entry(loginTk, width=25, font=fnSize12, textvariable=user_sv)
        entryUser.place(x=130, y=60)

        lb2 = ttk.Label(loginTk, text="Contraseña:", font=fnSize12).place(x=20, y=100)
        entryPassword = ttk.Entry(loginTk, width=25, font=fnSize12Bold, textvariable=password_sv, show="•")
        entryPassword.place(x=130, y=100)

        self.btnAceptar = ttk.Button(loginTk, text="Aceptar", style="Aceptar.TButton", command=lambda: self.__validateUser(loginTk,user_sv.get().strip(), password_sv.get().strip()))
        self.btnAceptar.place(x=40, y=160, width=140, height=40)
        btnCancelar = ttk.Button(loginTk, text="Cancelar", style="Cancelar.TButton", command=loginTk.destroy)
        btnCancelar.place(x=220, y=160, width=140, height=40)

        loginTk.bind('<Return>', lambda e: self.__validateUser(loginTk, user_sv.get().strip(), password_sv.get().strip()))
        loginTk.bind("<Escape>", lambda e: loginTk.destroy())
        loginTk.focus_force()
        entryUser.focus()
        loginTk.mainloop()

    def __validateUser(self, master_win:Tk, nombre_:str, password_:str):
        if nombre_ == "" or password_== "":
            msb.showinfo(TITLE_HERE, "usuario y contraseña son obligatorios")
        else:
            password_ = self.__cleanVariable(password_)
            query = f"SELECT * FROM usuarios WHERE nombre='{nombre_}' AND password=MD5('{password_}');"
            regUsuario = gb.LABD.consultar(query)
            if regUsuario == []:
                msb.showerror(TITLE_HERE, "El usuario no pudo ser auteticado.")
            else:
                msb.showinfo(TITLE_HERE, f"Acceso correcto para usuario {nombre_}.")
                self.__login_granted = True
                master_win.destroy()

    def __cleanVariable(self, var:str) -> str:
        ''' Limpia la variable de caracteres indeseables como: ' = " .'''
        chars_to_eliminate = "'=\"()"
        for c in chars_to_eliminate:  var = var.replace(c,"")
        var = var.replace(" or ","")
        var = var.replace(" OR ","")
        return var
    
    def loginGranted(self) -> bool:
        ''' Devuelve: 
        - True si la autenticación del usuario es correcta. 
        - False si no. '''
        return self.__login_granted