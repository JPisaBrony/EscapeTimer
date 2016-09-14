import socket

class Client():
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        while True:
            data = s.recv(1024)
            if not data:
                break
            print data
            s.send(data)
        s.close()