import socket

socket.setdefaulttimeout(0.5)

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))

        if result == 0:
            print(f"[OPEN] {host}:{port}")
        else:
            print(f"[CLOSED] {host}:{port}")

        s.close()

    except Exception as e:
        print(f"[ERROR] {host}:{port} -> {e}")


host = input("Enter host (e.g. 127.0.0.1): ")
port = int(input("Enter port: "))

scan_port(host, port)