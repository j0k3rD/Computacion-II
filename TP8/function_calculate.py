'''
Realizar un programa en python que reciba por argumentos:

    -p cantidad_procesos
    -f /ruta/al/archivo_matriz.txt
    -c funcion_calculo

El programa deberá leer una matriz almacenada en el archivo de texto pasado por argumento -f, 
y deberá calcular la funcion_calculo para cada uno de sus elementos.

Para aumentar la performance, el programa utilizará un Pool de procesos, y cada proceso del pool 
realizará los cálculos sobre una de las filas de la matriz.

La funcion_calculo podrá ser una de las siguientes:

    raiz: calcula la raíz cuadrada del elemento.
    pot: calcula la potencia del elemento elevado a si mismo.
    log: calcula el logaritmo decimal de cada elemento.
'''


#Importando librerias necesarias.
from multiprocessing import Pool
import os
import time
import argparse
import math

#Creacion de la funcion Main, donde se ejecutaran todos lo metodos del programa.
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',type=str,help="Enter the number of processes to create. EJ: '2', '5'")
    parser.add_argument('-f',type=str,help="Enter the file path. EJ: '/home/user/Documents/test.txt.'")
    parser.add_argument('-c',type=str,help="Select the function to calculate:   .root  .pot  .log")
    args = parser.parse_args()
    
    if args.c == "root":
        #Ejecuta la funcion root() con cada elemento de la lista
        results = pool.map(root, range(len(args.f)))
        print(results)

    elif args.c == "pot":
        #Ejecuta la funcion pot() con cada elemento de la lista
        results = pool.map(pot, range(len(args.f)))
        print(results)

    elif args.c == "log":
        #Ejecuta la funcion log() con cada elemento de la lista
        results = pool.map(log, range(len(args.f)))
        print(results)


    #Metodo que calcula la raiz de c/u de los elementos del file
    def root(args):
        for i in range(len(args.f)):
            res = math.sqrt(i)
            return res
    
    #Metodo que calcula la potencia de c/u los elementos del file
    def pot(args):
        for i in range(len(args.f)):
            res = math.pow(i)
            return res

    #Metodo que calcula el logaritmo de c/u de los elementos del file 
    def log(args):
        for i in range(len(args.f)):
            res = math.log(i)
            return res

    #Creo mi pool con n procesos
    pool = Pool(processes=(args.p))

if __name__=='__main__':
    main()