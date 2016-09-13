import socket
import sys
import os

HOST = '127.0.0.1'
PORT = int(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data = s.recv(1024)
    if not data:
        break
    print data
    s.send(data)
s.close()
