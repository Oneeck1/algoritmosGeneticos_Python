#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:43:29 2021



DESCRIPCION_ Ruleta primera version
Caso: Hola

@author: gustavo
"""

import random 
import numpy as np
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
    
# 2.- FRECUENCIA ESPERADA TOTAL
f = (np.sum(aptitudes))/(len(aptitudes))
     
# 3.- CALCULO DE VALORES ESPERADOS
valoresEsperados = []
for aptitud in aptitudes:
    valoresEsperados.append(aptitud*f)     

# 4.- SUMA DE VALORES ESPERADOS
T = np.sum(valoresEsperados)

print("POBLACION: ")
print(poblacion)
print("APTITUDES: ")
print(aptitudes)
print("VALORES ESPERADOS: ")
print(valoresEsperados)


# 5._ REPETIR N VECES
for i in range(10):
    # La suma es para que toque el T
    r = np.random.uniform(0,T+1e-4)
    



