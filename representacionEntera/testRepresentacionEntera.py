#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:20:45 2021

@author: gustavo
"""

from cromosomaEntero import Entero

ind = Entero()

ind.inicializa(0,10)

print(ind.cromosoma)
print(ind.fenotipo())
