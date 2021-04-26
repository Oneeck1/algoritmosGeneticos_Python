#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:44:07 2021
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: LABORATORIO 01
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: lABORATORIO 01, PARA EL OBJETIVO: Hola Mundo

@author: gustavo
"""

import random
import numpy as np
import copy

class Gen:
    
    def __init__(self):
        self.tamCad = 10
    
    
    def Aptitud(individuo):
        objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
        aptitud = 0
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]:
                aptitud+=1
                indice +=1
        return aptitud + 1e-4                
                
    def cruza(self, otro, aptitud=None):
        padre = self.cromosoma
        madre = otro.cromosoma
        # Crear hijos con cruza por dos puntos
        cp1 = int(np.ceil(len(padre)/3))
        cp2 = int(2*cp1)

        hijo1 = padre.copy()
        hijo2 = madre.copy()
        
        medio1 = madre[cp1:cp2]
        medio2 = padre[cp1:cp2]
        
        hijo1[cp1:cp2] = medio1
        hijo2[cp1:cp2] = medio2
        
        h1 = copy.deecopy(self)
        h1.cromosoma = hijo1
        h2 = copy.deecopy(otro)
        h2.cromosoma = hijo2
        
        if aptitud is None:
            return [h1, h2] 
        aptitudPadre = aptitud(self)
        aptitudMadre = aptitud(otro)
        aptitudHijo1 = aptitud(h1)
        aptitudHijo2 = aptitud(h2)

        # Generar mejores hijos
        while aptitudHijo1 < aptitudPadre or aptitudHijo1 < aptitudMadre or aptitudHijo2 < aptitudPadre or aptitudHijo2 < aptitudMadre:
            h1.inicializa(self.tam)
            h2.inicializa(self.tam)
            aptitudHijo1 = aptitud(h1)
            aptitudHijo2 = aptitud(h2)
        return [h1,h2]
class Cromosoma:
    genes = []
    gen = Gen() 
    genes.append(gen)

