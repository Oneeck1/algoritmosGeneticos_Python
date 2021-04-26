#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Prueba cromosomas POO

Created on Mon Mar 22 13:31:09 2021

@author: gustavo
"""
import numpy as np

from Lab01 import Cromosoma

def MyFuncion(ind):
    valor = ind.fenotipo()    
    return np.exp(-np.abs(50-valor))

p = Cromosoma()
m = Cromosoma()

p.inicializa(10)
m.inicializa(10)


print("Padre: ")
print(p)
print(p)
print("Madre: ")
print(m)
print(m)

hijos = m.cruza(p)

print("Hijo 0: ")
print(hijos[0])
print("Hijo 1: ")
print(hijos[1])












