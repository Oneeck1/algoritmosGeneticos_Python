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


Created on Mon Mar 22 13:07:59 2021

@author: gustavo
"""
import numpy as np
import random


class GenNum:

    '''
    La super clase GenNum representa genes que son parte de
    soluciones numéricas (cromosomas) en un Algoritmo genético. 
    TODO: Implementa todos los métodos que sean posibles
    '''

    def __init__(self):
        pass

    def inicializa(self, vMin=0, mMax=15):

        '''
        Inicializa de manera pseudo aleatoria al inidividuo.

        :param `vMin`: El valor mínimo  a representar
        :param `vMax`: El valor máximo  a representar
        '''
        self.vMin = vMin
        self.vMax = vMax
        
        

    def isFactible(self):

        '''
        Verifica si el gen está dentro de los rangos vMin y vMax

        :returns: True si el gen es factible, False en otro caso
        :rtype: bool
        '''
        pass

    def mutar(self, nbits):

        '''
        Aplica mutación al gen        
        '''

        pass

    def cruzar(self, otro):
        
        '''
        Operador de cruza por dos puntos

        :param `otro`: Otro gen del mismo tipo
        :returns: Dos hijos
        :rtype: GenNum
        '''
        pass

    def _str__():
        '''
        Imprime como una cadena el gen.

        :returns: Una cadena que representa al gen
        :rtype: str
        '''
        pass
    
    def fenotipo():
        '''

        :returns: Valor del fenotipo que representa el gen
        :rtype: int o float
        '''
        pass


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
        super().inicializa(vMin, vMax)
        self.gray = gray
        v = max([np.abs(vMin), np.abs(vMax)])
        self.nbitss = int(np.ceil(np.log(v + 1)/np.log(2)) + 1)
        self.vMin = vMin
        self.vMax = vMax         
        self.cromosoma = random.choices([0, 1], k = self.nbits)
        while not self.isFactible():
            self.cromosoma = random.choices([0, 1], k = self.nbits)


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
        pass


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
