#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:55:54 2021

@author: gustavo
"""
import random


class Gen():
    
    def inicializa(self, tamCad):
        self.tamCad = tamCad
        self.cromosoma = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k = tamCad)

    def Aptitud(self,individuo):
        objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
        aptitud = 0
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]:
                aptitud+=1
                indice +=1
        return aptitud + 1e-4


    def Poblacion(self, numero):
        poblacion = []
        for i in range(numero):
            individuo = self.cromosoma
            poblacion.append(individuo)
        return poblacion
    
            
    def aptitudIndividuos(self):
        aptitudes = []
        for individuo in self.poblacion:
            aptitudes.append(self.Aptitud(individuo)) 
        return aptitudes

    def __str__(self):
        return "Individuo: "+str(self.poblacion)+" ----> Fitness: "+str(self.aptitudes)
    
    def Mutar():
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
             g.inicializa(10)
             genes.append(g)
        self.genes = genes
        
    def mutar():
        pass
    
    def cruzar():
        pass
    
    def __str__():
        pass
    
    def fenotipo():
        pass



