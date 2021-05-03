#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:23:13 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Area Máxima de un triangulo

@author: gustavo
"""
import random


class Gen():
    
    def __init__(self):
        pass
    
    def inicializa(self, P):
        self.vMin = P/100
        self.vMax = P-self.vMin
        self.cromosoma = random.choices(self.vMin,self.vMax, k=3)

      

class Cromosoma():
    
    def __init__(self):    
        pass

    def inicializa(self,nPob):
        # Se crea espacio para los genes
        genes = []
        for i in range (nPob): # En TestLab01 se pedirá cuanfos genes desarrollaran
             g = Gen()  # Se crean los objetos
             g.inicializa(10) # Se inicializan los objetos (de tamaño 10 y 5 individuos)
             genes.append(g)    # Se agrega cada objeto a genes
        self.genes = genes # Se agrega a genes
