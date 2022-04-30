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

    fd = open("{}test.txt".format(args.f),"wb")
    os.ftruncate(fd.fileno(), 10)
    memory = mmap.mmap(fd.fileno(),0)
    # memory = mmap.mmap(fd,10)

    for i in range(2):
        pid = os.fork()
        if pid == 0:
            #Procesos que realiza el HIJO
            signal.signal(signal.SIGUSR1, handler_H1)
            time.sleep(2)
            signal.signal
            exit()
        #Procesos que realiza el PADRE
        time.sleep(1)
        read_l = memory.readline()
        print("Padre Leyendo: ",read_l)
        memory.seek(0)
        signal.signal(signal.SIGUSR1, handler_H2)
    for i in range(2):
        os.wait()


def handler_H1():
    signal.signal(signal.SIGINT, handler)
    memory.write(sys.stdin)
    # time.sleep(1)
    os.kill(pid, signal.SIGUSR1)

def handler_H2():
    read_l = memory.readline().decode()
    memory.write(read_l.decode().upper().encode())

if __name__=='__main__':
    main()