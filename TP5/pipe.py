##  Ejercicio del TP5 - Uso de Pipes - Inversor de texto

# Las "pipes" sirven para poder redireccionar una salida de un proceso hacia la entrada de otro y asi comunicarlos.

import argparse
import constants
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',type=str,help="Ingrese el nombre del archivo de texto a usar. EJ: 'test.txt'")
    args = parser.parse_args()
    func_exist(args)


def func_exist(args):
    if os.path.exists(args.f):
        file_f = open("{}{}.txt".format(constants.FILE, args.f), "r")
        return "Archivo f creado con exito"
    else:
        return "Archivo NO ENCONTRADO!"


def invest(args):
    with open(constants.FILE) as fd:
        lines = sum(1 for line in fd)
        print(lines)
    for i in range(lines):
        r,w = os.pipe()
        ret = os.fork()
        if ret == 0:

