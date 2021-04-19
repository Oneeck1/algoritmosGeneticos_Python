#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:47:16 2021

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
    return aptitud + 1e-4 # Sumo para evitar los 0


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
    
        