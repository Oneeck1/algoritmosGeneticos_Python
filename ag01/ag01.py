#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:43:36 2021
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CENTRO UNIVERSITARIO UAEM ZUMPANGO
INGENIERÍA EN COMPUTACIÓN
ALGORITMOS GENÉTICOS
Alumno: Gustavo Rodrígez Calzada
Profesor: Asdrúbal Lopez Chau

Descripcion: Implementa algoritmo genético





Ejercicio: Crear un algoritmo genético para "adivinar" una contraseña de 
4 vocales

ejemplo:
    password: aeio
    
SOLUCIÓN:    
    PASO1:
        Cromosoma: 4 genes; cada gen es una vocal
        Valores alelicos: a,e,i,o
        
    PASO2:
        Función objetivo: Entre más parecido sea un individuo al password,
        tendrá mayor aptitud
        
    PASO3:
        Operadores Genéticos:
            Cruza:                
            Mutación: 
                Tomar un gen aleatoriamente y cambiar por otra vocal
                Cambiar de posición 2 genes
                Invertir la cadena



@author: gustavo
"""
from cromosoma import Cromosoma as cromos
from numpy import array 

listaInd = array()

c = cromos()
# c.mutacion()
# c.printCromosoma()

#1) Generar N individuos
N = 10
len(listaInd)

#2) Inicializar aleatoriamente a los individuos
def individuos(N):
    for i in range(N):    
        listaInd[i] = c.printCromosoma()

individuos(N)    
#3) Imprimir la póblación


#4) Aplicar elitismo (agregarlo a la siguiente poblacion)


#5) Cruzar individuos de la poblacion actual y generar N hijos



#6) Agregar a los N hijos a la siguiente población



#7) Mutar al 5% esta nueva poblacion (elegido aleatoriamente)



#8) Ir al paso 3, y repetir el proceso 10 veces



#9) Elegir el mejor individuo