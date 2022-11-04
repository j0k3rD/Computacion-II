from calc_config import app
import time, os, math


@app.task
#Metodo que calcula la raiz de c/u de los elementos de los elementos de la linea de file
def root(num):
    time.sleep(1)    
    print("Process %d calculing root of %d" %(os.getpid(), num))
    return math.sqrt(num)

@app.task
#Metodo que calcula la potencia de c/u de los elementos de los elementos de la linea de file
def pot(num):
    time.sleep(1)
    print("Process %d calculing root of %d" %(os.getpid(), num))
    return math.pow(num,num)

@app.task
#Metodo que calcula el logaritmo de c/u de los elementos de los elementos de la linea de file
def log(num):
    time.sleep(1)
    print("Process %d calculing root of %d" %(os.getpid(), num))
    return math.log10(num)