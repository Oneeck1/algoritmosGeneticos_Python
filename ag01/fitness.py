#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:16:28 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS
Alumno: Gustavo Rodrígez Calzada
Profesor: Asdrúbal Lopez Chau

Descripcion: Implementar la funcion de aptitud



@author: gustavo
"""


from cromosoma import Cromosoma

passwordd = "aeio"

# Elitismo
def fitness(individuo):
    aptitud = 0
    for i in range(0,len(passwordd)):
        if passwordd[i] == individuo.cromosoma[i]:
            aptitud += 1
    return aptitud


def printFitness(individuo):
    fit = fitness(individuo)
    print(individuo.cromosoma + " -> "+ str(fit))















