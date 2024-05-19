# Сервер
import socket
import threading
serverSocket = socket.socket()
serverSocket.bind(('', 9123))
serverSocket.listen(1)
print("Сервер запущен")
def chatting():
    while True:
        data = clientSocket.recv(1024)
        print("Сообщение от клиента: "+data.decode())
        clientSocket.send(data.decode().upper().encode())

while True:
    print("Ожидаем подключения клиента...")
    clientSocket, addr = serverSocket.accept()
    print(f"Клиент подключился {addr}")
    thread = threading.Thread(target=chatting)
    thread.start()
