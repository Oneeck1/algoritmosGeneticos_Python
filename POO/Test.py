#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: tu nombre
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Prueba cromosomas POO

Created on Mon Mar 22 13:31:09 2021

@author: asdruballopezchau
"""
from Cromosomas import GenEntero, Cromosoma

p = GenEntero()
m = GenEntero()
p.inicializa(0, 100, True)
m.inicializa(0, 100, True)
print(p)
print(m)
hijos = p.cruzar(m)
print(hijos[0])
print(hijos[1])


