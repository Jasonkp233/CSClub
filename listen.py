from socket import *

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