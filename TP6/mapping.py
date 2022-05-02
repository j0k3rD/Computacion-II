#  Ejercicio del TP6 - Mapeado de Memoria y Sincronizacion - Leer y Almacenar

# 

import argparse
from cgitb import handler
import os
import sys
import time
import mmap
import signal

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-f',type=str,help="Ruta donde se ejecutara el archivo")
#     args = parser.parse_args()
#     mmap_sig(args)

# def mmap_sig(args):

# fd = open("{}test.txt".format(args.f),"w+")
memory = mmap.mmap(-1,20)

# os.ftruncate(fd.fileno(), 10)

# memory = mmap.mmap(fd.fileno(),0, access=mmap.ACCESS_WRITE)

    # memory = mmap.mmap(fd,10)

def handler_father(s,f):
    while(True):
        lines = memory.readline()
        print("Padre Leyendo: ",lines.decode())
        if not lines:
            break

def handler_H1(s,f):
    signal.signal(signal.SIGINT, handler_H1)###
    memory.write(sys.stdin.read().encode())
    # os.setsid()
    # os.chdir('/')

def handler_H2(s,f):
    signal.signal(signal.SIG_DFL, signal.SIGUSR1)
    read_l = memory.readline().decode()
    memory.write(read_l.decode().upper().encode())

def main():
    # read_l = memory.readline().decode()
    # memory.write(read_l.decode().upper().encode())

    print("Iniciando..")

    ff_pid = os.fork()
    if ff_pid == 0:
        #Procesos que realiza el HIJO 1
        signal.signal(signal.SIGUSR2, handler_H1)
        os.kill(ff_pid,signal.SIGUSR1)
        signal.pause()

        sf_pid = os.fork()
        if sf_pid == 0:
        #Procesos que realiza el HIJO 2
            while True:
                time.sleep(1)
        else:
            #Procesos que realiza el PADRE 1
            print("Second FORK")
            print("Child PID: %d" % sf_pid)
            os._exit(os.EX_OK)

    else:
        #Procesos que realiza el PADRE
        signal.signal(signal.SIGUSR1, handler_H1)
        signal.pause()
        print("First FORK")
        print("Child PID: %d" % ff_pid)
        signal.signal(signal.SIGUSR1, handler_father)
        signal.signal(signal.SIGUSR1, handler_H2)
        # signal.pause()        
        os.kill(ff_pid, signal.SIGUSR1)
        os.wait()


if __name__== "__main__":
    main()

        # signal.signal(signal.SIGUSR1, handler_H1)
        # signal.signal(signal.SIGINT, signal.SIG_DFL)
        # memory.write(sys.stdin.read().encode())
        # exit(0)
                # os.kill(h1, signal.SIGUSR1)
            # elif i == 2:
            #     #Procesos que realiza el HIJO 2
            #     read_l = memory.readline().decode()
            #     memory.write(read_l.decode().upper().encode())
    

# signal.signal(signal.SIGUSR1, handler_H1) 
# time.sleep(5)
# # memory.seek(0)

    # signal.signal(signal.SIGUSR1, handler_H2)
# for i in range(1):
#     os.wait()


# if __name__=='__main__':
#     main()