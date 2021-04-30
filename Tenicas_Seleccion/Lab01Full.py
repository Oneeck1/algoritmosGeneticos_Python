#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:55:54 2021

@author: gustavo
"""
import random
import numpy as np

class Gen():
    
    def Aptitud(self,individuo): # Se pedira el individuo 
        objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o'] # Nuestra palabra objetivo 
        aptitud = 0 
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]: # Recorre cada caracter para buscar coincidencias
                aptitud+=1  # Si hay coincidencias, incrementa aptitud
            indice +=1  # Incrementa el indice en uno para seguir con busca de coincidencias
        return aptitud + 1e-4   # Se pone e-4, para que no sea cero, y hacer operaciones despues

    
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
        cp1 = int(np.ceil(padre)/3)
        cp2 = int(2*cp1)        
        hijo1 = padre.copy()
        hijo2 = madre.copy()
    
    
    
    def Fenotipo():
        pass

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
    
    def cruzar():
        pass
    
    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + str(gen) + "\n" # Se imprimen los genes
        return cad
    
    def fenotipo():
        pass



