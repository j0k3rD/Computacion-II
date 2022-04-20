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
        r,w = os.pipe()
        ret = os.fork()
        if ret == 0:
            #Proceso que hacen los hijos
            os.close(w)
            r = os.fdopen(r,'r')
            # print("Child reading")
            line = r.readline()
        # No puedo poner solo el parametro de lines dentro de las llaves y agregarle lo otro ya que todo hace
        # una sola funcion por lo que lo hacemos con la "f" al principio en vez de format.
            print(f"{line[::-1].strip()}")
            r.close()
            time.sleep(1)
            # print("Child closing")
            # sys.exit(0)

        else:
            #Proceso que realiza el Padre
            os.close(r)
            w = os.fdopen(w,'w')
            # print("Father writting")
            w.write(lines[i])
            w.close()
            os.wait()
            # print("Father closing")
            sys.exit(0)


if __name__=='__main__':
    main()
    

#Bibliografica de ayuda: https://www.tutorialspoint.com/python/os_pipe.htm
#      readline()        https://stackoverflow.com/questions/6193779/python-readline-from-pipe-on-linux

