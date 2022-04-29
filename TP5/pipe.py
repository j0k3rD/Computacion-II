##  Ejercicio del TP5 - Uso de Pipes - Inversor de texto

# Las "pipes" sirven para poder redireccionar una salida de un proceso hacia la entrada de otro y asi comunicarlos.

import argparse
import constants_pipe
import os
import sys
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',type=str,help="Ingrese el nombre del archivo de texto a usar. EJ: 'test.txt'")
    args = parser.parse_args()
    # func_exist(args)
    invest(args)

# def func_exist(args):
#     if os.path.exists(args.f):
#         file_f = open("{}{}".format(constants_pipe.FILE, args.f), "r")
#         return "Archivo f creado con exito"
#     else:
#         return "Archivo NO ENCONTRADO!"


def invest(args):
    with open(args.f, 'w') as fd:
        fd.write(constants_pipe.TEXT)
    fd = open(args.f,'r')
    lines = fd.readlines()
    fd.close()

        # lines = sum(1 for line in fd)
        # print(lines)

    for i in range(len(lines)):
        #Inicio el descriptor r,w
        r1,w1 = os.pipe()
        r2,w2 = os.pipe()
        ret = os.fork()
        if ret == 0:
            #Proceso que hacen los hijos
            ##Primera Parte recibir la linea e invertirla.
            os.close(w1)
            r1 = os.fdopen(r1,'r')
            # print("Child reading")
            line = r1.readline()
        # No puedo poner solo el parametro de lines dentro de las llaves y agregarle lo otro ya que todo hace
        # una sola funcion por lo que lo hacemos con la "f" al principio en vez de format.
            inv = (f"{line[::-1].strip()}")
            r1.close()
            # time.sleep(1)

            ##Segunda Parte: Enviar la linea invertida.
            os.close(r2)
            w2 = os.fdopen(w2, 'w')
            w2.write(inv)
            w2.close()
            # print("Child closing")
            # sys.exit(0)

        else:
            #Proceso que realiza el Padre
            ##Primera Parte: enviar la linea al hijo.
            os.close(r1)
            w1 = os.fdopen(w1,'w')
            # print("Father writting")
            w1.write(lines[i])
            w1.close()
            os.wait()

            #Segunda Parte: Leer la linea invertida que le paso el hijo.
            os.close(w2)
            r2 = os.fdopen(r2, 'r')
            inv = r2.readline()
            print(inv)
            r2.close()
            # time.sleep(1)
            # print("Father closing")
            sys.exit(0)


if __name__=='__main__':
    main()
    

#Bibliografica de ayuda: https://www.tutorialspoint.com/python/os_pipe.htm
#      readline()        https://stackoverflow.com/questions/6193779/python-readline-from-pipe-on-linux
#
