"""Multiples clientes con:
        . multiprocessing
        . threading"""

import socket, sys, os, argparse, signal
from multiprocessing import Process

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# def exit(s,f):
#     print("Exiting..")
#     signal.signal(signal.SIGINT, signal.SIG_DLF)

def upper(cs, addr):
    while True:
        data = cs.recv(1024)
        x = data.decode("ascii")
        if x[:3] == "bye":
            cs.close()
        else:
            print("Recived: "+data.decode("ascii"))
            cs.send(data.upper())

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-p',type=int,help="Elijo el puerto con el que quiero conectarme.")
    args = parser.parse_args()

    if args.p:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        host = ""
        port = args.p

        ss.bind((host, port))

        ss.listen(5)

        while True:
            client = ss.accept()
            cs, addr = client
            print("Got a connection from %s" %str(addr))
            p1 = Process(target=upper, args=(client))
            p1.start()
            p1.join()
            exit(0)
    # signal.signal(signal.SIGINT, exit)


if __name__=="__main__":
    main()