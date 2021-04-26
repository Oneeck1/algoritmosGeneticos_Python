#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:44:07 2021

@author: gustavo
"""

class Gen:
    
    
    def Aptitud(individuo):
        objetivo = ['c','a','f','e']
        aptitud = 0
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]:
                aptitud+=1
                indice +=1
        return aptitud + 1e-4 # Sumo para evitar los 0

    def cruza():
        
    
    
    
class Cromosoma:
    genes = []
    gen = Gen() 
    genes.append(gen)

