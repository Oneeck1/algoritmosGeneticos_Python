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


class Gen():
    
    def __init__(self):
        pass
    
    def inicializa(self, P):
        vMin = P/100.0
        vMax = P-vMin
        self.cromosoma = [random.uniform(vMin,vMax)for i in range(0,3)]

    def __str__(self):
        lados = self.cromosoma
        return "A: "+str(lados[0])+", B: "+str(lados[1])+", C: "+str(lados[2])

class Cromosoma():
    
    def __init__(self):    
        pass

    def inicializa(self,nPob):
        # Se crea espacio para los genes
        genes = []
        for i in range (nPob): # En TestLab01 se pedirá cuanfos genes desarrollaran
             g = Gen()  # Se crean los objetos
             g.inicializa(10) # Se inicializan los objetos (de tamaño 10 y 5 individuos)
             genes.append(g)    # Se agrega cada objeto a genes
        self.genes = genes # Se agrega a genes

    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + str(gen) + "\n" # Se imprimen los genes
        return cad
