#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:32:39 2021

CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS
Alumno: Gustavo Rodrígez Calzada
Profesor: Asdrúbal Lopez Chau

Descripción: Implementa un cromosoma para representar numeros
enteros


@author: gustavo
"""

from Gray import Gray

ind = Gray()

ind.inicializa(-15,15)

print(ind.cromosoma)
print(ind.fenotipo())
ind.mutar(1)
print('MUTADO')
print(ind.cromosoma)
print(ind.fenotipo())
