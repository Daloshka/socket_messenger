import socket

server = socket.socket()
server.bind(("127.0.0.1", 2000))
server.listen()

print("Server is running!")
name = input('Type your name:')
conn, add = server.accept()

client = (conn.recv(1024)).decode()
print(client + ' Присоединился!')
conn.send(name.encode())

while True:
    try:
        message = input('Я: ')
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print(client, ':', message)
    except Exception as ex:
        print(f"Error {ex}")