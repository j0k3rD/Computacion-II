#  Ejercicio del TP6 - Mapeado de Memoria y Sincronizacion - Leer y Almacenar

import argparse
import os
import sys
import mmap
import signal


def handler_father(s,f):
        if s == signal.SIGUSR1:
            os.kill(pid_H2, signal.SIGUSR1)
        elif s == signal.SIGUSR2:
            os.kill(pid_H2, signal.SIGUSR2)
            #Para finalizar los dos hijos
            for i in range(2):
                os.wait()
            print("Father exiting..")
            sys.exit(0)


def handler_H2(s,f):
    print("H2 Notified")
    if s == signal.SIGUSR1:
        line = memory.readline().decode().upper()
        os.write(fd, line.encode())
    elif s == signal.SIGUSR2:
        print("H2 Exiting")
        sys.exit(0)

parser = argparse.ArgumentParser()
#Pasar ubicacion, el archivo se crea solo
parser.add_argument('-f',type=str,help="Ruta donde se ejecutara el archivo")
args = parser.parse_args()

memory = mmap.mmap(-1,100)
'''
os.O_WRONLY = abrir solo como escritura
os.O_CREAT = crea un archivo si no existe
os.O_TRUNC = tamaño truncado a 0
'''
fd = os.open("{}test.txt".format(args.f), os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

print("Starting..")

try:
    pid = os.fork()
    if pid == 0:
        #Procesos que realiza el Hijo 1.
        for line in sys.stdin:
            if line[:3] == "bye":
                os.kill(os.getppid(), signal.SIGUSR2)
                print("H1 Exiting")
                sys.exit(0)
            memory.write(line.encode())
            os.kill(os.getppid(),signal.SIGUSR1)
except OSError:
    print("Fork H1 failed")

try:
        #Proceso que realiza el HIJO 2
    pid_H2 = os.fork() 
    if pid_H2 == 0:
        signal.signal(signal.SIGUSR1, handler_H2)
        signal.signal(signal.SIGUSR2, handler_H2)
        while True:
            signal.pause()
except OSError:
    print("Fork H2 failed")

##Procesos que realiza el PADRE
print("Father Waiting...")
print(pid_H2)
signal.signal(signal.SIGUSR1, handler_father)
signal.signal(signal.SIGUSR2, handler_father)

#Padre siempre esperando a que le pase lineas el H1
while True:
    signal.pause()
    print("Father Reading: ", memory.readline().decode())
    print("Father Notifying..")


#Bibliografia:
# De los os_ : https://www.tutorialspoint.com/python/os_open.htm
# Del Double Fork: https://gist.github.com/Ma233/dd1f2f93db5378a29a3d1848288f520e

