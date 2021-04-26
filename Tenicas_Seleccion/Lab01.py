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
        self.cromosoma = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k = 10)
    
    def Aptitud(self,individuo):
        objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
        aptitud = 0
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]:
                aptitud+=1
                indice +=1
        return aptitud + 1e-4                
                    


    def inicializa(self, num):
        poblacion = []
        for i in range(int(num)):
            individuo = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k = int(self.tamCad))
            poblacion.append(individuo)
                        
        aptitudes = []
        for individuo in poblacion:
            aptitudes.append(self.Aptitud(individuo)) 
        return individuo
    

    def cruza(self, otro, aptitudd=None):
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
        
        if aptitudd is None:
            return [h1, h2] 
        aptitudPadre = aptitudd(self)
        aptitudMadre = aptitudd(otro)
        aptitudHijo1 = aptitudd(h1)
        aptitudHijo2 = aptitudd(h2)

        # Generar mejores hijos
        while aptitudHijo1 < aptitudPadre or aptitudHijo1 < aptitudMadre or aptitudHijo2 < aptitudPadre or aptitudHijo2 < aptitudMadre:
            h1.inicializa(self.tamCad)
            h2.inicializa(self.tamCad)
            aptitudHijo1 = aptitudd(h1)
            aptitudHijo2 = aptitudd(h2)
        return [h1,h2]
 

    def __str__(self):
        return "Individuo: "+str(self.individuo)+" ----> Fitness: "+str(self.aptitud)
        
        
    
class Cromosoma:
 
    
    
    def Aptitud(self,individuo):
        objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
        aptitud = 0
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]:
                aptitud+=1
                indice +=1
        return aptitud + 1e-4       
        

    def inicializa(self, n):
        poblacion = []
        for i in range(int(n)):
            individuo = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k = int(n))
            poblacion.append(individuo)
                        
        aptitudes = []
        for individuo in poblacion:
            aptitudes.append(self.Aptitud(individuo)) 
    
        genes = [] 
        g = Gen()
        g.inicializa(n)
        genes.append(g)            
        self.genes = genes
        return individuo
        
        

    def __str__(self):
        return "Individuo: "+str(self.inicializa(10))+" ----> Fitness: "+str(self.Aptitud(self.genes))
 

    def cruza(self, otro):
        '''
        Operador de cruza con otro gen

        :param `otro`: Otro cromosoma con la misma estuctura
        :returns: Dos hijos
        :rtype: Cromosma
        '''
        h1 = copy.deepcopy(self)
        h2 = copy.deepcopy(otro)        
        genesHijos1 = []
        genesHijos2 = []

        for i in range(len(self.genes)):
            GenPadre = self.genes[i]
            GenMadre = otro.genes[i]
            genHijos = GenPadre.cruza(GenMadre)
            genesHijos1.append(genHijos[0])
            genesHijos2.append(genHijos[1])
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]



