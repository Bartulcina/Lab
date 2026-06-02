import selectors
import socket

sel = selectors.DefaultSelector()
clients = {}

HOST = "localhost"
PORT = 65433

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
lsock.setblocking(False)

sel.register(lsock, selectors.EVENT_READ)

print(f"[CHAT SERVER] Listening on {HOST}:{PORT}")

while True:
    events = sel.select()

    for key, _ in events:
        if key.fileobj is lsock:
            conn, addr = lsock.accept()
            conn.setblocking(False)
            sel.register(conn, selectors.EVENT_READ)

            clients[conn] = {"addr": addr, "name": None}
            print(f"[CONNECT] {addr}")

        else:
            conn = key.fileobj
            data = conn.recv(1024)

            if data:
                msg = data.decode().strip()

                if clients[conn]["name"] is None:
                    clients[conn]["name"] = msg
                    print(f"[LOGIN] {msg}")
                else:
                    full_msg = f"{clients[conn]['name']}: {msg}"
                    print(full_msg)

                    for c in clients:
                        if c != conn:
                            c.sendall(full_msg.encode())

            else:
                print(f"[DISCONNECT] {clients[conn]['name']}")
                sel.unregister(conn)
                conn.close()
                del clients[conn]