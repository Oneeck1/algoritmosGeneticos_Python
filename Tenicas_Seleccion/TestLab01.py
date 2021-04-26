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
from Lab01 import Gen, Cromosoma
import numpy as np
# El mejor individuo que el número 50

def MyFuncion(ind):
    valor = ind.fenotipo()    
    return np.exp(-np.abs(50-valor))

p = Gen()
m = Gen()
p.inicializa(0, 100, True)
m.inicializa(0, 100, True)
print("Padre: ")
print(p)
print("Madre: ")
print(m)
hijos = p.cruzar(m, MyFuncion)
print("Hijo 0: ")
print(hijos[0])
print("Hijo 1: ")
print(hijos[1])

print("-----------GEN ENTERO Y REAL---------")
print("Padre: ")
p = Cromosoma()
p.inicializa([1.,0], [10.,8], [True, True])
print(p)

print("Madre: ")
m = Cromosoma()
m.inicializa([1.,0], [10.,8], [True, True])
print(m)

hijos = p.cruzar(m)
print("Hijo 0: ")
print(hijos[0])
print("Hijo 0: ")
print(hijos[1])

print("Mutacion: ")
# Mutaremos al padre
p.mutar(1)
print(p)