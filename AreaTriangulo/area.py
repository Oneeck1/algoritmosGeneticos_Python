#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:23:13 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS 2021
TEMA: Representación de soluciones numéricas para AG con POO
ALUMNO: GUSTAVO RODRIGUEZ CALZADA
PROFESOR: ASDRÚBAL LÓPEZ CHAU

DESCRIPCIÓN: Area Máxima de un triangulo

@author: gustavo
"""
import random
import numpy as np

class Gen():
    
    def __init__(self):
        pass
    
    def inicializa(self, P, numeroInd):
        self.P = P
        vMin = P/100.0
        vMax = P-2
        self.cromosoma = [random.uniform(vMin,vMax)for i in range(0,3)]
        
        poblacion = [] # Se reserva espacio para la poblacion
        for i in range(numeroInd):  
            individuo = self.cromosoma # Se asigna cada individuo a cromosoma
            poblacion.append(individuo) # Se agregan los individuos para obtener la poblacion
        
        aptitudes = [] # Se reserva espacio para las aptitudes
        for individuo in poblacion:
            aptitudes.append(self.Aptitud()) # Se hace el calculo de cada aptitud en cada individuo
        
        for i in range(len(poblacion)):
            self.aptitudes = aptitudes[i] # Se guarda cada aptitud en aptitudes

    def __str__(self):
        lados = self.cromosoma
        return "P = "+str(self.P)+"\nA: "+str(lados[0])+", \nB: "+str(lados[1])+", \nC: "+str(lados[2])+", \nAptitud: "+str(self.aptitudes)
    
    def Aptitud(self):
        A = self.cromosoma[0]
        B = self.cromosoma[1]
        C = self.cromosoma[2]
        S = ((A+B+C)/2)
        alpha = 0.5
        perimetro = (A+B+C)

        if S>A and S>B and S>C:
            
            aptitud = np.sqrt( S * (S-A) * (S-B) * (S-C) )
                
            if( perimetro > self.P):
                aptitud = aptitud * np.exp(-alpha * np.abs(self.P - (A + B + C)))
        
        else: 
            aptitud = 1e-6
        
        return aptitud
        

class Cromosoma():
    
    def __init__(self):    
        pass

    def inicializa(self,tamP,nPob=1):
        # Se crea espacio para los genes
        genes = []
        for i in range (nPob): # En TestLab01 se pedirá cuanfos genes desarrollaran
             g = Gen()  # Se crean los objetos
             g.inicializa(tamP,1) # Se inicializan los objetos (de tamaño 10 y 5 individuos)
             genes.append(g)    # Se agrega cada objeto a genes
        self.genes = genes # Se agrega a genes

    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + str(gen) + "\n\n" # Se imprimen los genes
        return cad
