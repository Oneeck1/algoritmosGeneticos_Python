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

from Lab01Full import Cromosoma
import numpy as np

def MyFuncion(ind):
    valor = ind.fenotipo()    
    return np.exp(-np.abs(50-valor))

# Se crea un cromosoma padre
p = Cromosoma() 
# Se crea un cromosoma madre
m = Cromosoma()

# Se inicializan, en este caso quiero 8 padres
p.inicializa(3)
# Se inicializan, en este caso quiero 8 madres
m.inicializa(3)

print("------------------------PADRES-----------------------")
# Se imprimen 
print("Padre: ")
print(p)

print("Madre: ")
print(m)


print("-----------------------CRUZA-------------------------")
hijos = p.Cruzar(m)
print("Hijo 0: ")
print(hijos[0])
print("Hijo 1: ")
print(hijos[1])











