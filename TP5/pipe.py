##  Ejercicio del TP5 - Uso de Pipes - Inversor de texto

# Las "pipes" sirven para poder redireccionar una salida de un proceso hacia la entrada de otro y asi comunicarlos.

import argparse
import constants_pipe
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',type=str,help="Ingrese el nombre del archivo de texto a usar. EJ: 'test.txt'")
    args = parser.parse_args()
    func_exist(args)
    invest(args)

def func_exist(args):
    if os.path.exists(args.f):
        file_f = open("{}{}".format(constants_pipe.FILE, args.f), "r")
        return "Archivo f creado con exito"
    else:
        return "Archivo NO ENCONTRADO!"


def invest(args):
    with open("test.txt") as fd:
        lines = sum(1 for line in fd)
        print(lines)

    for i in range(lines):
        #Inicio el descriptor r,w
        r,w = os.pipe()
        ret = os.fork()
        if ret == 0:
            #Proceso que hacen los hijos
            os.close(w)
            r = os.fdopen(r,'r')
            print("Child reading")
            line = fd.readline()
            print("{}[::-1].strip()".format(line))
            r.close()
            print("Child closing")

        else:
            #Proceso que realiza el Padre
            os.close(r)
            w = os.fdopen(w,'w')
            print("Father writting")
            w.write(lines[i])
            w.close()
            print("Father closing")
            os.wait()
            sys.exit(0)



if __name__=='__main__':
    main()
