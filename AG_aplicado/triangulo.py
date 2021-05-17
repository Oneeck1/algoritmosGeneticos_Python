#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:09:21 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Área máxima de un triángulo



@author: gustavo
"""
from Cromosomas import GenReal
from Cromosomas import Cromosoma
import numpy as np

class Triangulo:
    def __init__(self, perimetro):
        self.perimetro = perimetro;
        
    def setLados(self,a,b,c):
        self.a = a
        self.a = b
        self.a = c
      
    def area(self):
        s = self.a + self.b + self.c
        s = s/2.0
        
        tmp = s*(s-self.a)*(s-self.b)*(s-self.c)
        if tmp < 0:
            area = -1.0
        else:
            area = np.sqrt(tmp)
        return area
        
class TrianguloAG(Triangulo):
    
    def __init__(self, perimetro):
        super().__init__(perimetro)
        self.cromo = Cromosoma()
    
    def __str__(self):
        return "a = {:.3f}, b = {:.3f}, c={:.3f}".format(self.a, self.b, self.c)
        
    
    def inicializa(self):
        perimetro = self.perimetro
        self.cromo.inicializa(perimetro/100.0, perimetro/100.0, perimetro/100.0), [perimetro, perimetro, perimetro], [True,True,True]
        '''self.a = self.cromo.fenotipo()[0]
        self.b = self.cromo.fenotipo()[1]
        self.c = self.cromo.fenotipo()[2]
        '''
        
    def cruzar(self,madre):
        self.cromo.cruzar(madre)
    
    
    def mutar(self):
        return self.cromo.mutar(1)
    
    
class FitnessFunctionTriangulo:
    
    def evaluate(individuo):
        
    
    
ind1 = TrianguloAG(12)
ind1.inicializa()
print(ind1)    
        
        
        
        
        
        
