import socket

ports_input = input("Enter ports separated by space: ")
ports = list(map(int, ports_input.split()))

for port in ports:
    try:
        service = socket.getservbyport(port)
    except:
        service = "unknown"

    print(f"Port {port}: {service}")