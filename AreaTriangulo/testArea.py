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


from area import Cromosoma

# Se crea un cromosoma padre
p = Cromosoma() 
# Se crea un cromosoma madre
m = Cromosoma()

# Se inicializan, en este caso quiero 8 padres
p.inicializa(3)
# Se inicializan, en este caso quiero 8 madres
m.inicializa(3)
