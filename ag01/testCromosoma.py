#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:07:18 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS
Alumno: Gustavo Rodrígez Calzada
Profesor: Asdrúbal Lopez Chau

Descripcion: Prueba de la clase Cromosoma


@author: gustavo
"""

from cromosoma import Cromosoma as cromo  
from fitness import printFitness

a = cromo()
a.printCromosoma()
a.mutacion()
a.printCromosoma()

padre = cromo()
madre = cromo()

print("Padre: ")
padre.printCromosoma()
print("Madre: ")
madre.printCromosoma()

hijos = padre.cruza(madre)
print("Hijo A: ")
hijos[0].printCromosoma()
print("Hijo B: ")
hijos[1].printCromosoma()


print("-----------------------------------------")
print("Padre: ")
printFitness(padre)

print("Madre: ")
printFitness(madre)

print("Hijo 0: ")
printFitness(hijos[0])

print("Hijo 1: ")
printFitness(hijos[1])







