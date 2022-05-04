import os,mmap,sys,signal

def handler_father(s,f):
    if s == signal.SIGUSR1:
        os.kill(ch2, signal.SIGUSR1)
    elif s == signal.SIGUSR2:
        os.kill(ch2, signal.SIGUSR2)
        os.wait()
        os.wait()
        print("Father exiting..")
        sys.exit(0)

def handler_hijo2(s,f):
    print("H2 Notified")
    if s == signal.SIGUSR1:
        linea = mem.readline().decode().upper()
        os.write(fd, linea.encode())
    elif s == signal.SIGUSR2:
        print("H2 Saliendo")
        sys.exit(0)

mem = mmap.mmap(-1, 100)

fd = os.open("/home/aaron/Documents/Facultad/Tercer_Año/Computacion-II/TP6/archivo.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

if not os.fork():
    #child1
    for i in sys.stdin:
        if i[:3] == "bye":
            os.kill(os.getpid(), signal.SIGUSR2)
            print("H1 Saliendo")
            sys.exit(0)
        mem.write(i.encode())
        os.kill(os.getppid(),signal.SIGUSR1)

ch2 = os.fork()
if not ch2:
    #child2
    signal.signal(signal.SIGUSR1, handler_hijo2)
    signal.signal(signal.SIGUSR2, handler_hijo2)
    while True:
        signal.pause()

#Father
print("Padre Esperando...")
signal.signal(signal.SIGUSR1, handler_father)
signal.signal(signal.SIGUSR2, handler_father)

while True:
    signal.pause()
    print("Padre Leyendo: ", mem.readline().decode())
    print("Padre notificando..")