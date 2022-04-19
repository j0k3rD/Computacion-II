## Ejercicio del TP4 - Uso de Fork() - STRING ABECEDARIO

# "Fork" es un metodo de python que sirve para crear procesos hijos de otros.

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


al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    parser.add_argument('-f',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    parser.add_argument('-r',type=int,help="Cantidad de veces que se almacenará la letra en el archivo.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', action='store_true', help="Activa: Modo Verboso.")
    args = parser.parse_args()
    func_exist(args)
    

    if args.n and args.v and args.f and args.r:
        print("Ejecucion CON Modo Verboso\n")
        fork_fd(args)
    elif args.n and args.f and args.r:
        print("Ejecucion SIN Modo Verboso\n")   
        fork_fd(args)     
    else:
        print("Faltan argumentos")


def func_exist(args):
    if os.path.exists(args.f):
        file_f = open("{}{}.txt".format(constants.FILE, args.f), "w+")
        return "Archivo f creado con exito"


def fork_fd(args):
    #Tendriamos que poner que el padre habra el archivo antes y que le pase un valo de offset a los hijos.
    #Antes de hacer el write podiramos hacer un sigend.
    for i in range(args.n):
        ret = os.fork()
        if ret == 0:       
            for j in range(args.r):  
                alphabet(args, i)
                if args.v == True:                                
                    print(f"{constants.STARTING}, {os.getpid()},{constants.DURING}, {al[i]}")   
            os._exit(0)        
    for i in range(args.n):
        os.wait()
    with open("{}{}.txt".format(constants.FILE, args.f), "a") as fd:
        fd.write('\n') 


def alphabet(args, c):
    a = al[c]
    with open("{}{}.txt".format(constants.FILE, args.f), "a") as fd:
        fd.write(str(a))
        fd.flush()
    time.sleep(1)


if __name__=='__main__':
    main()
