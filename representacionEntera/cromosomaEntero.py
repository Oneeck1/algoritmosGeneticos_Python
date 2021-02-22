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
import numpy as np


class Entero:
    
    def __init__(self):
        pass
    def inicializa(self, minimo=0, maximo=32): 
        v = np.max(np.abs(minimo), np.abs(maximo))
        self.nbits = np.ceil(np.log(v+1)/np.log(2))
        self.minimo = minimo
        self.maximo = maximo # Hasta aqui vamos a saber los N bits de minimo y maximo
        self.cromosoma = random.choices([0,1], k = self.nbits)
        
        pass
    def mutar(self):
        pass
    def cruzar(self, otro):
        pass
