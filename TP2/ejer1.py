##Ejercicio 1 -- TP2

## Ejercitacion con subprocess.Popen [popen]

import argparse
from asyncio import subprocess
from asyncio.subprocess import STDOUT
from concurrent.futures import process
import os
import sys
from subprocess import Popen, PIPE, STDOUT
import time

now = time.strftime("%c")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',type=str,help="Elija el comando que quiera ejecutar. EJ: 'ls -l', 'ip a'")
    parser.add_argument('-f',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    parser.add_argument('-l',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    args = parser.parse_args()
    func_arch(args)
    func_arch(args)


def func_exist(args):
    if os.path.exists(args.f) == False:
        args.f = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.f), "w")
        return "Archivo f creado con exito"
    elif os.path.exists(args.l) == False:
        args.l = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w")
        return "Archivo l creado con exito"
    else:
        return "Argumentos invalidos"


def func_arch(args):
    fs = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.f), "w+")
    Popen(["{}".format(args.c)],shell=True, stdout=fs)

    fd = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w+")
    p = Popen(["{}".format(args.c)], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read()
    with open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w+") as error_file:
        error_file.write(str(output))
 

if __name__=='__main__':
    main()


