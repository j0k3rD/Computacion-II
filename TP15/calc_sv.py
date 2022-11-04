import socketserver, click
from tasks_calc import pot, root, log


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        if self.data == b'root':
            self.request.sendall(str(root.delay(2)).encode())
        elif self.data == b'pot':
            self.request.sendall(str(pot.delay(2)).encode())
        elif self.data == b'log':
            self.request.sendall(str(log.delay(2)).encode())

@click.command()
@click.option('-hs','--host', default='localhost', help='Host to connect')
@click.option('-p','--port', default=5000, help='Port to connect')

def main(host, port):
    HOST, PORT = host, port
    socketserver.TCPServer.allow_reuse_address = True   
    
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()