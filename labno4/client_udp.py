import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("localhost", 8000)

while True:
    msg = input("Enter message (or exit): ")

    if msg == "exit":
        break

    client.sendto(msg.encode(), server)

    data, _ = client.recvfrom(1024)
    print("Server:", data.decode())