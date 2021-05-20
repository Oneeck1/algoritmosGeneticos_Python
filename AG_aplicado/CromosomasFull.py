#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: tu nombre
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Super clase de todas las cromosomas numéricas

Created on Mon Mar  8 16:49:47 2021

@author: asdruballopezchau
"""

import numpy as np
import random
import copy


class GenNum:

    '''
    La super clase GenNum representa genes que son parte de
    soluciones numéricas (cromosomas) en un Algoritmo genético.
    TODO: Implementa todos los métodos que sean posibles
    '''

    def __init__(self):
        pass

    def inicializa(self, vMin=0, vMax=15):
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
        return True

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

    def __str__():
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
        #  Cálculo del número minimo de bits para representar un valor
        #  entre vMin y vMax
        v = max([np.abs(vMin), np.abs(vMax)])
        self.nbits = int(np.ceil(np.log(v + 1)/np.log(2)) + 1)
        self.cromosoma = random.choices([0, 1], k=self.nbits)
        # Generar un indivividuo factible
        while not self.isFactible():
            self.cromosoma = random.choices([0, 1], k=self.nbits)

    # Regresa el fenotipo: El valor que representa el cromosoma
    def fenotipo(self):
        if not self.gray:  # Representación en binario
            cad = str(self.cromosoma[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
        else:  # Representación en Gray
            binario = self.cromosoma.copy()
            for i in range(2, len(self.cromosoma)):
                a = self.cromosoma[i - 1]
                b = self.cromosoma[i]
                if a == b:
                    binario[i] = 0
                else:
                    binario[i] = 1
            cad = str(binario[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
        if self.cromosoma[0] == 0:
            return int(cad, 2)
        else:
            return -int(cad, 2)

    #  Regresa True si el individuo representa una solucion factible, y False en otro caso
    def isFactible(self):
        if self.fenotipo() >= self.vMin and self.fenotipo() <= self.vMax:
            return True
        else:
            return False

    def mutar(self, nbits):
        while True:
            bits_cambiar = random.choices(range(len(self.cromosoma)), k=nbits)
            for i in bits_cambiar:
                self.cromosoma[i] = 1 - self.cromosoma[i]
            if self.isFactible():
                break

    def cruzar(self, otro, funcionAptitud=None):
        padre = self.cromosoma
        madre = otro.cromosoma
        # Crear hijos con cruza por dos puntos
        cp1 = int(np.ceil(len(padre)/3))
        cp2 = int(2*cp1)
        hijo1 = padre.copy()
        hijo2 = madre.copy()
        medio1 = madre[cp1:cp2]
        medio2 = padre[cp1:cp2]
        hijo1[cp1:cp2] = medio1
        hijo2[cp1:cp2] = medio2
        h1 = copy.deepcopy(self)  # Crea una copia exacta
        h1.cromosoma = hijo1
        h2 = copy.deepcopy(otro)
        h2.cromosoma = hijo2
        if funcionAptitud is None:
            return [h1, h2]
        aptitudPadre = funcionAptitud(self)
        aptitudMadre = funcionAptitud(otro)
        aptitudHijo1 = funcionAptitud(h1)
        aptitudHijo2 = funcionAptitud(h2)

        # Genera hijos mejores siempre.
        while aptitudHijo1 < aptitudPadre \
            or aptitudHijo1 < aptitudMadre \
        or aptitudHijo2 < aptitudPadre \
        or aptitudHijo2 < aptitudMadre:
            h1 = GenEntero()
            h1.inicializa(self.vMin, self.vMax)
            h2 = GenEntero()
            h2.inicializa(otro.vMin, otro.vMax)
            aptitudHijo1 = funcionAptitud(h1)
            aptitudHijo2 = funcionAptitud(h2)
        return [h1, h2]

    def __str__(self):
        return str(self.cromosoma) + " (" + str(self.fenotipo()) + ")"


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
                 
        super().inicializa(vMin, vMax)
        self.gray = gray
        # Calculo del número mínimo de bits para representar un valor entre
        # vMin y vMax
        v = max([vMin, vMax])  
        self.nbits = int(np.ceil(np.log(v + 1)/np.log(2)) + 1) # Saber cuantos bits ocupo para parte entera
        entero = random.choices([0, 1], k = self.nbits)
        decimal = random.choices([0, 1], k = self.nbits)
      
        #self.cromosoma = entero,decimal
        # self.entero_decimal(NumAl)
        entero = str(entero[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
        #entero22 = str(entero[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
        decimal = str(decimal[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')



class Cromosoma:
    '''
    La clase representa soluciones con uno o más genes
    que son parte de un Algoritmo genético.

    Cada cromosoma puede tener uno o más genes de tipo numérico, ya
    sean enteros o reales, con representación binaria o Gray.

    TODO: LA CLASE CROMOSOMA TIENE GENES" APROVECHA LO QUE 
    PUEDAS DE LAS CLASES GenNum, GenEntero y GenReal.
    '''

    def __init__(self):
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
        genes = []
        if len(vMins) != len(vMaxs):
            return

        for i in range(len(vMins)):
            if type(vMins[i]) is float or type(vMaxs[i]) is float:
                g = GenReal()
                g.inicializa(vMins[i], vMaxs[i], gray=grays[i])
                genes.append(g)
            else:
                #  Representación entera
                g = GenEntero()
                g.inicializa(vMins[i], vMaxs[i], gray=grays[i])
                genes.append(g)
        self.genes = genes

    def isFactible(self):
        factible = True
        for gen in self.genes:
            factible = factible and gen.isFactible()
            if not factible:
                return False
        return True

    def mutar(self, nbits=1):
        '''
        Aplica mutación al individuo completo
        '''
        for gen in self.genes:
            gen.mutar(nbits)

    def cruzar(self, otro):
        '''
        Operador de cruza con otro gen

        :param `otro`: Otro cromosoma con la misma estuctura
        :returns: Dos hijos
        :rtype: Cromosma
        '''
        h1 = copy.deepcopy(self)
        h2 = copy.deepcopy(otro)
        genesHijos1 = []
        genesHijos2 = []
        for i in range(len(self.genes)):
            genPadre = self.genes[i]
            genMadre = otro.genes[i]
            genHijos = genPadre.cruzar(genMadre)
            genesHijos1.append(genHijos[0])
            genesHijos2.append(genHijos[1])
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]
        # LABORATORIO: Implementar la cruza con función de aptitud
        # para producir siempre mejores hijos.

    def __str__(self):
        '''
        Imprime como una cadena el cromosoma.

        :returns: Una cadena que representa al cromosoma completo
        :rtype: str
        '''
        cad = ""
        for gen in self.genes:
            cad = cad + str(gen) + "\n"
        return cad

    def fenotipo(self):
        '''
        :returns: Valores del cromosoma
        :rtype: int o float
        '''
        fenotipos = []
        for gen in self.genes:
            fenotipos.append(gen.fenotipo())
        return fenotipos