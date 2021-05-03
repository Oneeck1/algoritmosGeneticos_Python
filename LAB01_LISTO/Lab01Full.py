#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Prueba cromosomas POO

Created on Mon Mar 22 13:31:09 2021

@author: gustavo
"""
import random
import numpy as np
import copy

objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o'] # Nuestra palabra objetivo 

class Gen():
    # NOS DICE LAS COINCIDENCIAS EN LA POSICION EXACTA 
    def Aptitud(self,individuo): # Se pedira el individuo     
        aptitud = 0 
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]: # Recorre cada caracter para buscar coincidencias
                aptitud+=1  # Si hay coincidencias, incrementa aptitud
            indice +=1  # Incrementa el indice en uno para seguir con busca de coincidencias
        return aptitud + 1e-4   # Se pone e-4, para que no sea cero, y hacer operaciones despues

    # NOS MUESTRA EL NUMERO DE CARACTERES IGUALES (SIN IMPORTAR EL ORDEN)
    def Aptitud2(self, individuo):
        aptitud2 = 0
        indice = 0
        for letraa in objetivo:
            if letraa in individuo: # Verifica si la letra está en todo el individuo, y suma si hay
                aptitud2 += 1                               
            indice += 1
        return aptitud2 + 1e-4  # Se guarda en aptitud, y se pone e-4, para que no haya problemas en los calculos por el cero
    
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
        
        for i in range(len(poblacion)):
            self.aptitudes = aptitudes[i] # Se guarda cada aptitud en aptitudes

        aptitudes2 = []
        for individuo in poblacion:
            aptitudes2.append(self.Aptitud2(individuo)) # Se hace el calculo de cada aptitud2 en cada individui
            
        for i in range(len(poblacion)):
            self.aptitudes2 = aptitudes2[i] # Se guarda cada aptitud en aptitudes2

    
    def __str__(self):
        # Se imprime el resultado en pantalla de los individuos y su fitnes respectivo
        crom = self.cromosoma
        crom = str(crom[1:]).replace('[', '').replace(']', '').replace(',', '').replace("'","")
        return "Individuo:   "+str(crom)+" ---> Fitness: "+str(self.aptitudes)+", Fitness2: "+str(self.aptitudes2)
    

    
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
        
        h2 = copy.deepcopy(otro) # Clona el nuevo objeto
        h2.cromosoma = hijo2
        
        if fitnessFunction is None:
            return [h1,h2]  # Se retornan los hijos
        aptitudPadre = fitnessFunction(self)
        aptitudMadre = fitnessFunction(otro)
        aptitudHijo1 = fitnessFunction(h1)
        aptitudHijo2 = fitnessFunction(h2)
        
        while aptitudHijo1 < aptitudMadre or aptitudHijo1 < aptitudPadre or aptitudHijo2 < aptitudMadre or aptitudHijo2 < aptitudPadre:    
            h1 = Cromosoma()    # Se crea un objeto de tipo Cromosoma
            h1.inicializa(self.tamCad,self.numeroInd) # Se inicializas
            h2 = Cromosoma()    # Se crea un objeto de tipo Cromosoma
            h2.inicializa(self.tamCad, self.numeroInd) # Se inicializa
            aptitudHijo1 = fitnessFunction(h1)                
            aptitudHijo2 = fitnessFunction(h2)                
        return [h1,h2] # Se retornan los hijos

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



