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
    objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
    aptitud = 0
    indice = 0
    for letra in objetivo:
        if letra == individuo[indice]:
            aptitud+=1
        indice +=1
    return aptitud


poblacion = []
for i in range(10):
    individuo = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k = 10)
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

numerosElegidos = entero
faltaPorElegir = fraccionaria


# SELECCION PARTE FRACCIONARIA
parteFraccionaria = []
for i in range(len(fraccionaria)):
    parteFraccionaria.append(poblacion[fraccionaria[i]])

parteEntera = []
for i in range(len(fraccionaria)):
    parteEntera.append(poblacion[fraccionaria[i]])



for i in range(len(fraccionaria)):
    elegido = random.choices(parteFraccionaria, k=1)        
    
    
PF =[]
PE = []
    
for i in range(len(entero)):  
    PE.append(poblacion[entero[i]])    
    
for i in range(len(fraccionaria)):      
    PF.append(poblacion[fraccionaria[i]])
    
    
    
    
print("PARTES: ")    
print(partes)

print("\nPARTE ENTERA, INDICES: ")
print(entero)

print("\nPARTE FRACCIONARIA, INDICES: ")
print(fraccionaria)

print("\nPARTE ENTERA: ")
print(PE)

print("\nPARTE FRACCIONARIA: ")
print(PF)

print("\nPARTE ENTERA, CARACTERES") 
print(parteEntera)

print("\nPARTE FRACCIONARIA, CARACTERES") 
print(parteFraccionaria)


print("\nELEGIDO")   
print(elegido)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
