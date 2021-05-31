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
 
        # Calcular la longitud de todos los datos       
        longitud = len(self.datos)
        
        # Valores alelicos que son numeros aleatorios del 1 al Numero de clusters
        valoresAlelicos = list(range(1, self.k+1))
        
        # Se asigna al cromosoma los valores alelicos
        self.cromosoma = random.choices(valoresAlelicos, k=longitud)
    
    
    def aptitud(self):
        self.datos = sample(range(0,len(self.cromosoma)),k)
        E = []
        S = []
        for i in range(0,len(self.datos)):
            for j in range(0,len(self.cromosoma)-1):
                E[j] = ( pow( ( abs(self.cromosoma[j] - self.cromosoma[self.datos[i]]) ) ,2 ) )
            S[i] = min(E)        
        res = min(S)
        return res
    
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
        # Mutación al 5%
        
        porcentaje = int( np.ceil(len(self.cromosoma)*0.05) )
        
        
        for i in range(porcentaje):
            indices = random.randint(1,len(self.cromosoma)-1)
            if self.cromosoma[indices] == 1:
                indices2 = random.randint(2,3)            
                self.cromosoma[indices] = self.cromosoma[indices2]
                
            elif self.cromosoma[indices] == 2:
                indices2 = random.sample([1,3],1)
                indices2 = int(indices2[0])
                self.cromosoma[indices] = self.cromosoma[indices2]
                
            elif self.cromosoma[indices] == 3:
                indices2 = random.randint(1,2)
                self.cromosoma[indices] = self.cromosoma[indices2]
            else:
                self.cromosoma = self.cromosoma
        return self.cromosoma
    
    def printIt(self):
        print(self.cromosoma)
    
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

#-------------------------------CREACION DE LOS INDIVIDUOS------------------
# Creación del individuo 1 
individuo1 =  Cluster(datos,k)

# Creación del individuo 2
individuo2 =  Cluster(datos,k)

#-------------------------------CREACION DE LOS HIJOS------------------------    
# Creación de los hijos, cruzando los 2 individuos
hijos = individuo1.cruzar(individuo2)

#-------------------------------IMPRIMIENDO LOS INDIVIDUOS------------------
# Imprimiendo INDIVIDUO 1
print("Papá")
individuo1.printIt()

# Imprimiendo INDIVIDUO 2
print("Mamá")
individuo2.printIt()

#-------------------------------IMPRIMIENDO LOS HIJOS-----------------------
# Imprimiendo HIJO0
print("Primer hijo")
hijos[0].printIt()

# Imprimiwndo HIJO1
print("Segundo hijo")
hijos[1].printIt()    

#-------------------------------GRAFICANDO DE LOS HIJOS----------------------
hijos[0].graficar()
hijos[1].graficar()  
