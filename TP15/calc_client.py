import socket, click


@click.command()

@click.option('-hs','--host', default='localhost', help='Host to connect')
@click.option('-p','--port', default=5000, help='Port to connect')
@click.option('-op','--op', help='Operation to do. log, pot, root')
@click.option('-n','--num1', help='Number 1')

def main(host, port, op, num1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(op.encode())
    data = s.recv(1024)
    print(data)
    s.close()
    

if __name__ == '__main__':
    main()