from socket import *
import struct

def recv_msg(sock):
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recvall(sock, msglen)

def recvall(sock, n):
    data = ''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def send_msg(sock, msg):
    finalMsg = struct.pack('>I', len(msg)) + msg
    sock.sendall(finalMsg)

#listen to connections from server
serverPort = 4444
ccSocket = socket(AF_INET, SOCK_STREAM)
ccSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ccSocket.bind(('',serverPort))
ccSocket.listen(5) #handle at most 5 connections 

print 'Awaiting server connections' 
connectionSocket, addr = ccSocket.accept()
print "Connected to [%s]!" % addr[0]

while 1:
	message = raw_input('Input command: ') 
	connectionSocket.send(message)
	response = connectionSocket.recv(1024) 
	print "Server responded with: %s" % response

connectionSocket.close()
