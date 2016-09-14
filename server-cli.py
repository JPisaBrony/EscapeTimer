from server import Server
from multiprocessing import Manager
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python " + sys.argv[0] + " HOST PORT"
        sys.exit(0)
    
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    man = Manager()
    cons = man.list()
    s = Server(sys.argv[1], int(sys.argv[2]), cons)
    s.start()
	
    while True:
        cmd = raw_input("Connection: ")
        cmd2 = raw_input("Message: ")
        cons[int(cmd)] = cmd2