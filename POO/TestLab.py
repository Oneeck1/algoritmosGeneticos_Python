#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Crosmosomas numéricas en POO
ALUMNO: tu nombre
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Prueba cromosomas con genes numéricos
en POO con Python

Created on Mon Apr  5 21:22:38 2021

Instrucciones: Después de haber completado la clase
para genes reales (codificación en binario y gray),
ejecuta este script. Se debe de imprimir cromosomas
con tres genes (dos reales y uno entero).

@author: asdruballopezchau
"""
from Cromosomas import Cromosoma

# Prueba de laboratorio
p = Cromosoma()  # Crea cromosoma del padre
m = Cromosoma()  # Crea cromosoma de la madre
# Inicializa aleatoriamente. La estructura del cromosoma
# es:  entero | real | real
p.inicializa([1, 0., -1.0], [10, 8., 4], [True, True, False])
m.inicializa([1, 0., -1.0], [10, 8., 4], [True, True, False])
# Imprime las cromosomas con tres genes cada una
print('Padre: ')
print(p)
print('Madre: ')
print(m)
hijos = p.cruzar(m)
print('Hijos: ')
print(hijos[0])
print(hijos[1])
# Muta el primero hijo
hijos[0].mutar()
print(hijos[0])



