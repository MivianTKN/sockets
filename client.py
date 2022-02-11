
import socket

HOST = input("Please enter host IP (Press E for 127.0.0.1 deafult)\n")  # The server's hostname or IP address
if HOST.upper() == "E":
    HOST = "127.0.0.1"
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        a = input("Data to send (E to send nothing)\n")
        if a.upper() != "E":
            s.sendall(a.encode())
        data = s.recv(1024)
        print(data)

print('Received', repr(data))