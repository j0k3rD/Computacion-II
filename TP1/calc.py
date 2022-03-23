## Calculadora con args

#Librerias usadas
import argparse
import sys


#Definimos la clase main que será llamada para ejecutar las op.
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o',type=str,help="Elige una operacion (+,-,*,/")
    parser.add_argument('-n',type=int,default=1,help="Elige un numero del 1-9")
    parser.add_argument('-m',type=int,default=1,help="Elige un numero del 1-9")
    args = parser.parse_args()
    sys.stdout.write(str(calculate(args)))


#Creamos la funcion de calculate para saber que operaiones se van a realizar.
def calculate(args):

    if args.o == "*":
        total = args.n*args.m
    elif args.o == "+":
        total = args.n+args.m
    elif args.o == "-":
        total = args.n-args.m
    elif args.o == "/":
        total = args.n/args.m
    else:
        print("Error con los argumentos. Vuelva a intentarlo.")
    print(args.n, args.o, args.m,"=",total)


if __name__=='__main__':
    main()

##Como no funcionaba el printeo del resultado se buscó el por qué y se llegó a la conclusión de añadir la clase main.
#s