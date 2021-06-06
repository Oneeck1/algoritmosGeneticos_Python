#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:36:03 2021

@author: gustavo
"""


'''
LISTO Usuario digite su contraseña la cual puede llevar cualquier caracter
LISTO Convertir la contraseña op1 codigo binaio opc2 codigo gray
PENDIENTE fitness que va hacer con una ec simple 
(el cual se va a calcular si el numero de coincidentes)
y se va acalcular de la siguiente manera
supongamos que la cadena que se digita es "hi word", su conversion es:
01101000011010010010000001110111011011110111001001100100-> longitud 56
ahora el programa lo que genera son cadenas de longitud 56 ocea de la long del usuario digitada
el fitness lo calcularemos haciendo que esta cadena la divide uno a uno ya casi esta
y la compare con cada individuo que genera el programa y por cada que acierte se va a ir suamando
y un contador incrementa y se le saque el porcentaje con la regla de 3
56 es el 100% y si el programa acerto 34 entonces seria 60.7% 

FITNESS INDIVIDUO

# pendiente agregar el numero de parecidos en el fitnes (se va realizar tomando en cuenta el punto anterior)

Definir los if  que van a depender de el numero de generaciones
aquí tengo en mente hacer un proedio general por generacion
ejemplo el ppromedio de una generacion de 5 individuos es de 500%
pero la generacion acumulada solo alcanzó un 370 sumando todos los porcentajes
se hace la regla de 3 del porcentaje total que es 500 - el ejemplo 436 y da 64 

Funcion de paro de generaciones 
si el num es mayor a tal o menor se hace el paro


50
89
70

total 209
lo perfecto seria 300

91 
1.- que si ya esta casi perfecto pare
2.- si la sol se sesga en el mismo fitness total que pare



'''

import numpy as np
import random
from os import system

#Creamos la clase de AG en el que ponemos los parametros iniciales 
class DNA():
    def __init__(self, target,prob_mut, num_indiv, num_selec, num_gener, verbose = True):
    #Definoms las variables que se van a ocupar en el AGS
        self.target = target 
        self.prob_mut = prob_mut
        self.num_indiv = num_indiv
        self.num_selec = num_selec
        self.num_gener = num_gener
        self.verbose = verbose
    
    
    #Generamos el individuo
    def crear_individuo(self,min =0, max =2): #Definimos el maximo y el  minimo de del los limites para generar random 
        individuo = [np.random.randint(min,max) for i in range(len(self.target))] #Conjunto de numeros del largo de nuestro de objetibo
        return individuo
    
    #Generamos la poblacion
    def crear_poblacion(self):
        poblacion = [self.crear_individuo() for i in range(self.num_indiv)]
        return poblacion

    #Evaluamo el individuo
    def fitness(self, individual):
        fitness = 0
        for i in range(len(individual)):
            if individual[i] == self.target[i]:
                fitness += 1
        return fitness


    def seleccion(self, poblacion):
        #Para que no solo nos muestre el fitnes de coincidencia de eleento por elemento tambien le pasamos el individuo 
        scores = [(self.fitness(i), i) for i in poblacion]
        #Ahora tenemos que seleccionar los individuos con el mejor fitness que lo def con num_selec = 2 individuos
        scores = [i[1] for i in sorted(scores)]
        
        '''
        SCORE: Mejores Alelos
        FALTA: IMPRIMIR El Score junto a su individuo        
        '''
        
        #seleccion elitista
        seleccionados = scores[len(scores) - self.num_selec: ]
        return seleccionados


    def reproduccion(self, poblacion, seleccionados):
        punto = 0
        padre = []

        for i in range(len(poblacion)):
            punto = np.random.randint(1, len(self.target) -1) #hacemos que cambien los de enmedio
            padre = random.sample(seleccionados, 2) #Numero de padres que quiero para hacer la nueva generacion 
        #Metodo de cruce a un punto (hacuendo que lo que se cambie sea intermedio)
            poblacion[i][:punto] = padre[0][:punto]
            poblacion[i][punto:] = padre[1][punto:]

        return poblacion

    def mutacion(self,poblacion):
        for i in range(len(poblacion)):
            if random.random() <= self.prob_mut:
                punto = random.randint(1, len(self.target) - 1)
                nuevo_valor = np.random.randint(0,2)
                while nuevo_valor == poblacion[i][punto]:
                    nuevo_valor = np.random.randint(0,2)
                poblacion[i][punto] = nuevo_valor

            return poblacion
    
    def ascii_to_bin(self, char):
        ascii = ord(char)
        bin = []
        while (ascii > 0):
            if (ascii & 1) == 1:
                bin.append("1")
            else:
                bin.append("0")
            ascii = ascii >> 1
        bin.reverse()
        binary = "".join(bin)
        zerofix = (8 - len(binary)) * '0'
        return zerofix + binary

    def ejecutar(self):

        poblacion = self.crear_poblacion()
        seleccionados = self.seleccion(poblacion)

        for i in range(self.num_gener):
            if self.verbose:
                print('\n________________________________________________________________________________________________________________')
                print("\nGeneracion:", i+1)
                print("Poblacion: \n", poblacion)
                print("Seleccion: \n", seleccionados)
            
    
            poblacion = self.reproduccion(poblacion, seleccionados)
            poblacion = self.mutacion(poblacion)


def main():
    system("cls")
    print("\n")
    print("************************INICIO DEL PROGRAMA***********************************")
    String = input("\n\nDigite su contraseña a revisar:")
    binary = []
    model1 = DNA(target = binary, prob_mut = 0.2, num_indiv = 5, num_selec= 3, num_gener = 10, verbose= True)
    for char in String:
        binary.append((model1.ascii_to_bin(char)))
    a = ("".join(binary))
    print("Su contrasenia en binario es:", a)
    print("\nComenzemos con las generaciones... \n")
    system("pause")
    target = a        
    model = DNA(target = target, prob_mut = 0.2, num_indiv = 4, num_selec= 2, num_gener = 4, verbose= True)
    model.ejecutar()
    print("\nSu contraseña es: Fuerte\n")
    print("************************FIN DEL PROGRAMA***********************************")

if __name__ == '__main__':
    main()