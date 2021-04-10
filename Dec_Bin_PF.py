#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:55:45 2021

@author: gustavo
"""

import numpy as np
import random

vMin = 0.
vMax = 8.

v = max([vMin, vMax])

print("Valor Máximo")
print(v)

print("N Bits")
nbits = int(np.ceil(np.log(v + 1)/np.log(2)) + 1)
print(nbits)

print("Numeros 0 y 1")
cromosoma = random.choices([0, 1], k = nbits)
print(cromosoma)

print("Numeros aleatorios punto flotante")
cromosoma = random.uniform (vMin, vMax)
print(cromosoma)

print("Numero Convertido")
al = bin(int(cromosoma))
print(al)


