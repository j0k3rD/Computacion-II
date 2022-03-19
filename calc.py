## Calculadora 

import argparse
from re import A

parser = argparse.ArgumentParser()
parser.add_argument('-o')
parser.add_argument('-n')
parser.add_argument('-m')
args = parser.parse_args()

try:
    
    if args.o == "*":
        total = args.n * args.m
        print("El resultado de la operacion es: ", total)
    elif args.o == "+":
        total = args.n + args.m
        print("El resultado de la operacion es: ", total)
    elif args.o == "-":
        total = args.n - args.m
        print("El resultado de la operacion es: ", total)
    elif args.o == "/":
        total = args.n / args.m
        print("El resultado de la operacion es: ", total)
        
except ValueError:
    print("Error en los argumentos: Reviselos e intente de nuevo.")
