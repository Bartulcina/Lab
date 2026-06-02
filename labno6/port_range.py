import socket

socket.setdefaulttimeout(0.5)

def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "unknown"


def scan_range(host, start_port, end_port):
    print(f"\nScanning {host}...\n")

    for port in range(start_port, end_port + 1):
        if port < 1 or port > 65535:
            continue

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))

        if result == 0:
            service = get_service(port)
            print(f"[OPEN] {port} ({service})")

        s.close()


host = input("Host: ")
start = int(input("Start port: "))
end = int(input("End port: "))

scan_range(host, start, end)