## Ejercicio del TP3 - Uso de Fork() - SUMA DE PROCESOS PARES

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
from tokenize import group


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-he', action='store_true', help="Activa: Ayuda.")
    #EN este caso se creo una ayuda personalizada para ayudar al usuario como usar el sript, pero argsparse ya trae
    #su propia ayuda con -h que el es help que ponemos en ellos.
    group.add_argument('-v', action='store_true', help="Activa: Modo Verboso.")
    args = parser.parse_args()

    if args.he:
        print("AYUDA: \n")
        help_F(args)
    else:
        print("Ejecutado SIN ayuda.\n")

    if args.n and args.v:
        print("Ejecucion CON Modo Verboso\n")
        verbose(args)
    elif args.n:
        fork_F(args)
    else:
        print("Ejecucion SIN Modo Verboso\n")


def fork_F(args):        
    for i in range(args.n):
        ret = os.fork()
        if ret == 0:
            # print(subprocess.check_output(["ps", "fax"], universal_newlines=True))
            suma = 0
            i = 0
            operation(args)
            os._exit(0)
        else:
            time.sleep(0.0001)
            #Hacerlo de esta forma no tiene sentido ya que por cada hijo que creo lo voy a esperar hasta que termine.
            #No aprovecha el multiprocesing.
            #Por lo que lo que estaria bien, pero no del todo. Lo que habria que hacer es hacer un for i in range afuera
            #del for este para que haga un wait por cada uno de los procesos. Los crea todos de una y despues los
            #mata tambien.
            # MAL
         ## os.wait()
            # MAL

    for i in range(args.n):
        wait()
    #Ese for seria la opcion correcta.


def operation(args):
    suma = 0
    i = 0
    while i <= os.getpid():
        if i % 2 == 0:
            suma = suma+i
        i+=1
    print("PID: ", os.getpid(), "-", "PPID: ", os.getppid(), ":", suma)


def verbose(args):
    STARTING = "Starting process"
    ENDING = "Ending process"
    
    for i in range(args.n):
        ret = os.fork()
        if ret == 0:
            print(STARTING, os.getpid())
            time.sleep(1)
            operation(args)
            time.sleep(1)
            print(ENDING, os.getpid())    
            os._exit(0)          
    time.sleep(3)
    for i in range(args.n):
        wait()


def help_F(args):
    INIT_TXT= """Como usar:
                            1. Escriba en su terminal 'python3'.
                            2. Seguido de '-n' donde debe poner la cantidad de procesos hijos a crear.
                            3. Luego puede elegir si agregar el Modo Verboso, escribiendo '-v', el cual mostrará detalles
                            sobre como se va ejecutando el proceso.
                            4. Por ultimo de 'Enter' para comenzar la ejecucion.
                            """
    print(INIT_TXT)


if __name__=='__main__':
    main()
