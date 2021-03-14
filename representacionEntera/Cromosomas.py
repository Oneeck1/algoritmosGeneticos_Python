#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Super clase de todas las cromosomas numéricas

Created on Mon Mar  8 16:49:47 2021

@author: gustavo
"""

import numpy as np
import random
import time


class GenNum:

    '''
    La super clase GenNum representa genes que son parte de
    soluciones numéricas (cromosomas) en un Algoritmo genético. 
    TODO: Implementa todos los métodos que sean posibles
    '''

    def __init__(self, vMin, mMax):
        pass
        

    def inicializa(self, vMin=0, mMax=15):

        '''
        Inicializa de manera pseudo aleatoria al inidividuo.

        :param `vMin`: El valor mínimo  a representar
        :param `vMax`: El valor máximo  a representar
        '''
        v = max([np.abs(vMin), np.abs(mMax)])
        self.nbitss = int(np.ceil(np.log(v + 1)/np.log(2)) + 1)
        self.vMin = vMin
        self.mMax = mMax         
        self.cromosoma = random.choices([0, 1], k = self.nbits)
        while not self.isFactible():
            self.cromosoma = random.choices([0, 1], k = self.nbits)
            


    def isFactible(self):

        '''
        Verifica si el gen está dentro de los rangos vMin y vMax

        :returns: True si el gen es factible, False en otro caso
        :rtype: bool
        '''
        if self.fenotipo() >= self.vMin and self.fenotipo() <= self.mMax:
            return True
        else: 
            return False
        

    def mutar(self, nbits):

        '''
        Aplica mutación al gen        
        '''
        respaldo = self.cromosoma.copy()
        start = time.time()
        while True:
            currentTime = time.time()
            if currentTime-start > 0.3:
                print('Timeout')
                while self.cromosoma == respaldo:
                    self.inicializa(self.vMin, self.mMax)
                return
                
            idxs = random.sample(range(self.nbitss), nbits)
            for i in idxs:
                self.cromosoma[i] = 1 - self.cromosoma[i]
                if not self.isFactible():
                    self.cromosoma = respaldo.copy()
                    break    
            if respaldo != self.cromosoma:#  Comprobar que sea diferente al individuo antes de mutar
                    break

    def cruzar(self, otro):
        
        '''
        Operador de cruza por dos puntos

        :param `otro`: Otro gen del mismo tipo
        :returns: Dos hijos
        :rtype: GenNum
        '''
        a = self.cromosoma
        b = otro.cromosoma
        
        tempA = a[1]+a[2]
        tempB = b[1]+b[2]
        
        temppA = tempA+b[3]
        temppB = tempB+a[3]
        
        hijo1 = a[0] + temppA
        hijo2 = b[0] + temppB

        h1 = Cromosoma()
        h2 = Cromosoma()
        h1.cromosoma = hijo1
        h2.cromosoma = hijo2
        
        return [h1, h2]
        

    def _str__(self):
        '''
        Imprime como una cadena el gen.

        :returns: Una cadena que representa al gen
        :rtype: str
        '''                
        pass
    
    def fenotipo(self):
        '''
        :returns: Valor del fenotipo que representa el gen
        :rtype: int o float    
        '''
        cad = str(self.cromosoma[1:]).replace('[','').replace(']','').replace(',','').replace(' ','')
        if self.cromosoma[0] == 0: 
            return int(cad, 2)
        else: 
            return -int(cad, 2)        


class GenEntero(GenNum):

    '''
    Sub clase de GenNum representa genes que son parte de
    soluciones numéricas enteras en un Algoritmo genético.
    La cadena de bits del gen está binario o gray.
    
    TODO: SOBRE ESCRIBE LOS MÉTODOS, APROVECHA LO QUE 
    PUEDAS DE LA SUPERCLASE
    '''

    def inicializa(self, vMin=0, vMax=15, gray=True):
        
        '''
        Inicializa de manera pseudo aleatoria al inidividuo.

        :param `vMin`: El valor mínimo  a representar
        :param `vMax`: El valor máximo  a representar
        :param `gray`: Valor para indicar si el gen 
        representa valores en Gray o en Binario
        '''
        if gray:
            v = max([np.abs(vMin), np.abs(vMax)])
            self.nbits = int(np.ceil(np.log(v + 1)/np.log(2)) + 1)
            self.vMin = vMin
            self.vMax = vMax
            gray = str()
            cad = str(self.cromosoma[1:]).replace('[','').replace(']','').replace(',','').replace(' ','')

            for i in range(len(cad) - 1):
                if (cad[i] == cad[i + 1]):
                    gray += "0"
                else :
                    gray += "1"
            
            self.cromosoma = gray
            while not self.isFactible():
                self.cromosoma = gray
        else:
            super().inicializa()
            
        
        
    def isFactible(self):
        super().isFactible()        
        
    def mutar(self,nbitss):
        super().mutar()
        
    def cruzar(self, otro):
        super().cruzar()        
        
    def _str__(self):
        super()._str__()
        
    def fenotipo(self):
        super().fenotipo()

class GenReal(GenNum):

    '''
    Sub clase de GenNum representa genes que son parte de
    soluciones numéricas reales en un Algoritmo genético.
    La cadena de bits del gen está binario o gray.
    
    TODO: SOBRE ESCRIBE LOS MÉTODOS, APROVECHA LO QUE 
    PUEDAS DE LA SUPERCLASE
    '''

    def inicializa(self, vMin=0, vMax=15, gray=True):
        
        '''
        Inicializa de manera pseudo aleatoria al inidividuo.

        :param `vMin`: El valor mínimo  a representar
        :param `vMax`: El valor máximo  a representar
        :param `gray`: Valor para indicar si el gen 
                    representa valores en Gray o en Binario
        '''
        super.inicializa()
        
    def isFactible(self):
        super().isFactible()        
        
    def mutar(self,nbitss):
        super().mutar()
        
    def cruzar(self, otro):
        super().cruzar()        
        
    def _str__(self):
        super()._str__()
        
    def fenotipo(self):
        super().fenotipo()


class Cromosoma:
    '''
    La clase representa soluciones numéricas con uno o más genes 
    que son parte de un Algoritmo genético.

    Cada cromosoma puede tener uno o más genes de tipo numérico, ya
    sean enteros o reales, con representación binaria o Gray.

    TODO: LA CLASE CROMOSOMA TIENE GENES" APROVECHA LO QUE 
    PUEDAS DE LAS CLASES GenNum, GenEntero y GenReal.
    '''
    pass

    def __init__(self, listaGenes):
        
        '''
        Forma un cromosoma con los genes del inidividuo en la lista.

        :param `listaGenes`: Una lista con genes (subtipos de GenNum).
        '''        
        pass

    def inicializa(self, vMins, vMaxs, grays):
        '''
        Inicializa de manera pseudo aleatoria a cada uno de los genes 
        del inidividuo.

        :param `vMins`: Lista de valores mínimos para cada gen
        :param `vMax`:  Lista de valores máximos para cada gen
        :param `grays`: Lista de valores bool indicando si 
        la codificación es gray o binaria para cada gen
        '''
        pass
    
    def isFactible(self):
        pass

    def mutar(self, nbits):

        '''
        Aplica mutación al individuo completo
        '''

        pass

    def cruzar(self, otro):

        '''
        Operador de cruza con otro gen

        :param `otro`: Otro cromosoma con la misma estuctura
        :returns: Dos hijos
        :rtype: Cromosma
        '''
        pass

    def _str__():
        
        '''
        Imprime como una cadena el cromosoma.

        :returns: Una cadena que representa al cromosoma completo
        :rtype: str
        '''
        pass
    def fenotipo():
        '''

        :returns: Valores del cromosoma
        :rtype: int o float
        '''
        pass
