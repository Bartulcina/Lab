import socket

socket.setdefaulttimeout(0.5)

def scan(host, ports):
    print(f"\nHOST: {host}")
    print("-" * 30)

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((host, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"

                print(f"[OPEN] {port} ({service})")
            s.close()

        except:
            pass


hosts = input("Enter hosts (comma separated): ").split(",")
ports = input("Enter ports (comma separated): ").split(",")

ports = [int(p.strip()) for p in ports]

for h in hosts:
    scan(h.strip(), ports)