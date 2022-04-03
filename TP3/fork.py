## Ejercicio del TP3 - Uso de Fork()

# Fork es un metodo de python que sirve para crear procesos hijos de otros.

#----------------------------------#

import argparse
import os



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=str,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    # parser.add_argument('-h',type=str,help="Ayuda.")
    parser.add_argument('-v',type=str,help="Modo Verboso.")
    args = parser.parse_args()
    fork_F()
    p_son()


def fork_F(args):
    for i in args.n:
        ret = os.fork()
        if ret == 0:
            p_son()            


def p_son(args):
    sum=0
    i = 0
    while i <= os.getpid():
        if i % 2 == 0:
            print(i)
            suma = suma+1
        i+=1
    print("PID: ", os.getpid(), "-", "PPID: ", os.getppid(), ":", suma)









if __name__=='__main__':
    main()