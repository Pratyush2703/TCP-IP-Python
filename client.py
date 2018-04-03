import socket
import sys
from thread import *
 
HOST = ''   
PORT = 8888 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.connect((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket

print s.recv(1024)

while(1):
    inp = raw_input("enter something here\n")
    s.send(inp)
    
    print s.recv(1024)
s.close()