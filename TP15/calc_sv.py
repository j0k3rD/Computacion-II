import socketserver, click
from tasks_calc import pot, root, log
# Sirve para que podamos devolver el resultado de la operacion al cliente
from celery.result import AsyncResult


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Primero parseamos el mensaje
        op, num1 = self.data.decode().split(" ")
        num1 = int(num1)
        # Llamamos a la funcion correspondiente
        if op == "root":
            result = root.delay(num1)
        elif op == "pot":
            result = pot.delay(num1)
        elif op == "log":
            result = log.delay(num1)
        else:
            result = "Invalid operation"
        # Enviamos el resultado
        ## Con esta linea obtenemos el resultado de la operacion que nos envia celery, si no la hacemos asi devuleve el id##
        res = AsyncResult(result.id)
        self.request.sendall(bytes(str(res.get()), "utf-8"))


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