#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:28:16 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS
Alumno: Gustavo Rodrígez Calzada
Profesor: Asdrúbal Lopez Chau

Descripción: Implementa un cromosoma para representar numeros
enteros



@author: gustavo

"""


from CromosomaEntero import Entero

ind = Entero()

ind.inicializa(0, 15)
print(ind.cromosoma)
print(ind.fenotipo())
ind.mutar(2)
print('MUTADO')
print(ind.cromosoma)
print(ind.fenotipo())
