#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:55:54 2021

@author: gustavo
"""
import random
import numpy as np
import copy

objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o'] # Nuestra palabra objetivo 

class Gen():
    
    def Aptitud(self,individuo): # Se pedira el individuo     
        aptitud = 0 
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]: # Recorre cada caracter para buscar coincidencias
                aptitud+=1  # Si hay coincidencias, incrementa aptitud
            indice +=1  # Incrementa el indice en uno para seguir con busca de coincidencias
        return aptitud + 1e-4   # Se pone e-4, para que no sea cero, y hacer operaciones despues

    
    def Aptitud2(self, individuo):
        aptitud = 0
        indice = 0
        for letra in objetivo:
                        

    
    def inicializa(self, tamCad, numeroInd): # Se pedirá el tamañoCadena y NumeroDeIndividuos
        self.tamCad = tamCad
        # Se hace el cromosoma del tamaño que se desee con letras aleatorias
        self.cromosoma = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '], k = tamCad)

        poblacion = [] # Se reserva espacio para la poblacion
        for i in range(numeroInd):  
            individuo = self.cromosoma # Se asigna cada individuo a cromosoma
            poblacion.append(individuo) # Se agregan los individuos para obtener la poblacion
    
        aptitudes = [] # Se reserva espacio para las aptitudes
        for individuo in poblacion:
            aptitudes.append(self.Aptitud(individuo)) # Se hace el calculo de cada aptitud en cada individuo
        
        for i in range(len (poblacion)):
            self.aptitudes = aptitudes[i] # Se guarda cada aptitud en aptitudes

        aptitudes2 = []
        for individuo in poblacion:
            aptitudes2.append(self.Aptitud2(individuo))

    
    def __str__(self):
        # Se imprime el resultado en pantalla de los individuos y su fitnes respectivo
        return "Individuo: "+str(self.cromosoma)+" ----> Fitness: "+str(self.aptitudes)
    
    def Mutar(self, n):
        pass
    
    def Cruzar(self, otro, fitnessFunction=None):
         # Creación de los padres
        padre = self.cromosoma
        madre = otro.cromosoma

        # CRUZA POR DOS PUNTOS
        cp1 = int(np.ceil(len(padre))/3)
        cp2 = int(2*cp1)        
        hijo1 = padre.copy()
        hijo2 = madre.copy()
    
        medio1 = madre[cp1:cp2]
        medio2 = padre[cp1:cp2]
        hijo1[cp1:cp2] = medio1 
        hijo2[cp1:cp2] = medio2
        
        h1 = copy.deepcopy(self) # Clona el objeto actual
        h1.cromosoma = hijo1
        
        h2 = copy.deepcopy(otro)
        h2.cromosoma = hijo2
        
        if fitnessFunction is None:
            return [h1,h2]
        aptitudPadre = fitnessFunction(self)
        aptitudMadre = fitnessFunction(otro)
        aptitudHijo1 = fitnessFunction(h1)
        aptitudHijo2 = fitnessFunction(h2)
        
        while aptitudHijo1 < aptitudMadre or aptitudHijo1 < aptitudPadre or aptitudHijo2 < aptitudMadre or aptitudHijo2 < aptitudPadre:    
            h1 = Cromosoma()
            h1.inicializa(self.tamCad,self.numeroInd)
            h2 = Cromosoma()
            h2.inicializa(self.tamCad, self.numeroInd)
            aptitudHijo1 = fitnessFunction(h1)                
            aptitudHijo2 = fitnessFunction(h2)                
        return [h1,h2]

class Cromosoma():
    
    def __init__(self):    
        pass

    def inicializa(self,nGenes):
        # Se crea espacio para los genes
        genes = []
        for i in range (nGenes): # En TestLab01 se pedirá cuanfos genes desarrollaran
             g = Gen()  # Se crean los objetos
             g.inicializa(10,5) # Se inicializan los objetos (de tamaño 10 y 5 individuos)
             genes.append(g)    # Se agrega cada objeto a genes
        self.genes = genes # Se agrega a genes
        
    #def mutar(self):
        #for gen in self.genes:
            #gen.Mutar(n)
    
    def Cruzar(self, otro):
        h1 = copy.deepcopy(self)
        h2 = copy.deepcopy(otro)        
        genesHijos1 = []
        genesHijos2 = []

        for i in range(len(self.genes)):
            GenPadre = self.genes[i]
            GenMadre = otro.genes[i]
            genHijos = GenPadre.Cruzar(GenMadre)
            genesHijos1.append(genHijos[0])
            genesHijos2.append(genHijos[1])
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]
    
    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + str(gen) + "\n" # Se imprimen los genes
        return cad



