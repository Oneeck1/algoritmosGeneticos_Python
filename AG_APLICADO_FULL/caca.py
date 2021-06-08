#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np
import random
from os import system


class cad():
    def __init__(self, contraseña):
        self.contraseña = contraseña
        
    def Fcontraseña (self):
        if self.contraseña <= 9:
            print("Su contraseña es débil")            
            g = 38
            return g
        elif self.contraseña >= 10 and self.contraseña <= 15: 
            print("Su contraseña es regular")
            g1 = 84
            return g1
        elif self.contraseña >= 16 and self.contraseña <= 25:
            print("Su contraseña es buena")
            g2 = 227
            return g2
        else: 
            print("Su contraseña es muy dificil de predecir")
            g3 = 376
            return g3



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
        for i in range(self.num_gener):
            if self.verbose:
                print('\n________________________________________________________________________________________________________________')
                print("Tu contraseña que pusiste fue: ",A)
                print("\nTu contraseña en binario de la Funcion Objetivo es: ",B)
                print("\nGeneracion:", i+1)
                print("Poblacion: \n", poblacion)
            seleccionados = self.seleccion(poblacion)
            poblacion = self.reproduccion(poblacion, seleccionados)
            poblacion = self.mutacion(poblacion)
    
            
def main():
    system("cls")
    print("\n")
    print("************************INICIO DEL PROGRAMA***********************************")
    String = input("\n\nDigite su contraseña a revisar:")
    binary = []
    C = len(String)
    cade = cad(C)
    ng = cade.Fcontraseña()
    
    model1 = DNA(target = binary, prob_mut = 0.2, num_indiv = 5, num_selec= 3, num_gener = ng, verbose= True)
    
    for char in String:
        binary.append((model1.ascii_to_bin(char)))
    a = ("".join(binary))
    print("Su contrasenia en binario es:",a)
    global A
    A = String
    global B
    B = a
    
    ventana=tk.Tk()
    ventana.title("Contraseña")
    ventana.geometry("1250x90")
    ventana.configure(background='black')

    etiqueta1=tk.Label(ventana,text="contraseña digitada",bg='red',fg="white")
    etiqueta2=tk.Label(ventana,text=String,bg='dark turquoise',fg="white")
    etiqueta3=tk.Label(ventana,text="contraseña convertida a binario",bg='red',fg="white")
    etiqueta4=tk.Label(ventana,text= a,bg='dark turquoise',fg="white")
    etiqueta1.pack()
    etiqueta2.pack()
    etiqueta3.pack()
    etiqueta4.pack()
    #ventana.mainloop()

    print("\nComenzemos con las generaciones... \n")
    system("pause")
    target = a
    model = DNA(target = target, prob_mut = 0.2, num_indiv = 4, num_selec= 2, num_gener = ng, verbose= True)
    model.ejecutar()
    #model.contraseña()
    #print("\nSu contraseña es: Fuerte\n")
    print("************************FIN DEL PROGRAMA***********************************")

if __name__ == '__main__':
    main()