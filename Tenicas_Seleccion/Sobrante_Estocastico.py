#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:31:10 2021

@author: gustavo
"""

import random 
import numpy as np
import math
# OBJEIVO: CAFE

def fitnessFuncion(individuo):
    objetivo = ['c','a','f','e']
    aptitud = 0
    indice = 0
    for letra in objetivo:
        if letra == individuo[indice]:
            aptitud+=1
        indice +=1
    return aptitud


poblacion = []
for i in range(10):
    individuo = random.choices(['a', 'b', 'c', 'd', 'e', 'f'], k = 4)
    poblacion.append(individuo)
    
    #RULETA
# 1.- CALCULO DE APTITUDES
aptitudes = []
for individuo in poblacion:
    aptitudes.append(fitnessFuncion(individuo))
    
    
print("\nPOBLACION: ")    
for i in range(10):
    print(poblacion[i])
    
print("\nAPTITUDES: ")    
for i in range(10):
    print(aptitudes[i])    
    
# 2.- FRECUENCIA ESPERADA TOTAL
f = (np.sum(aptitudes))/(len(aptitudes))
print("\nFRECUENCIA:")
print(f)
    
    
# 3.- CALCULAR E
e = []
for i in range(10):
    e.append(aptitudes[i]/f)
    
print("\nE: ")
for i in range(10):
    print(e[i])

# 4._ PARTE ENTERA Y FRACCIONARIA
partes = []   

for i in range(10): 
    partes.append(math.modf(e[i]))
    
# PARTE ENTERA
entero = []    
fraccionaria = []
for i in range(10):
    if float(partes[i][1]) >= 1.0:
        entero.append(i)
    else:
        fraccionaria.append(i)
    
# SELECCION PARTE FRACCIONARIA
parteFraccionaria = []
for i in range(len(fraccionaria)):
    parteFraccionaria.append(poblacion[fraccionaria[i]])


for i in range(len(fraccionaria)):
    elegido = random.choices(parteFraccionaria, k=1)        
    
print("PARTES: ")    
print(partes)

print("\nPARTE ENTERA, INDICES: ")
print(entero)
print("\nPARTE FRACCIONARIA, INDICES: ")
print(fraccionaria)
print("\nPARTE FRACCIONARIA") 
print(parteFraccionaria)
print("\nELEGIDO")   
print(elegido)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
