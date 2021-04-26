#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:44:07 2021

@author: gustavo
"""

import random

class Gen:
    
    def __init__(self):
        self.tamCad = 10
    
    
    def Aptitud(individuo):
        objetivo = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
        aptitud = 0
        indice = 0
        for letra in objetivo:
            if letra == individuo[indice]:
                aptitud+=1
                indice +=1
        return aptitud + 1e-4                
                
    def cruza(self, otro):
        padre = self.cromosoma
        madre = otro.cromosoma
        # Crear hijos con cruza por dos puntos
        
        h1 = padre[0]+madre[1:5]+padre[5]
        h2 = madre[0]+padre[1:5]+madre[5]
        
        hijoUno = Cromosoma()
        hijoDos = Cromosoma()

        hijoUno.Cromosoma = h1
        hijoDos.Cromosoma = h2

        return [hijoUno, hijoDos]         


    
class Cromosoma:
    genes = []
    gen = Gen() 
    genes.append(gen)

