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
import copy

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
        self.datos = datos
    
    def inicializa(self, K):
        longitud = len(self.datos)
        valoresAlelicos = list(range(1, K+1))
        self.cromosoma = random.choices(valoresAlelicos, k=longitud)

        
    def graficar(self):
        labels=['','or', 'ob', 'og', 'oc', 'ok']
        clusters = list(set(self.cromosoma))
        clusters.sort()
        for cluster in clusters:
            i = 0
            index = []
            for gen in self.cromosoma:
                if gen == cluster:
                    index.append(i)
                i+=1    

            plt.plot(self.datos.iloc[index, 0],
                     self.datos.iloc[index, 1],
                     labels[cluster])
    def cruzar(self, Madre):    
        padre = self.cromosoma
        madre = Madre.cromosoma
        cp1 = int(np.ceil(len(padre)/3.0))
        cp2 = cp1*2
        hijo1 = padre.copy()
        hijo2 = madre.copy()
        medio1 = madre[cp1:cp2]
        medio2 = padre[cp1:cp2]
        hijo1[cp1:cp2] = medio1
        hijo2[cp1:cp2] = medio2
        h1 = copy.deepcopy(self)  # Crea una copia exacta
        h1.cromosoma = hijo1
        h2 = copy.deepcopy(Madre)
        h2.cromosoma = hijo2
        return [h1, h2]
        
    def mutar(self):
        pass
    
    def printIt(self):
        print(self.cromosoma)

##########################################################

# Se lee el conjunto de datos de iris
datos = pd.read_csv('iris.csv')

# Selección de las dos columnas para los datos
datos = datos.iloc[:,0:2]
plt.scatter(datos.iloc[:, 0], datos.iloc[:, 1])

# Creación de 2 individuos
ind1 = IndividuoCluster(datos)
ind2 = IndividuoCluster(datos)

# Inicialización de 3 Clusters
K = 3

# Inicializando los 2 individuos
ind1.inicializa(K)
ind2.inicializa(K)

# Creación de los hijos, cruzando los 2 individuos
hijos = ind1.cruzar(ind2)

# Imprimiendo INDIVIDUO 1
print("Papá")
ind1.printIt()

# Imprimiendo INDIVIDUO 2
print("Mamá")
ind2.printIt()

# Imprimiendo HIJO0
print("Primer hijo")
hijos[0].printIt()

# Imprimiwndo HIJO1
print("Segundo hijo")
hijos[1].printIt()

# Graficando el INDIVIDUO1
ind1.graficar()

# Graficando los HIJOS
hijos[0].graficar()
hijos[1].graficar()        
        

