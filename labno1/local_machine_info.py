import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("Local IP:", ip_address)

# simple TCP server on 9999
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen(1)

print("TCP server running on port 9999")

conn, addr = server.accept()
print("Connection from:", addr)

conn.send(b"Hello from Lab1 server")
conn.close()
server.close()