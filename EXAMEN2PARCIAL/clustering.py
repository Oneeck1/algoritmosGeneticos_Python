#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:15:06 2021
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Solucion de problemas con AG
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: EXAMEN:Implementa clustering con un AG

@author: gustavo
"""


import pandas as pd
from matplotlib import pyplot as plt
import random
import numpy as np
from random import sample
import copy

class Cluster:
    def __init__(self, datos, k):
        # Inicializando los datos 
        self.datos = datos
        
        # Inicializando los k clusters
        self.k = k
        pass
    
    
    def aptitud(self):
        pass
    
    def cruzar(self,Madre):
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
        pass
    
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
            
    
    
# Importamos los datos del csv    
datos = pd.read_csv('datosExamen.csv')    

# K = 3, el núero de clusters
k = 3

# Creación del individuo 1 
individuo1 =  Cluster(datos,k)

# Creación del individuo 2
individuo2 =  Cluster(datos,k)
    
# Creación de los hijos, cruzando los 2 individuos
hijos = individuo1.cruzar(individuo2)

# Imprimiendo INDIVIDUO 1
print("Papá")
individuo1.printIt()

# Imprimiendo INDIVIDUO 2
print("Mamá")
individuo2.printIt()

# Imprimiendo HIJO0
print("Primer hijo")
hijos[0].printIt()

# Imprimiwndo HIJO1
print("Segundo hijo")
hijos[1].printIt()    