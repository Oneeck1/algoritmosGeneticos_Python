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
    
    
    def inicializa(self):
        perimetro = self.perimetro
        self.cromo.inicializa(perimetro/100.0, perimetro/100.0, perimetro/100.0), [perimetro, perimetro, perimetro], [True,True,True]
        
    
    def cruzar(self,madre):
        self.cromo.cruzar(madre)
    
    
    def mutar(self):
        return self.cromo.mutar(1)
    
    

cromo  = Cromosoma()
perimetro = 10.0
cromo.inicializa(perimetro/100.0, perimetro/100.0, perimetro/100.0), [perimetro, perimetro, perimetro], [True,True,True]        
        
        
        
        
        
        
        
        
