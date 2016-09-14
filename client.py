import socket
from thread import *

class Client():
    def __init__(self, host, port, man):
        self.HOST = host
        self.PORT = port
        self.manlist = man

    def clientThread(self, c):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        while True:
            data = s.recv(1024)
            if not data:
                break
            c[0] = data
            s.send(data)
        s.close()
    
    def start(self):
        start_new_thread(self.clientThread, (self.manlist,))