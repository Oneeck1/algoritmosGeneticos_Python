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

DESCRIPCIÓN: Prueba cromosomas P.O.O

Created on Mon Mar 22 13:31:17 2021

@author: gustavo
"""

from AG_Base import Cromosoma, GenEntero

print("---IMPRIMIR CROMOSOMA----")
c = Cromosoma()
c.inicializa([1, 1, 10],[100, 50, 100], [True, False, True])
print(c)
c.mutar(1)
print(c)

print("---IMPRIMIR MUTACION----")

p = GenEntero()
m = GenEntero()

p.inicializa(0,25,True)
m.inicializa(0,25,True)

print("Padre")
print(p)

print("Madre")
print(m)

hijos = p.cruzar(m)
print("Hijo 1")
print(hijos[0])

print("Hijo 2")
print(hijos[1])

