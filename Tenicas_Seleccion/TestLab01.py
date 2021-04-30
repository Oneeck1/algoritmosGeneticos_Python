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

# Se crea un cromosoma padre
p = Cromosoma() 
# Se crea un cromosoma madre
m = Cromosoma()

# Se inicializan, en este caso quiero 8 padres
p.inicializa(8)
# Se inicializan, en este caso quiero 8 madres
m.inicializa(8)

# Se imprimen 
print("Padre: ")
print(p)

print("Madre: ")
print(m)













