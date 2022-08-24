import socketserver, threading, multiprocessing, signal, argparse
from subprocess import Popen, PIPE, STDOUT

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            command = Popen({data}, stdout=PIPE, stderr=PIPE,shell=True)
            out, err = command.communicate()
            if out.decode() == "":
                return self.request.send(b"ERROR\n"+err)
            elif err.decode() == "":
                return self.request.send(b"OK\n"+out)

class ThrHandle(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ProcHandle(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

 
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, help="Puerto que el va a usar para iniciar el sv")
    parser.add_argument('-c', type=str, help="Seleccionar 't' para threading y 'p' para process")
    args = parser.parse_args()

    HOST, PORT = "", args.p
    socketserver.TCPServer.allow_reuse_address = True

    if args.c == "t":
        server = ThrHandle((HOST,PORT), MyServer)
        server.serve_forever()
        # try:
        #     signal.pause()
        # except:
        #     server.shutdown()      
    if  args.c == "p":
        server = ProcHandle((HOST, PORT), MyServer)
        server.serve_forever()
        # try:
        #     signal.pause()
        # except:
        #     server.shutdown()
    else:
        print("Error! Arguments not valid.")