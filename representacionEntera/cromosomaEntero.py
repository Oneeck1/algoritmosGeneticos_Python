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
import random

class Entero:
    
    def __init__(self):
        pass
 
    def inicializa(self, minimo=-32, maximo=32): 
        v = max([np.abs(minimo), np.abs(maximo)])
        self.nbits = int(np.ceil(np.log(v+1)/np.log(2)))
        self.minimo = minimo
        self.maximo = maximo # Hasta aqui vamos a saber los N bits de minimo y maximo
        self.cromosoma = random.choices([0,1], k = self.nbits)
        while not self.isFactible():
            self.cromosoma = random.choices([0,1], k=self.nbits)
    
    def fenotipo(self):
        cad = str(self.cromosoma[1:]).replace('[','').replace(']','').replace(',','').replace(' ','')
        if self.cromosoma[0]==0:
            return int(cad,2)
        else:
            return -int(cad,2)  

    def isFactible(self):
        if self.fenotipo() >= self.minimo and self.fenotipo() <= self.maximo:
            return True
        else:
            return False
    
    def mutar(self, nBitsToChange=1):
        cadena = list(self.cad)
        for i in range(nBitsToChange):
            tmp = random.sample(self.cromosoma,1)
        cadena[np.random.randint(0,1)] = tmp[0]
        cadena = ''.join(cadena)
        self.cromosoma=cadena        
            
            
            
            
            
            