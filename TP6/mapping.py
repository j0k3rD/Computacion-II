#  Ejercicio del TP6 - Mapeado de Memoria y Sincronizacion - Leer y Almacenar

# 

import argparse
import os
import sys
import mmap
import signal

pid_H1 = None
pid_H2 = None

def handler_father(s,f):
    #Señales para matar a los hijos
    if s == signal.SIGUSR1:
        os.kill(pid_H2, signal.SIGUSR1)
    elif s == signal.SIGUSR2:
        os.kill(pid_H2, signal.SIGUSR2)
        print("Father exiting..")
        for i in range(2):
            os.wait()
        sys.exit(0)


def handler_H2(s,f):
    print("H2 Notified")
    if s == signal.SIGUSR1:
        line = memory.readline().decode().upper()
        os.write(fd, line.encode())
    elif s == signal.SIGUSR2:
        print("H2 Exiting")
        sys.exit(0)


# def main(self):
parser = argparse.ArgumentParser()
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

for i in range(2):
    pid = os.fork()
    if pid == 0:
        if i == 0:
            #Procesos que realiza el HIJO 1
            pid_H1 = os.getpid()
            for line in sys.stdin:
                if line == "bye":
                    os.kill(pid_H1, signal.SIGUSR2)
                    print("H1 Exiting")
                    sys.exit(0)
            memory.write(line.encode())
            os.kill(pid_H1,signal.SIGUSR1)

        else:
            #Proceso que realiza el HIJO 2
            pid_H2 = os.getpid()
            signal.signal(signal.SIGUSR1, handler_H2)
            signal.signal(signal.SIGUSR2, handler_H2)
            while True:
                signal.pause()

    else:
        #Procesos que realiza el PADRE
        print("Father Waiting...")
        signal.signal(signal.SIGUSR1, handler_father)
        signal.signal(signal.SIGUSR2, handler_father)

        while True:
            signal.pause()
            print("Father Reading: ", memory.readline().decode())
            print("Father Notifying..")

# for i in range(2):
#     os.wait()

# if __name__== "__main__":
#     main()


#/home/aaron/Documents/Facultad/Tercer_Año/Computacion-II/TP6/