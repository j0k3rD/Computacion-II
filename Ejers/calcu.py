## Calculadora con getopt 

from ast import arg
import sys
import getopt

def calculate():
    argv = sys.argv[1:]

    opts,args = getopt.getopt(argv, "-o:-n:-m")

    for opt, arg in opts:
        if opt in ['-o']:
            