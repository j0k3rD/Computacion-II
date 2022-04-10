## Ejercicio del TP4 - Uso de Fork() - STRING ABECEDARIO

# Fork es un metodo de python que sirve para crear procesos hijos de otros.

#----------------------------------#

import argparse
from curses.ascii import EM
from multiprocessing.connection import wait
import os
from queue import Empty
import subprocess
from time import sleep
import time
import constants


al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = None
c = 0
aprin = []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    parser.add_argument('-f',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    parser.add_argument('-r',type=str,help="Cantidad de veces que se almacenará la letra en el archivo.")
    parser.add_argument('-v',type=str,help="Inicia en Modo Verboso.")
    args = parser.parse_args()
    func_exist(args)
    fork_fd(args, c)
    alphabet(args, a, c, aprin)


def func_exist(args):
    if os.path.exists(args.f):
        file_f = open("{}{}.txt".format(constants.FILE, args.f), "w+")
        return "Archivo f creado con exito"


def fork_fd(args, c):     
    for i in range(args.n):  
        ret = os.fork()
        if ret == 0:   
            c += 1 
            # for j in range (0, len(al)):
            alphabet(args, a, c, aprin)
            os._exit(0)
    for i in range(args.n):
        os.wait()



def alphabet(args, a, c, aprin):
    a = al[c]
    with open("{}{}.txt".format(constants.FILE, args.f), "w+") as fd:
        fd.write(str(a))
        aprin.append(a)
        fd.flush()
        time.sleep(0.1)
        print(aprin)



def verbose(args, a):
    STARTING = "Proceso {} escribiendo letra {}".format(os.getpid, a)
    ENDING = "Ending process"
    
    for i in range(args.n):
        ret = os.fork()
        if ret == 0:
            print(STARTING)
            print(ENDING, os.getpid())    
            os._exit(0)          
    for i in range(args.n):
        wait()


if __name__=='__main__':
    main()
