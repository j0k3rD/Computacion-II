# Ejercicio 7 - Multiprocessing con Queue.

''''
PROBLEMA:

Escribir un programa que genere dos hijjos utilizando multiprocessing.
Uno de los hijos deberá leer desde stdin texto introducido por el usuario, y deberá escribirlo 
en un pipe (multiprocessing).

El segundo hijo deberá leer desde el pipe el contenido de texto, lo encriptará utilizando 
el algoritmo ROT13, y lo almacenará en una cola de mensajes (multiprocessing).

El primer hijo deberá leer desde dicha cola de mensajes y mostrar el contenido cifrado por pantalla.
'''

import sys
import os
from multiprocessing import Process, Pipe

# ##PARA INGRESAR POR STDIN
# def func():
#     sys.stdin = open(0)
#     print(sys.stdin)
#     print("Ingrese una linea: ")
#     c = sys.stdin.readline()
#     print('Got', c)


# multiprocessing.Process(target=func).start()

def f(r,w,nproc):
    # print("nproc vale: %d" % nproc)
    if(nproc == 2):
        #Proceso del H2, 
        # print("receptor")
        print("%d: proc %d recibiendo: %s" % (nproc, os.getpid(),r.recv()))
        r.send("_hello world")
    if(nproc == 1):
        #Proceso del H1, LEE DESDE STDIN
        sys.stdin = open(0)
        print(sys.stdin)
        print("Ingrese una linea: ")
        c = sys.stdin.readline()
        # print('Got', c)
        # print("emisor")
        w.send(c)
        print(str(nproc) + w.recv())
    r.close()
    w.close()
    print("Proceso PID %d (%d) terminando..." % (os.getpid(), nproc))

if __name__ == '__main__':
    #Crea el Pipe
    r, w = Pipe()
    # print("padre: %d" %os.getpid())
    p1 = Process(target=f, args=(r,w,1))
    p2 = Process(target=f, args=(r,w,2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Bye...")