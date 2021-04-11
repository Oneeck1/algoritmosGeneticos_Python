#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:15:54 2021

@author: gustavo
"""

import numpy as np
import random
import math


vMin = -1.0
vMax = 4

v = max([vMin, vMax])

#print("Valor Máximo")
#print(v)

print("N Bits")
nbits = int(np.ceil(np.log(v + 1)/np.log(2)) + 1)
print(nbits)

#print("Numeros 0 y 1")
entero = random.choices([0, 1], k = nbits)
#print(entero)
entero = str(entero[:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
fraccion = random.choices([0, 1], k = nbits+2)
fraccion = str(fraccion[:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
#print(cromosoma)

"""
print("Numeros aleatorios punto flotante")
cromosoma = random.uniform (vMin, vMax)
print(cromosoma)
"""

print("Entero: ")
print(entero)

print("Decimal")
print(fraccion)

print("Numero Completo: ")
numCom = str(entero)+"."+str(fraccion)
print(numCom)

print("Entero Convertido: ")
entero = int(entero,2)
print(entero)


print("Fraccion Convertida: ")
#decimal_binario = []
aux=fraccion*2
#valor= int(round(fraccion,2))
aux=round(fraccion,2) * 2
#decimal_binario.append(valor)
print(aux)





