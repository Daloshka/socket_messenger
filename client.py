import socket

socket_server = socket.socket()

name = input("Enter login: ")
socket_server.connect(("127.0.0.1", 2000))
socket_server.send(name.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print(server_name, " присоединился")

while True:
    try:
        message = (socket_server.recv(1024)).decode()
        print(server_name, ":", message)
        message = input("Я: ")
        socket_server.send(message.encode())
    except Exception as ex:
        print(f"Error {ex}")