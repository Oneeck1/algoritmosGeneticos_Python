#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:06:34 2021

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


