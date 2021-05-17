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

from Cromosomas import Cromosoma 
import numpy as np

class Triangulo:
    def __init__(self, perimetro):
        self.a = 0
        self.b = 0
        self.c = 0
        
        self.perimetro = perimetro
    def __str__(self):
        return "a = {:.3f}, b = {:.3f} c = {:.3f}".format(self.a, self.b, self.c)
    
    def setLados(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = self.a + self.a + self.c
        s = s/2.0
        tempo = s*(s-self.a)*(s-self.b)*(s-self.c)
        if tempo < 0:
            area =  -1.0
        else:
            area =  np.sqrt(tempo)
        return area

class TrianguloAG(Triangulo):
    
    def __init__(self, perimetro):
        super().__init__(perimetro)
        self.cromo = Cromosoma()
   
    def inicializa(self):
        perimetro = self.perimetro
        self.cromo.inicializa([perimetro/100.0, perimetro/100.0, perimetro/100.0], [perimetro, perimetro, perimetro],
                 [True, True, True])
        '''self.a = self.cromo.fenotipo()[0]
        self.b = self.cromo.fenotipo()[1]
        self.c = self.cromo.fenotipo()[2]
        '''
    
    def cruzar(self, madre):
        return self.cromo.cruzar(madre)
    
    def mutar(self):
        return self.cromo.mutar(1)
    
class FitnessFunctionTriangulo:
    
    def evaluate(self, individuo):
        TOL = 0.5
        alfa = 1
        area = individuo.area()
        perimetroRequerido = individuo.perimetro
        perimetroInd = individuo.a + individuo.b + individuo.c
        difPerimetro = np.abs(perimetroInd - perimetroRequerido)
        if area <= 0:
            return -1
        if area > 0:
            if difPerimetro < TOL:
                return area
            else:
                return area * np.exp(-difPerimetro*alfa)

class ProblemaTrianguloAG:
    
    def __init__(self,tamanoPoblacion, perimetro):
        self.N = tamanoPoblacion
        self.poblacion = []        
        self.ff = FitnessFunctionTriangulo()
        
        for i in range(self.N):
            tag = TrianguloAG(perimetro)
            tag.inicializa()
            self.poblacion.append(tag)

    def getAptitudes(self):
        aptitudes = []            
         for ind in self.poblacion:
             apt = self.ff.evaluate(ind)
             aptitudes.append(apt
            
    def printPoblacion(self):
        for ind in self.poblacion:
            print(ind)
            
    def evolve(self):
        pass
    
    
ind1 = TrianguloAG(12)
ind1.inicializa()
ff = FitnessFunctionTriangulo()
ind1.setLados(3,3,3)
print(ind1)    
print(ff.evaluate(ind1))
        
        
        
        
        
        
