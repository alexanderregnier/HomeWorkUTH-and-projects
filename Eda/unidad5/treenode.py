'''
Archivo: treenode.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 28-noviembre-2021

Objetivo: Proveer de una clase para gestionar los elementos nodo de un árbol binario.

Fuentes consultadas:
https://recursospython.com/guias-y-manuales/el-tipo-de-dato-none/
'''

class TreeNode:
    ''' Clase para implementar un Nodo. Un nodo es un elemento de un árbol binario. '''
    def __init__(self):
        self.izq = None     # Apuntador al nodo hijo que es menor
        self.value = None   # El valor del nodo
        self.der = None     # Apuntador al nodo hijo que es mayor

    def insert(self, dato):
        if self.value == None:     # Si el valor del nodo es None significa que el nodo no está ocupado
            self.value = dato
        else:
            if dato < self.value:
                if self.izq == None:
                    self.izq = TreeNode()
                self.izq.insert(dato)
            else:
                if self.der == None:
                    self.der = TreeNode()
                self.der.insert(dato)

    # Checar: Recorrido de árboles:
    # https://es.wikipedia.org/wiki/Recorrido_de_árboles

    def inorden(self, values:list):
        ''' Llena la lista values con los valores del obtenidos al efectuar un recorrido in-orden. '''
        if self.value != None:
            if self.izq != None: self.izq.inorden(values)
            values.append(self.value)       # print(self.value)
            if self.der != None: self.der.inorden(values)

    def preorden(self, values:list):
        ''' Llena la lista values con los valores del obtenidos al efectuar un recorrido pre-orden. '''
        if self.value != None:
            values.append(self.value)       # print(self.value)
            if self.izq != None: self.izq.preorden(values)
            if self.der != None: self.der.preorden(values)

    def postorden(self, values:list):
        ''' Llena la lista values con los valores del obtenidos al efectuar un recorrido post-orden. '''
        if self.value != None:
            if self.izq != None: self.izq.postorden(values)
            if self.der != None: self.der.postorden(values)
            values.append(self.value)       # print(self.value)

    def search(self, dato):
        ''' Busca un dato en el árbol. '''
        if self.value == dato:
            return True
        elif dato < self.value:
            if self.izq == None:
                return False
            return self.izq.search(dato)
        else:
            if self.der == None:
                return False
            return self.der.search(dato)

    def delete(self, dato):
        ''' Elimina un dato del árbol. '''
        if self.value == dato:
            if self.izq == None and self.der == None:
                self.value = None
            elif self.izq == None:
                self.value = self.der.value
                self.der = self.der.der
            elif self.der == None:
                self.value = self.izq.value
                self.izq = self.izq.izq
            else:
                self.value = self.der.min()
                self.der.delete(self.value)
        elif dato < self.value:
            if self.izq != None:
                self.izq.delete(dato)
        else:
            if self.der != None:
                self.der.delete(dato)