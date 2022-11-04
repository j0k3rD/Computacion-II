import socket, click


@click.command()

@click.option('-hs','--host', default='localhost', help='Host to connect')
@click.option('-p','--port', default=5000, help='Port to connect')
@click.option('-op','--op', help='Operation to do. log, pot, root')
@click.option('-n','--num1', help='Number 1')

def main(host, port, op, num1):
    HOST, PORT = host, port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    msg = op + " " + num1
    s.send(bytes(msg, "utf-8"))
    recv = str(s.recv(1024),"utf-8")
    print(recv)

if __name__ == '__main__':
    main()