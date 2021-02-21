#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:43:36 2Null21
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
from fitness import printFitness
from operator import itemgetter

# Lista para los individuos 
listaInd = []
eli = []

c = cromos()
password = "aeio"


#1) Generar N individuos
N = 10

#2) Inicializar aleatoriamente a los individuos

for i in range(N):    
    listaInd.append(c.generarCadena())


for uno in range(0,10):
    #3) Imprimir la póblación
    print('---------------------POBLACION----------------------')
    for i in range(N):
        print("Individuo ",i,": ",listaInd[i])

    poblacion = cromos()

    #4) Aplicar elitismo (agregarlo a la siguiente poblacion)
    print('---------------------ELITISMO----------------------')
    for i in listaInd:      
        poblacion = i
        aptitud = 0
        for j in range(0,len(i)): # Un for para recorrer cada uno de los individuos
            if password[j] == poblacion[j]: # Revisa caracter por caracter
                aptitud += 1 # Si es igual un caracter, suma 1
                print(poblacion + "->" + str(aptitud)) # Imprime el resultado
                eli.append(aptitud) # Guarda en una lista los valores de las aptitudes
    maximo_sort = sorted(enumerate(eli), key=itemgetter(1), reverse=True) # Conocer el valor maximo y en que posicion
    index, value = maximo_sort[0] # Se guardan en 2 variables
    print("Indice: {}, Valor Maximo: {}".format(index,value)) # Imprime los datos
    valorM = listaInd[index] # De la lista original, tomar el indice de donde es más alto la aptitud
    print("EL VALOR MAYOR ES: {}".format(valorM)) # Lo imprime


    #5) Cruzar individuos de la poblacion actual y generar N hijos
    print('---------------------GENERAR N HIJOS----------------------')

    madre = cromos()
    padre = cromos()
    poblacion2 = cromos()
    hijos = padre.cruza(madre)
    numHijos = 2
    for h in range(0,numHijos):
        print("Hijo {}: ".format(h))
        hijos[h].printCromosoma()
        poblacion2 = (hijos[h])    
        
    #6) Agregar a los N hijos a la siguiente población
            
            # Hecho en el paso anterior

            
    #7) Mutar al 5% esta nueva poblacion (elegido aleatoriamente)
    poblacion2.mutacion()
    print(poblacion2)
    #8) Ir al paso 3, y repetir el proceso 1Null veces

