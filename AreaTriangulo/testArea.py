#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:23:13 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Test Area Maxima de un Triangulo

@author: gustavo
"""

# Probabilidad 1e-6

from area import Cromosoma

# Se crea un cromosoma padre
p = Cromosoma() 
# Se crea un cromosoma madre
m = Cromosoma()

# Se inicializan
p.inicializa(10) # P
# Se inicializan
m.inicializa(10) # P

print("------------------------PADRES-----------------------")
# Se imprimen 
print("Padre: ")
print(p)

print("Madre: ")
print(m)
