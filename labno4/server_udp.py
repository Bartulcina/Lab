import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 8000))

print("UDP Server running...")

while True:
    data, addr = server.recvfrom(1024)
    msg = data.decode()

    print(f"Received from {addr}: {msg}")

    response = "ACK: " + msg
    server.sendto(response.encode(), addr)