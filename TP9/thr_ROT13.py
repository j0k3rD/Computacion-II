## Ejercicio del TP9 - Uso de threading() - ENCRIPTACION ROT13

"""
Threading: me ayudan en la performance de mi programa, ya que son menos costosos que crear procesos.
Ademas que agilizan las operaciones I/O.
"""
#-------------------------------------------------------------------------------------------------------#
"""
Escribir un programa que genere dos hilos utilizando threading.

Uno de los hilos deberá leer desde stdin texto introducido por el usuario, y deberá escribirlo en un mecanismo IPC (*).

El segundo hijo deberá leer desde dicho mecanismo IPC el contenido de texto, lo encriptará utilizando el algoritmo ROT13, 
y lo almacenará en una cola de mensajes (queue).

El primer hijo deberá leer desde dicha cola de mensajes y mostrar el contenido cifrado por pantalla.

(*) Verificar si el uso de os.pipe() o multiprocessing.Pipe() son thread-safe, caso contrario usar Queue.
"""
#-------------------------------------------------------------------------------------------------------#

import threading
from queue import Queue
import sys
import time
import codecs
import signal


def exit(signum,frame):
    print("GoodBye Mr.Robot")
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    

def f(q1,q2,nthr):
    if(nthr == 1):
        #Proceso del H1, LEE DESDE STDIN
        sys.stdin = open(0)
        print("\nWelcome Sr.\n")
        print("Enter the string to encrypt: ")
        while True:
            for line in sys.stdin:
                q1.put(line)
                #T1 LEE lo que le envio encriptado el T2
                time.sleep(1)
                print("\nT1 reading encrypted line: ",q2.get())

    if(nthr == 2):
    #Proceso del T2
        while True:
            msg = str(q1.get())
            print("\nT2 encrypting..")
            q2.put(codecs.encode(msg, 'rot13'))

signal.signal(signal.SIGINT, exit)


if __name__ == '__main__':
    #Creo las Colas
    q1 = Queue()
    q2 = Queue()

    #Creacion de los Hilos T1 y T2
    t1 = threading.Thread(target=f, args=(q1,q2,1), daemon=True)
    t2 = threading.Thread(target=f, args=(q1,q2,2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
