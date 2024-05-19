import socket
serverSocket = socket.socket()
serverSocket.bind(('', 9123))
serverSocket.listen(1)
print("Сервер запущен")
conn, addr = serverSocket.accept()
print("Клиент подключился")
print(addr)

