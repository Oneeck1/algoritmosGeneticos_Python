#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Solución de problemas con AG
ALUMNO: tu nombre
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: área máxima de un triangulo
de perímetro P  

Created on Mon May 17 13:08:30 2021

@author: asdruballopezchau
"""

# Agrega la ruta donde se encuentra el arhcivo que contiene
# la clase.

from Cromosomas2 import Cromosoma 
import numpy as np
import copy
import random

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
        p = self.perimetro
        self.cromo.inicializa([p/100.0, p/100.0, p/100.0], 
                              [p, p, p],
                              [True, True, True])
        '''self.a = self.cromo.fenotipo()[0]
        self.b = self.cromo.fenotipo()[1]
        self.c = self.cromo.fenotipo()[2]
        '''
    
    def cruzar(self, madre):        
        hijos = self.cromo.cruzar(madre)
        lados = hijos[0].fenotipo()
        a = lados[0]
        b = lados[1]
        c = lados[2]
        hijo1 = copy.deepcopy(self)
        hijo1.setLados(a, b, c)
        hijo2 = copy.deepcopy(madre)
        lados = hijos[1].fenotipo()
        a = lados[0]
        b = lados[1]
        c = lados[2]
        hijo2.setLados(a, b, c)
        return [hijo1, hijo2]
    
    def mutar(self):
        mutante = self.cromo.mutar(1)
        lados = mutante.fenotipo()
        a = lados[0]
        b = lados[1]
        c = lados[2]
        clon = copy.deepcopy(self)
        clon.setLados(a, b, c)
        return clon
    
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


class TecnicaSeleccion:    
    def selecciona(self, poblacion, aptitudes, cuantos):
        probs = np.exp(aptitudes)/ np.sum(np.exp(aptitudes))
        selected = random.choices(poblacion, probs, k=cuantos)
        return selected
    
class ProblemaTrianguloAG:
    
    def __init__(self, tamanoPoblacion, perimetro):
        self.N = tamanoPoblacion
        self.poblacion = []
        self.ff = FitnessFunctionTriangulo()
        self.tecSeleccion = TecnicaSeleccion()
        # 1) Genera N individuos TrianguloAG con lados aleatorios
        for i in range(self.N):
            tag = TrianguloAG(perimetro)
            tag.inicializa()
            self.poblacion.append(tag)
    
    def getAptitudes(self, pob=None):
        if pob is None:
            pob = self.poblacion
        aptitudes = []
        for ind in pob:
            apt = self.ff.evaluate(ind)
            aptitudes.append(apt)
        return aptitudes
    
    def elitismo(self):
        # Calcula todas las aptitudes
        aptitudes = self.getAptitudes()
        # Identifica la aptitud más alta
        maxApt = np.max(aptitudes)
        # Identifica en donde está el mejor individuo
        idx = aptitudes.index(maxApt)
        # Clonar al individuo
        mejor = self.poblacion[idx]
        clon =  copy.deepcopy(mejor)
        return clon
        
    def printPoblacion(self):
        for ind in self.poblacion:
            print(ind)
    
    def evolve(self):
        sigPoblacion = []
        # 2) Aplicar elitismo
        mejor = self.elitismo()
        sigPoblacion.append(mejor)
        # 3) Cruzar para generar hijos
        pobIntermedia = []
        for i in range(int(self.N/2)):
            padres = self.tecSeleccion.selecciona(self.poblacion, self.getAptitudes(), 2)
            papa = padres[0]
            mama = padres[1]
            hijos = papa.cruzar(mama)
            hijo1 = hijos[0]
            hijo2 = hijos[1]
            pobIntermedia.append(hijo1)
            pobIntermedia.append(hijo2)
            pobIntermedia.append(copy.deepcopy(mama))
            pobIntermedia.append(copy.deepcopy(papa))
        # 4) Mutación del 5% de la población
        totalMutar = int(np.ceil(0.05*len(pobIntermedia)))
        mutantes = self.tecSeleccion.selecciona(pobIntermedia, 
                                     self.getAptitudes(pobIntermedia), 
                                     totalMutar)
        mutados = []
        for mutante in mutantes:
            pobIntermedia.append(mutante.mutar())
        # En este punto pobIntermedia contiene padres, hijos y mutantes
        # 5) Crear nueva generación
        seleccionados = self.tecSeleccion.selecciona(pobIntermedia, self.getAptitudes(pobIntermedia), self.N-1)
        for seleccionado in seleccionados:
            clon = copy.deepcopy(seleccionado)
            sigPoblacion.append(clon)
        self.poblacion = sigPoblacion
    
prob = ProblemaTrianguloAG(20, 12)
prob.evolve()
#prob.printPoblacion()