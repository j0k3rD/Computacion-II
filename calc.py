## Calculadora 

import sys

op = sys.argv[1]
val1= sys.argv[2]
val2= sys.argv[3]


try:
    op= str(op)
    val1= float(val1)
    val2= float(val2)
    total = 0

    if op == "*":
        total = val1 * val2
    elif op == "+":
        total = val1 + val2
    elif op == "-":
        total = val1 - val2
    elif op == "/":
        total = val1 / val2

    print("El resultado de la operacion es: ", total)

except ValueError:
    print("Error en los argumentos: Reviselos e intente de nuevo.")
