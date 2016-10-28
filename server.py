from socket import *
import time, struct

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

#establish connection TO server
serverName = '127.0.0.1'
serverPort = 4444

while True:
	print "Attempting to connect to Control Center."
	serverSocket = socket(AF_INET, SOCK_STREAM)
	try:
		serverSocket.connect((serverName,serverPort))
	except error, v:
		if v[0] == 61:
			print "Control Center not up. Waiting five seconds."
			time.sleep(5)
			continue #try again. back to top of loop
	print "Connected to Control Center. Awaiting data!"
	while True:
		#wait for data from server
		query = serverSocket.recv(1024) 
		#do something with that data
		print "Got command [%s] from Control Center. Replying."  % query
		serverSocket.send(query + " ; Got command")

serverSocket.close()
