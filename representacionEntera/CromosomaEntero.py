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
import time


class Entero:
    
    def __init__(self):
        pass
    
    def inicializa(self, minimo=-32, maximo=32):
        v = max([np.abs(minimo), np.abs(maximo)])
        self.nbits = int(np.ceil(np.log(v + 1)/np.log(2)) + 1)
        self.minimo = minimo
        self.maximo = maximo
        self.cromosoma = random.choices([0, 1], k = self.nbits)
        while not self.isFactible():
            self.cromosoma = random.choices([0, 1], k = self.nbits)
            
    
    # Regresa el fenotipo: El valor que representa el cromosoma
    def fenotipo(self):
        cad = str(self.cromosoma[1:]).replace('[','').replace(']','').replace(',','').replace(' ','')
        if self.cromosoma[0] == 0: return int(cad, 2)
        else: return -int(cad, 2)
        
    #  Regresa True si el individuo representa una solucion factible, y False en otro caso
    def isFactible(self):
        if self.fenotipo() >= self.minimo and self.fenotipo() <= self.maximo:
            return True
        else: return False
    
    #  Muta al individuo
    def mutar(self, nbitsToChange=1):
        respaldo = self.cromosoma.copy()
        start = time.time()
        while True:
            currentTime = time.time()
            if currentTime-start > 0.3:
                print('Timeout')
                while self.cromosoma == respaldo:
                    self.inicializa(self.minimo, self.maximo)
                return
                
            idxs = random.sample(range(self.nbits), nbitsToChange)
            for i in idxs:
                self.cromosoma[i] = 1 - self.cromosoma[i]
                if not self.isFactible():
                    self.cromosoma = respaldo.copy()
                    break    
            if respaldo != self.cromosoma:#  Comprobar que sea diferente al individuo antes de mutar
                    break
                
    def cruzar(self, otro):
        pass