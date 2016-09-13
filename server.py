import socket
from thread import *
from multiprocessing import Process, Manager
import ctypes
import sys
import os

HOST = '127.0.0.1'
PORT = int(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def clientThread(con, adr, c, id):
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

def serverThread(c):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    id = 0
    while True:
        conn, addr = s.accept()
        print "Connected by " + str(addr)
        c.append("")
        start_new_thread(clientThread, (conn, addr, c, id))
        id += 1

def main(cons):
    #man = Manager()
    #cons = man.list()
    start_new_thread(serverThread, (cons,))

#if __name__ == '__main__':
    #man = Manager()
    #cons = man.list()
    #start_new_thread(serverThread, (cons,))
    #while True:
    #    cmd = raw_input("Connection: ")
    #    cmd2 = raw_input("Message: ")
    #    cons[int(cmd)] = cmd2