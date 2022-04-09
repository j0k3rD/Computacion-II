

import argparse
import os
from signal import alarm
from time import sleep
import constants
import string
import time
from multiprocessing.connection import wait

al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string = []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    parser.add_argument('-f',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    parser.add_argument('-r',type=str,help="Cantidad de veces que se almacenará la letra en el archivo.")
    parser.add_argument('-v',type=str,help="Inicia el Modo Verboso.")
    args = parser.parse_args()
    func_exist(args)
    fork_fd(args)


def func_exist(args):
    if os.path.exists(args.f):
        file_f = open("{}{}.txt".format(constants.FILE, args.f), "w+")
        return "Archivo f creado con exito"


def fork_fd(args):     
    for i in range(args.n):  
        ret = os.fork()
        if ret == 0:   
            a = None 
            # for j in range (0, len(al)):
            c = 0
            a = al[c]
            c =+ 1
            with open("{}{}.txt".format(constants.FILE, args.f), "w+") as fd:
                fd.write(a)
                string.append(a) 
                fd.flush()
                time.sleep(0.1)
            print(string)
            os._exit(0)

    for i in range(args.n):
        wait()



def verbose(args):
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
