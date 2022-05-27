## Ejercicio del TP8 - Uso de Pool() - OPERACIONES CON MATRICES

#Pool: En este caso vamos a llamar a un grupo de procesos. Puedo crear procesos idle y le damos tareas.

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
import numpy as np


lines = []
results = []
    

parser = argparse.ArgumentParser()
parser.add_argument('-p',type=str,help="Enter the number of processes to create. EJ: '2', '5'")
parser.add_argument('-f',type=str,help="Enter the file path. EJ: '/home/user/Documents/test.txt.'")
parser.add_argument('-c',type=str,help="Select the function to calculate:   .root  .pot  .log")
args = parser.parse_args()


#Metodo que me muestra en que elemento estoy realizando el cálculo.
def sumador(num):
    num = num+1

#Metodo que me muestra el proceso con el cual estoy realizando el cálculo.
def pid(num):
    return ("pid: %d - x=%d" % (os.getpid(), num))

#Metodo que me trae cada una de las lineas del archivo
def fd_lines(args):
    with open(args.f) as fd:
        for line in fd:
            strip_lines = line.strip('"')
            listli = strip_lines.split()
            m=lines.append(listli)
            '''
            Ocurria un error, los elementos se guardaban como 'str', por lo que ahora los convierto cada uno
            de ellos a 'int'.
            '''
            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    lines[i][j] = int(lines[i][j])


#Metodo que calcula la raiz de c/u de los elementos de los elementos de la linea de file
def root(num):
    time.sleep(1)    
    print("Process %d calculing root of %d" %(os.getpid(), num))
    return math.sqrt(num)


#Metodo que calcula la potencia de c/u de los elementos de los elementos de la linea de file
def pot(num):
    time.sleep(1)
    print("Process %d calculing root of %d" %(os.getpid(), num))
    return math.pow(num,num)


#Metodo que calcula el logaritmo de c/u de los elementos de los elementos de la linea de file
def log(num):
    time.sleep(1)
    print("Process %d calculing root of %d" %(os.getpid(), num))
    return math.log10(num)


#Creo mi pool con n procesos
pool = Pool(processes= int(args.p))


#Primero tengo que generar las listas (lines) de numeros que se le ingresaran a la operacion.
fd_lines(args)


#Metodo que inicia el calculo
def calculate(args):
    #Ejecuta la funcion que elija con cada linea de la lista
    for i in range(len(lines)):
        print("-------------------------------")
        #Con unos if decido que metodo aplicar para cada parametro en -c que se ingrese.
        if args.c == "root":
            print("CALCULATE ROOT\n")
            #! NO PUEDO HACER QUE UN PROCESO HAGA TODA UNA LINEA DE LA MATRIZ
            result = pool.map(root,lines[i])
            #Guardo el elemento dentro de mi lista de resultados
            results.append(result)
            continue
        elif args.c == "pot":
            print("CALCULATE POWER\n")
            #! NO PUEDO HACER QUE UN PROCESO HAGA TODA UNA LINEA DE LA MATRIZ
            result = pool.map(pot,lines[i])
            #Guardo el elemento dentro de mi lista de resultados
            results.append(result)        
            continue
        elif args.c == "log":
            print("CALCULATE LOGARITHM\n")
            #! NO PUEDO HACER QUE UN PROCESO HAGA TODA UNA LINEA DE LA MATRIZ
            result = pool.map(log,lines[i])
            #Guardo el elemento dentro de mi lista de resultados
            results.append(result)
            continue
        
        print("\nLIST RESULT: ", result)
        print("-------------------------------\n")
    pool.close()

    #Genero mi matriz resultante con los elementos de mi lista 'results' y la muestro por pantalla
    print("\nRESULTING MATRIX:\n")
    matriz = np.array(results)
    print(matriz)
    print("\n")

#Llamo al metodo para iniciar el script
calculate(args)