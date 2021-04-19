#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:43:29 2021



DESCRIPCION_ Ruleta primera version
Caso: Hola

@author: gustavo
"""

import random 

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
    individuo = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], k = 4)
    poblacion.append(individuo)
    
    #RULETA
# 1.- CALCULO DE APTITUDES
    aptitudes = []
    for individuo in poblacion:
        aptitudes.append(fitnessFuncion(individuo))
    
    