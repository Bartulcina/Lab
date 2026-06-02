import socket

HOST = "localhost"
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("[CLIENT] Connected to server")

while True:
    msg = input("Unesi poruku (ili 'exit'): ")

    if msg.lower() == "exit":
        break

    client.sendall(msg.encode())
    data = client.recv(1024)

    print("[CLIENT] Received:", data.decode())

client.close()