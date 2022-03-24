##Ejercicio 1 -- TP2

## Ejercitacion con subprocess.Popen [popen]

import argparse
import os
import sys
import subprocess as sp



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',type=str,help="Elija el comando que quiera ejecutar. EJ: 'ls -l', 'ip a'")
    parser.add_argument('-f',type=str,default=1,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    parser.add_argument('-l',type=str,default=1,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    args = parser.parse_args()
    func_arch(args)
#    sys.stdout.write(str(func_arch(args)))

# def func_exist(args):
#     if os.path.exists(args.f) == False:
#         args.f = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.f), "w")
#         return "Archivo f creado con exito"
#     elif os.path.exists(args.l) == False:
#         args.l = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w")
#         return "Archivo l creado con exito"
#     else:
#         return "Argumentos invalidos"

def func_arch(args):
    fd = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.f), "w+")
    sp.Popen(["{}".format(args.c)], stdout=fd)

    fd = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w+")
    sp.Popen(["{}:, Comando: ,{} ejecutado con exito".format(date, args.c)], stdout=fd, stderr=fd)

if __name__=='__main__':
    main()


    