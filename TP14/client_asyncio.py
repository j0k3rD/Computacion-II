import socket, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-hs', help="Seleccionar el host a conectar")
parser.add_argument('-p', type=int, help="Puerto que el va a usar para iniciar el handshake")
args = parser.parse_args()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket!")
    sys.exit()

host = args.hs
port = args.p

s.connect((host, port))

while (1):
    msg = input('> ')
    if msg == str("exit"):
        print("[~] Connection Closed")
        s.send(bytes(msg, "utf-8"))
        break
    elif msg == str(""):
        print("[!] Enter a valid argument.")
        continue
    else:
        s.send(bytes(msg, "utf-8"))
        recv = str(s.recv(1024),"utf-8")
        print(recv)