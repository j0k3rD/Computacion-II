import asyncio, argparse
from subprocess import Popen, PIPE

def execution(self):
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

 
async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-hs', type=str, help="Direccion del Host.")
    parser.add_argument('-p', type=int, help="Puerto que el va a usar para iniciar el sv")
    args = parser.parse_args()

    # socketserver.TCPServer.allow_reuse_address = True

    server = await asyncio.start_server(
        execution, args.hs, args.p)
    await server.serve_forever()

asyncio.run(main())













async def handle_echo(r,w):
    pass

async def main():
    server = await asyncio.start_server(handle_echo, '0.0.0.0', 8888)
    addr = server.sockets[0].getsockname()

    async with server:
        print(f'Tasks: {len(asyncio.all_tasks())}')
        await server.serve_forever()
asyncio.run(main())