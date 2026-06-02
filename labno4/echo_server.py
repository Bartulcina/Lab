import socket
import datetime
from local_machine_info import print_machine_info

HOST = "localhost"
PORT = 9000

print(datetime.datetime.now())
print_machine_info()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("TCP Echo Server running...")

conn, addr = server.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024)

    if not data:
        break

    msg = data.decode()

    if msg == "ime_prezime":
        response = "Unos nije podržan."
    else:
        response = msg

    conn.sendall(response.encode())

conn.close()
server.close()