# Клиент
import socket
import threading
clientSocket = socket.socket()
clientSocket.connect(('127.0.0.1', 9123))
def sendMessage():
    while True:
        message = input("Введите сообщение: \n")
        clientSocket.send(message.encode())
def getReponse():
    while True:
        data = clientSocket.recv(1024)
        print(data.decode())
        print("Введите сообщение: ")

thread1 = threading.Thread(target=sendMessage)
thread1.start()
getReponse()
