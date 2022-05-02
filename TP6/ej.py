import mmap
import os

mm = mmap.mmap(-1, 13)
mm.write(b"Hello world!")



pid = os.fork()

if pid == 0:  # In a child process
    mm.seek(0)
    print(mm.readline().decode())

    mm.close()





# memoria = mmap.mmap(-1, 13)

# pid = os.fork()

# if pid == 0:
#     #PROCESOS HIJOS
#     memoria.write(b"hola pa\n")
#     exit()

# #PADRE
# leido = memoria.readline()
# print(b"Padre leyendo: ", leido.decode())
# os.wait()
 















# # def handler_H1(s,f):
# #     signal.signal(signal.SIGINT, signal.SIG_DFL)
# fd = open("/home/aaron/Documents/Facultad/Tercer_Año/Computacion-II/TP6/test.txt", "rb")

# memoria = mmap.mmap(fd.fileno(),0, access=mmap.ACCESS_READ)

# memoria.readline()
# # signal.signal(signal.SIGINT, handler)
# # memoria = mmap.mmap(-1,12)
# # memoria.write()
# # time.sleep(100)
