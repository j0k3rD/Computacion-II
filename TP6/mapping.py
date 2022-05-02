#  Ejercicio del TP6 - Mapeado de Memoria y Sincronizacion - Leer y Almacenar

# 

import argparse
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
# def handler_H1(s,f):
#     signal.signal(signal.SIGINT, signal.SIG_DFL)###
#     memory.write(sys.stdin.read().encode())
#     exit(0)
    # time.sleep(1)
    # os.kill(pid, signal.SIGUSR1)

# def handler_H2(s,f):
#     read_l = memory.readline().decode()
#     memory.write(read_l.decode().upper().encode())

# for i in range(1):
print("Iniciando..")
pid = os.fork()
if pid == 0:
    h1 = os.getpid()
    h2 = os.getpid()
        # if i == 1:
    #Procesos que realiza el HIJO 1
    # signal.signal(signal.SIGUSR1, handler_H1)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    memory.write(sys.stdin.read().encode())
    exit(0)
            # os.kill(h1, signal.SIGUSR1)
        # elif i == 2:
        #     #Procesos que realiza el HIJO 2
        #     read_l = memory.readline().decode()
        #     memory.write(read_l.decode().upper().encode())

    
#Procesos que realiza el PADRE
# signal.signal(signal.SIGUSR1, handler_H1) 
time.sleep(5)
# memory.seek(0)
while(True):
    lines = memory.readline()
    print("Padre Leyendo: ",lines.decode())
    if not lines:
        break
memory.close()
os.wait()
    # signal.signal(signal.SIGUSR1, handler_H2)
# for i in range(1):
#     os.wait()


# if __name__=='__main__':
#     main()