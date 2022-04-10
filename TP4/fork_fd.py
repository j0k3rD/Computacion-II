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
c = -1
aprin = []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    parser.add_argument('-f',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    parser.add_argument('-r',type=int,help="Cantidad de veces que se almacenará la letra en el archivo.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', action='store_true', help="Activa: Modo Verboso.")
    args = parser.parse_args()
    # func_exist(args)
    # fork_fd(args, c, a, aprin)

    if args.n and args.v:
        print("Ejecucion CON Modo Verboso\n")
        verbose(args, c, a, aprin)
    elif args.n:
        fork_fd(args, c, a, aprin)
    else:
        print("Ejecucion SIN Modo Verboso\n")

def func_exist(args):
    if os.path.exists(args.f):
        file_f = open("{}{}.txt".format(constants.FILE, args.f), "w+")
        return "Archivo f creado con exito"


def fork_fd(args, c, a, aprin):     
    for i in range(args.n):  
        c += 1 
        ret = os.fork()
        if ret == 0:   
            for j in range(args.r):
                alphabet(args, a, c, aprin)
            print(aprin) 
            os._exit(0)
    for i in range(args.n):
        os.wait()


def alphabet(args, a, c, aprin):
    a = al[c]
    with open("{}{}.txt".format(constants.FILE, args.f), "w") as fd:
        fd.write(str(a))
        aprin.append(a)
        fd.flush()
        time.sleep(1)



def verbose(args, c, a, aprin):
    STARTING = "Proceso"
    DURING = "escribiendo letra"
    
    for i in range(args.n):
        c += 1
        ret = os.fork()
        if ret == 0:       
            for j in range(args.r):  
                alphabet(args, a, c, aprin)                               
                print(STARTING, os.getpid(),DURING, al[c])   
            os._exit(0)        
    for i in range(args.n):
        os.wait()


if __name__=='__main__':
    main()
