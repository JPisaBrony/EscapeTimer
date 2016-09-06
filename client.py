import socket
import sys

HOST = '127.0.0.1'
PORT = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data = s.recv(1024)
    if not data:
        break
    print data
    s.send(data)
s.close()
