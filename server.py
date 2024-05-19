# Сервер
import socket
import threading
serverSocket = socket.socket()
serverSocket.bind(('', 9123))
serverSocket.listen(1)
print("Сервер запущен")
sockets = []
def chatting(clientSocket):
    clientSocket.send("Введите имя: ".encode())
    userName = clientSocket.recv(1024)
    userName = userName.decode()
    while True:
        data = clientSocket.recv(1024)
        print(f"{userName}: {data.decode()}")
        for socket in sockets:
            socket.send(f"{userName}: {data.decode()}".encode())

while True:
    print("Ожидаем подключения клиента...")
    clientSocket, addr = serverSocket.accept()
    print(f"Клиент подключился {addr}")
    sockets.append(clientSocket)
    thread = threading.Thread(target=chatting, args=(clientSocket,))
    thread.start()
