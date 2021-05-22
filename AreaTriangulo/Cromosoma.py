#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:15:10 2021

@author: gustavo
"""


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
