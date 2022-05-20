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


results = []
si = [[1,2,3],[4,5,6]]
    
#Creacion de la funcion Main, donde se ejecutaran todos lo metodos del programa.
# def main():
parser = argparse.ArgumentParser()
parser.add_argument('-p',type=str,help="Enter the number of processes to create. EJ: '2', '5'")
parser.add_argument('-f',type=str,help="Enter the file path. EJ: '/home/user/Documents/test.txt.'")
parser.add_argument('-c',type=str,help="Select the function to calculate:   .root  .pot  .log")
args = parser.parse_args()


#Metodo que me muestra en que elemento estoy realizando el cálculo.
def sumador(num):
    num = num+1

def pid(num):
    return ("pid: %d - x=%d" % (os.getpid(), num))

#Metodo que me trae cada una de las lineas del archivo
def fd_lines(args):
    with open(args.f) as fd:
        for line in fd:
            strip_lines = line.strip('"')
            listli = strip_lines.split()
            print(listli)
            m=results.append(listli)

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


#Con unos if decido que metodo aplicar para cada parametro en -c que se ingrese
if args.c == "root":
    #Ejecuta la funcion root() con cada linea de la lista
    for i in range(len(si)):
        print("-------------------------------")
        print("CALCULATE ROOT\n")
        # fd_lines(args)
        result = pool.map(root,si[i])
        print("\nLIST RESULT: ", result)
        print("-------------------------------\n")
    pool.close()


elif args.c == "pot":
    #Ejecuta la funcion pot() con cada linea de la lista
    for i in range(len(si)):
        print("-------------------------------")
        print("CALCULATE POWER\n")
        result = pool.map(pot,si[i])
        print("\nLIST RESULT: ", result)
        print("-------------------------------\n")
    pool.close()


elif args.c == "log":
    #Ejecuta la funcion log() con cada linea de la lista
    for i in range(len(si)):
        print("-------------------------------")
        print("CALCULATE LOGARITHM\n")
        result = pool.map(log,si[i])
        print("\nLIST RESULT: ", result)
        print("-------------------------------\n")
    pool.close()
    
    
# if __name__=='__main__':
#     main()