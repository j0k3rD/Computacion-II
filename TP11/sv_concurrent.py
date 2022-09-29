import socket,argparse
import concurrent.futures
from subprocess import Popen, PIPE, STDOUT


def handle(s2, addr):
    while True:
        data = s2.recv(1024)
        print(data)
        if data == b"exit":
            print("[~] Connection closed.")
            break
        else:
            command = Popen({data}, stdout=PIPE, stderr=PIPE,shell=True)
            out, err = command.communicate()
            if out.decode() == "":
                s2.send(b"ERROR\n"+err)
            elif err.decode() == "" and len(out.decode()) > 1024:
                max_size = len(out.decode())
                s2.send(b"OK\n[!](RESIZED=%i). Change 'Buffersize' to send all message.\n" %max_size+out[:1024])
            elif err.decode() == "":
                s2.send(b"OK\n"+out)

def ProcHandle(args):
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("", args[1]))
            s.listen(1)
            while True:
                s2, addr = s.accept()
                result = executor.submit(handle, s2, addr)

def ThrHandle(args):
    with concurrent.futures.ThreadPoolExecutor(8) as executor:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(args)
            s.listen(1)
            while True:
                s2, addr = s.accept()
                result = executor.submit(handle, s2, addr)

 
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, help="Puerto que el va a usar para iniciar el sv")
    parser.add_argument('-c', type=str, help="Seleccionar 't' para threading y 'p' para process")
    args = parser.parse_args()

    HOST, PORT = "", args.p

    if args.c == "t":
        server = ThrHandle((HOST, PORT))
        server.serve_forever()
    elif  args.c == "p":
        server = ProcHandle((HOST, PORT))
        server.serve_forever()
    else:
        print("[!] Error! Arguments not valid.")