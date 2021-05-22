#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:44:04 2021

@author: gustavo
"""


import math

# PARTE ENTERA
def binario(num):
    co=0
    resto = 0
    numero_binario = []
 
    if num <= 1:
        print("no se puede convertir")
    else:
        while num > 1:
            #co = num //2
            resto=num%2
            numero_binario.append(resto)
            num=num//2
        numero_binario.append(1)
        numero_binario.reverse()
        return numero_binario
 
    
# PARTE FRACCIONARIA    
def binario_decimal(decimal):
 
    aux=decimal*2
    decimal_binario=[]
    lista=[]
    valor=0
    while aux not in lista :
            lista.append(aux)
            partes=math.modf(aux)
            valor= int(round(partes[1],2))
            decimal_binario.append(valor)
            if int(round(partes[1],2)) == 1 and round(partes[0],2)== 0.0:
                break
            aux=round(partes[0],2) * 2
 
    return decimal_binario
 
 
 
 
def entero_decimal():
    global entero
    global decimal
    global numero
    numero=float(input("Ingrese un número: "))
    partes=math.modf(numero)
    decimal=round(partes[0],2)
    entero=int(partes[1])
    if decimal == 0.0:
        print("El número decimal {} es en binario {}]" .format(int(numero) ,binario(entero)))
    else:
        parte_entera=binario(entero)
        parte_decimal=binario_decimal(decimal)
        print("El número decimal {} es en binario {}.{}" .format(int(numero) ,parte_entera,parte_decimal))
 
entero_decimal()