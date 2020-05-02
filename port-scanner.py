import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
    print('Invald Amount of arguments')
    print('Syntax: python3 port-scanner')

#pretty banner
print('-'*50)
print('scanning a target '+target)
print('time started: '+str(datetime.now()))
print('-'*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if(result == 0):
            print('port {} is open' , format(port))
        s.close()
            
except KeyboardInterrupt:
    print('\nExiting program')
    sys.exit()

except socket.gaierror:
    print('Host name could not be resolved')
    sys.exit()

except socket.error:
    print('Could not connect to server')
    sys.exit()
