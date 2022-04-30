#  Ejercicio del TP6 - Mapeado de Memoria y Sincronizacion - Leer y Almacenar

# 

import argparse
from cgitb import handler
import os
import sys
import time
import mmap
import signal

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',type=str,help="Ruta donde se ejecutara el archivo")
    args = parser.parse_args()
    mmap_sig(args)

def mmap_sig(args):

    memory = mmap.mmap(-1,10)

    for i in range(2):
        pid = os.fork()
        if pid == 0:
            #Procesos que realiza el HIJO
            signal.signal(signal.SIGUSR1, handler_H1)
            

        #PADRE
        time.sleep(1)
        read_l = memory.readline()
        memory.seek(0)
        os.wait()


def handler_H1():
    signal.signal(signal.SIGINT, handler)
    memory.write(sys.stdin)
    os.kill(pid, signal.SIGUSR1)


