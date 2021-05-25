#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:04:45 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Solucion de problemas con AG
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Implementa clustering con un AG

@author: gustavo
"""

import pandas as pd
from matplotlib import pyplot as plt
import random
import numpy as np

class funcionAptitudCluster:
    def evaluate(self, indiv, datos):
        pass
    
    def computerCentroids(self, k):
        '''
        Calcular los K centroides
        return = una lista de centroides
        '''
        cK = k
        
        

class IndividuoCluster:
    def __init__(self, datos):
        self.datos = datos  # guardo los datos 
    
    def inicializa(self, K):
        longitud = len(self.datos)
        valoresAlelicos = list(range(1, K+1))
        self.cromosoma = random.choices(valoresAlelicos,
                                        k=longitud)

    def cruzar(self, madre):
        pass
    
    def mutar(self):
        pass
    
    def printIt(self):
        print(self.cromosoma)

##########################################################
#PRUEBAS
datos = pd.read_csv('iris.csv')
datos = datos.iloc[:,0:2]
plt.scatter(datos.iloc[:, 0], datos.iloc[:, 1])
ind1 = IndividuoCluster(datos)
K = 3
ind1.inicializa(K)
ind1.printIt()