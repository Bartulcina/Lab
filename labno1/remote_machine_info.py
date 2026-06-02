import socket
import subprocess

domain = "google.com"

# ping check
subprocess.run(["ping", "-c", "1", domain])

ip = socket.gethostbyname(domain)

print("Domain:", domain)
print("IP:", ip)