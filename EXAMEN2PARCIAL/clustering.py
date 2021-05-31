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
        pass
    
    def aptitud(self):
        pass
    
    def cruzar(self):
        pass
    
    def mutar(self):
        pass
    
    def __str__(self):
        pass
    
    
    
# Importamos los datos del csv    
datos = pd.read_csv('datosExamen.csv')    

# K = 3, el núero de clusters
k = 3

# Creación del individuo 1 
individuo1 =  Cluster(datos)

# Creación del individuo 2
individuo2 =  Cluster(datos)
    
# Creación de los hijos, cruzando los 2 individuos
hijos = individuo1.cruzar(individuo2)

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