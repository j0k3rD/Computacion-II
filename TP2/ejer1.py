##Ejercicio 1 -- TP2

## Ejercitacion con subprocess.Popen [popen]

import argparse
from asyncio import subprocess
from asyncio.subprocess import STDOUT
from concurrent.futures import process
import os
from re import A
from subprocess import Popen, PIPE, STDOUT
import time

now = time.strftime("%c")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',type=str,help="Elija el comando que quiera ejecutar. EJ: 'ls', 'ip'")
    parser.add_argument('-f',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    parser.add_argument('-l',type=str,help="Pase un archivo como argumento. O simplemente el nombre para crear uno")
    args = parser.parse_args()
    func_exist(args)
    func_files(args)
    

def func_exist(args):

    if os.path.exists(args.f):
        file_f = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.f), "r+")
    else:
        file_f = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.f), "w")
        return "Archivo f creado con exito"
    
## Se hizo con dos ifs por separado ya que si lo intentamos hacer en uno solo, se creara el primero y terminara
#  la ejecucion del mismo sin crear el segundo.

    if os.path.exists(args.l):
        file_l = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "r+")
    else:
        file_l = open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w")
        return "Archivo l creado con exito"


def func_files(args):

    p = Popen(["{}".format(args.c)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()


    if p.returncode == 0:
        with open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.f), "w+") as fd:
            fd.write(str(out))

        cmd = str(args.c)
        txt = "Fecha y Hora: '{}'. Comando: '{}' ejecutado correctamente.".format(now, cmd)
        with open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w+") as error_file:
            error_file.write(str(txt))
    else:
        with open("/home/aaron/Documents/Computacion II/TPS/TP2/{}.txt".format(args.l), "w+") as error_file:
            error_file.write(str(err))
 

if __name__=='__main__':
    main()


## Bibliografias usadas: 
#  Para entender un poco mas sobre las entradas: https://www.saltycrane.com/blog/2008/09/how-get-stdout-and-stderr-using-python-subprocess-module/
#  Tenia un problema ya que el stderr no me lo estaba printeando bien y ademas cuando se pasaba un comando bien tambien pasaba
# como error. Este video ayudo a entender el PIPE y comunicate() para generar las dos salidas: https://www.youtube.com/watch?v=VlfLqG_qjx0
#  Para importar la fecha y hora: https://pythondiario.com/2014/05/obtener-fecha-y-hora-actual-en-python.html
                        