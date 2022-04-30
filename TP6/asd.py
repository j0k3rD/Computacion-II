import mmap, signal, os, time

fd = open("/home/aaron/Documents/Facultad/Tercer_Año/Computacion-II/TP6/test.txt", "rb")

def lee(s, f):
    leido = area.read(12)
    area.seek(0)
    area.write(leido.decode().upper().encode())
    os.kill(pid, signal.SIGUSR1)

def lee_may(s, f):
    print(area.read(12))

signal.signal(signal.SIGUSR1, lee)
area = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ)

pid = os.fork()
if pid == 0:
    signal.signal (signal.SIGUSR1, lee_may)
    area.write(b"soy el hijo ")
    os.kill(os.getppid(), signal.SIGUSR1)
    area.seek(0)
    signal.pause()
    exit()

os.wait()

