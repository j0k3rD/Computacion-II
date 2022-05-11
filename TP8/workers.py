from audioop import mul
import multiprocessing

workers = multiprocessing.Pool()

input("esperando")

'''Esto crea un grupo de procesos que estan esperando que hacer. Crea por defecto la cantidad de cores
fisicos que tiene nuestra pc o los asignados a la maquina virtual.'''