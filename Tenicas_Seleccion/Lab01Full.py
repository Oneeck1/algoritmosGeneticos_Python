#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:55:54 2021

@author: gustavo
"""
import random


class Gen():
    
    def Aptitud(self,individuo):
        objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
        aptitud = 0
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]:
                aptitud+=1
                indice +=1
        return aptitud + 1e-4

    
    def inicializa(self, tamCad, numeroInd):
        self.tamCad = tamCad
        self.cromosoma = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k = tamCad)

        poblacion = []
        for i in range(numeroInd):
            individuo = self.cromosoma
            poblacion.append(individuo)
    
        aptitudes = []
        for individuo in poblacion:
            aptitudes.append(self.Aptitud(individuo)) 
        
        for i in range(len (poblacion)):
            self.aptitudes = aptitudes[i]

    
    def __str__(self):
        
        return "Individuo: "+str(self.cromosoma)+" ----> Fitness: "+str(self.aptitudes)
    
    def Mutar(self, n):
        pass
    
    def Cruzar():
        pass    
    
    def Fenotipo():
        pass

class Cromosoma():
    
    def __init__(self):    
        pass

    def inicializa(self,nGenes):
        genes = []
        for i in range (nGenes):
             g = Gen()
             g.inicializa(10,5)
             genes.append(g)
        self.genes = genes
        
    #def mutar(self):
        #for gen in self.genes:
            #gen.Mutar(n)
    
    def cruzar():
        pass
    
    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + str(gen) + "\n"
        return cad
    
    def fenotipo():
        pass



