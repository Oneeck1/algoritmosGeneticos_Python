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
import random

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
        a = self.cromosoma
        b = otro.cromosoma
        
        tempA = a[1]+a[2]
        tempB = b[1]+b[2]
        
        temppA = tempA+b[3]
        temppB = tempB+a[3]
        
        hijo1 = a[0] + temppA
        hijo2 = b[0] + temppB

        h1 = Cromosoma()
        h2 = Cromosoma()
        h1.cromosoma = hijo1
        h2.cromosoma = hijo2
        
        return [h1, h2]
    
    def mutacion(self):
        # Tomar un gen aleatoriamente y cambiarlo aleatoriamente 
        c = list(self.cromosoma)
        tempo = random.sample(self.alfabeto,1)
        c[np.random.randint(0,self.tamCad)] = tempo[0]
        c = ''.join(c)
        self.cromosoma = c
        
        
    def printCromosoma(self):
        print(self.cromosoma)
            
            