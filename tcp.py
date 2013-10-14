import socket
import time
import sys
import getopt

def main(argv):
    host=""
    port=""
    timeout=1.0
    try:
        opts, args = getopt.getopt(argv, "h:p:", ["host", "port"])
    except getopt.GetoptError:
        print 'tcp.py -h <host> -p <port>'
        sys.exit(2)
    if not len(opts) == 2:
        print 'tcp.py -h <host> -p <port>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            host = arg
        elif opt == '-p':
            port = int(arg)
    for i in range(5):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((host, port))
            print "[%s] Connection established" % time.strftime("%H:%M:%S")
            time.sleep(1)
            s.close()
        except Exception, ex:
            print "[%s] Cannot connect" % time.strftime("%H:%M:%S")
            print ex.message

if __name__ == "__main__":
    main(sys.argv[1:])    
