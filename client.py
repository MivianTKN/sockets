
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        a = input("Data to send (E to send nothing")
        if a.upper() != "E":
            s.sendall(a.encode())
        data = s.recv(1024)
        print(data)

print('Received', repr(data))