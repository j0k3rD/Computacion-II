## Ejercicio del TP3 - Uso de Fork() - SUMA DE PROCESOS PARES

# Fork es un metodo de python que sirve para crear procesos hijos de otros.

#----------------------------------#

import argparse
from multiprocessing.connection import wait
import os



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    # parser.add_argument('-h',type=str,help="Ayuda.")
    parser.add_argument('-v',type=str,help="Modo Verboso.")
    args = parser.parse_args()
    print(args.n)
    if args.v == None:
        print("Ejecucion SIN Modo Verboso")
        fork_F(args)
        # p_son(args)
    else:
        print("Ejecucion CON Modo Verboso")
        verbose(args)
        # p_son(args)


def fork_F(args):
    for i in range(args.n):
        os.fork()
        # ret = os.fork()
        # if ret == 0:
        #     p_son()            
# def p_son(args):
    suma = 0
    while i <= os.getpid():
        if i % 2 == 0:
            suma = suma+i
        i+=1
            # for i in range(args.n):
            #     os.wait()
    print("PID: ", os.getpid(), "-", "PPID: ", os.getppid(), ":", suma)


def verbose(args):
    STARTING = "Starting process"
    FINISHING = "Ending process"
    


if __name__=='__main__':
    main()