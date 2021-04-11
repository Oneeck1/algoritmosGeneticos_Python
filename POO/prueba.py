#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:37:37 2021

@author: gustavo
"""

import numpy as np
import random
import math

vMin = -1.0
vMax = 4

v = max([vMin, vMax])

nbits = int(np.ceil(np.log(v + 1)/np.log(2)) + 1) # Saber cuantos bits ocupo para parte entera
        
        
# Numeros aleatorios punto flotante
NumAl = random.uniform (vMin, vMax)
print(NumAl)
                                        
#        self.cromosoma = random.choices([0, 1], k = self.nbits)
entero = random.choices([0, 1], k = nbits)
decimal = random.choices([0, 1], k = nbits+4)

entero2 = entero
decimal2 = decimal 
ent = str(entero2[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
dec = str(decimal2[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')


numEntero = str(entero)+"."+str(decimal)

print(numEntero)


cad = str(numEntero[1:]).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
print("Nuevo:")
print(cad)
cadena = list(cad)
print("CADENA")
print(cadena)

# ///////////////////////////////////////////////////////////////////////////////////////////////


#         parte_entera=binario(entero)
#         parte_decimal=binario_decimal(decimal)



