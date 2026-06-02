import socket

HOST = "localhost"
PORT = 65433

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

name = input("Enter username: ")
sock.sendall(name.encode())

print("Chat started...")

while True:
    msg = input("> ")
    sock.sendall(msg.encode())
    