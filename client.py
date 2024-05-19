# Клиент
import socket
clientSocket = socket.socket()
clientSocket.connect(('127.0.0.1', 9123))
while True:
    message = input("Введите сообщение: ")
    clientSocket.send(message.encode())
    data = clientSocket.recv(1024)
    print(f"Ответ от сервера: {data.decode()}")