import socket

HOST = "0.0.0.0"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[SERVER] Connected by {addr}")

with conn:
    while True:
        data = conn.recv(1024)

        if not data:
            break

        msg = data.decode()
        print(f"[SERVER] Received: {msg}")

        conn.sendall(data)

server.close()