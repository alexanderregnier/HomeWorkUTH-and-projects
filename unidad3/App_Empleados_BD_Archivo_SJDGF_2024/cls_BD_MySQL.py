'''
Archivo: cls_BD_MySQL.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 16-marzo-2022

Objetivo: Proporcionar una clase para gestionar la conexión a MySQL.
'''
import mysql.connector

class BD_MySQL():
    def __init__(self, user:str, password:str, host:str, database:str, port=3306 ) -> None:
        # self.cnx = mysql.connector.connect()
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database


    def conectar(self, print_exception:bool = True):
        ''' Devuelve True si la conexión tiene éxito, False si no. \n
        Si print_exception es False no se mostrará en pantalla el mensaje de la Exception devuelta 
        por el DMBS. '''
        try:
            self.cnx = mysql.connector.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port, 
                database = self.database )
            return True
        except Exception as ex:
            if print_exception:  print(ex)
            return False
        
        
    def consultar(self, query:str):
        ''' Ejecutar Consultas tipo SELECT que devuelvan 0 o más registros. '''
        try:
            self.conectar()
            cursor = self.cnx.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            self.cnx.close()
            return resultado    # resultado va a ser una lista de python
        except Exception as e:
            print(e)
            return []   # lista vacía


    def consultarFunc(self, query:str):
        ''' Ejecutar Consultas tipo SELECT <FUNCIÓN> que devuelvan 1 valor numérico, por ejemplo:  
            - SELECT COUNT(*) FROM empleados; 
            - SELECT SUM(importe) FROM facturas; '''        
        try:
            self.conectar()
            cursor = self.cnx.cursor()
            cursor.execute(query)
            resultado = cursor.fetchone()
            self.cnx.close()
            return resultado[0]    # resultado[0] va a ser un dato simple de python (int o float)
        except Exception as e:
            print(e)
            return None


    def ejecutar(self, query:str):
        ''' Ejecutar Consultas tipo INSERT, UPDATE o DELETE.  
            + Estas consultas afectan las tablas de la BD pero no devuelven valor alguno. '''
        try:
            self.conectar()
            self.cnx.cursor().execute(query)
            self.cnx.commit()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
