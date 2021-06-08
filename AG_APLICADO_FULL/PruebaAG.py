#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:37:14 2021

@author: gustavo
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import random
from os import system

class DNA():
    def __init__(self, target,prob_mut, num_indiv, num_selec, num_gener, verbose = True):
        self.target = target
        self.prob_mut = prob_mut
        self.num_indiv = num_indiv
        self.num_selec = num_selec
        self.num_gener = num_gener
        self.verbose = verbose
    
    def crear_individuo(self,min =0, max =2): #Definimos el maximo y el  minimo de del los limites para generar random 
        individuo = [np.random.randint(min,max) for i in range(len(self.target))] #Conjunto de numeros del largo de nuestro de objetibo
        return individuo
    
    def crear_poblacion(self):
        poblacion = [self.crear_individuo() for i in range(self.num_indiv)]
        return poblacion

    def fitness(self, individual):
        fitness = 0
        for i in range(len(individual)):
            if individual[i] == self.target[i]:
                fitness += 1
        return fitness

    def seleccion(self, poblacion):
        scores = [(self.fitness(i), i) for i in poblacion]
        scores = [(i[0], i[1]) for i in sorted(scores)]
        print(scores)

def main():
    target= [1, 0, 1, 0]
    model = DNA(target = target, prob_mut = 0.2, num_indiv = 4, num_selec= 2, num_gener = 4, verbose= True)
    model.seleccion(model.crear_poblacion())

if __name__ == '__main__':
    main()