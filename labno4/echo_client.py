import socket

HOST = "localhost"
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("Message (exit to quit): ")

    if msg == "exit":
        break

    client.sendall(msg.encode())
    data = client.recv(1024)

    print("Server:", data.decode())

client.close()