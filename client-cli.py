from client import Client
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python " + sys.argv[0] + " HOST PORT"
        sys.exit(0)
    
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    c = Client(sys.argv[1], int(sys.argv[2]))
    c.start()