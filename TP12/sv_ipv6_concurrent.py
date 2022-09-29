import socketserver, threading, multiprocessing, signal, argparse, socket
from subprocess import Popen, PIPE, STDOUT

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if data == b"exit":
                print("[~] Connection closed.")
                break
            else:
                command = Popen({data}, stdout=PIPE, stderr=PIPE,shell=True)
                out, err = command.communicate()
                if out.decode() == "":
                    self.request.send(b"ERROR\n"+err)
                elif err.decode() == "" and len(out.decode()) > 1024:
                    max_size = len(out.decode())
                    self.request.send(b"OK\n[!](RESIZED=%i). Change 'Buffersize' to send all message.\n" %max_size+out[:1024])
                elif err.decode() == "":
                    self.request.send(b"OK\n"+out)

class Server6Thr(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class Server6Fork(socketserver.ForkingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class ServerThr(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ServerFork(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

def service(prot, port):
    if prot[0] == socket.AF_INET and args.c == "t":
        print("IPv4")
        server = ServerThr((HOST,PORT), MyServer)
    elif prot[0] == socket.AF_INET and args.c == "p":
        print("IPv4")
        server = ServerFork((HOST,PORT), MyServer)

    elif prot[0] == socket.AF_INET6 and args.c == "t":
        print("IPv6")
        server = Server6Thr((HOST,PORT), MyServer)
    elif prot[0] == socket.AF_INET6 and args.c == "p":
        print("IPv6")
        server = Server6Fork((HOST,PORT), MyServer)
    else:
        print("[!] Error! Arguments not valid.")
    server.serve_forever()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, help="Puerto que el va a usar para iniciar el sv")
    parser.add_argument('-c', type=str, help="Seleccionar 't' para threading y 'p' para process")
    args = parser.parse_args()

    HOST, PORT = "localhost", args.p
    socketserver.TCPServer.allow_reuse_address = True

    directions = socket.getaddrinfo("localhost", args.p, socket.AF_UNSPEC, socket.SOCK_STREAM)
    ips = []
    for ip in directions:
        ips.append(threading.Thread(target=service, args=(ip,args.p)))
    for ip in ips:
        ip.start()