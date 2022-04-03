## Ejercicio del TP3 - Uso de Fork() - SUMA DE PROCESOS PARES

# Fork es un metodo de python que sirve para crear procesos hijos de otros.

#----------------------------------#

import argparse
from multiprocessing.connection import wait
import os
import subprocess
from time import sleep
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    # parser.add_argument('-h',type=str,help="Ayuda.")
    parser.add_argument('-v',type=str,help="Modo Verboso.")
    args = parser.parse_args()
    if args.v == None:
        print("Ejecucion SIN Modo Verboso")
        fork_F(args)
        # p_son(args)
    else:
        print("Ejecucion CON Modo Verboso")
        verbose(args)
        # p_son(args)


def fork_F(args):        
        # for i in range(0, args.n):
        ret = os.fork()
        if ret == 0:
            # print(subprocess.check_output(["ps", "fax"], universal_newlines=True))
            # os.wait()
            # time.sleep(1)
            suma = 0
            i = 0
            while i <= os.getpid():
                if i % 2 == 0:
                    suma = suma+i
                i+=1
            print("PID: ", os.getpid(), "-", "PPID: ", os.getppid(), ":", suma)
        else:
            time.sleep(0.0001)
            print("Soy el padre")
            os.wait()


def verbose(args):
    STARTING = "Starting process"
    FINISHING = "Ending process"
    


if __name__=='__main__':
    main()