#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:40:17 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS
Alumno: Gustavo Rodrígez Calzada
Profesor: Asdrúbal Lopez Chau

Descripción: Cromosoma del primer algoritmo genético


@author: gustavo
"""
import numpy as np


class Cromosoma:
    
    # Constructor
    def __init__(self):            
        self.tamCad = 4
        self.alfabeto = "aeiou"
        self.cromosoma=self.generarCadena()
        
    def generarCadena(self):
        cad = ""
        for i in range(0, self.tamCad):
            j = np.random.randint(0,self.tamCad)
            cad = cad+self.alfabeto[j]
        return cad
            
    def cruza(self, otro):
        pass
    
    def mutacion(self):
        pass
    
    def printCromosoma(self):
        print(self.cromosoma)
            
            