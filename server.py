import socket
from thread import *

class Server():
    def __init__(self, host, port, man):
        self.HOST = host
        self.PORT = port
        self.manlist = man

    def clientThread(self, con, adr, c, id):
        print "Client ID: " + str(id)
        while True:
            while True:
                if str(c[id]) != "":
                    break
            con.send(c[id])
            c[id] = ""
            data = con.recv(1024)
            if not data: 
                break
            print str(adr) + " : " + data
        print "Closed connection " + str(adr)
        con.close()

    def serverThread(self, c):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.HOST, self.PORT))
        s.listen(5)
        id = 0
        while True:
            conn, addr = s.accept()
            print "Connected by " + str(addr)
            c.append("")
            start_new_thread(self.clientThread, (conn, addr, c, id))
            id += 1

    def start(self):
        start_new_thread(self.serverThread, (self.manlist,))