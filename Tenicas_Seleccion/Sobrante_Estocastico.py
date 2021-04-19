#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:31:10 2021

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
