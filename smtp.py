from socket import *
import time, datetime, ssl, base64, sys, getpass

violet = '\033[95m'
blue = '\033[34m'
lightBlue = '\033[34m'
green = '\033[92m' 
yellow = '\033[93m'
red = '\033[31m'
end = '\033[0m'
bold = '\033[1m'
Amherst = False

print green + "Welcome..." + end

msg = "\r\EHLO bob"
mailserver = "smtp.amherst.edu"
serverPort = 25

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))
clientSocket.send(msg)
recv = clientSocket.recv(1024)
if recv.startswith("220"):
	print "[Connection to Amherst Exchange SMTP server established]"

heloCommand = "\r\nHELO\r\n"
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
if recv1.startswith("500"):
	print "[Hello Processed]"

date = datetime.datetime.fromtimestamp(time.time()).strftime("%a, %d %b %Y %H:%M:%S")
fromAddress = raw_input("%sSender address: %s" % (violet, end))
fromName = raw_input("%sSender name: %s" % (blue, end))
subject = raw_input("%sSubject: %s" % (yellow, end))
toAddress = raw_input("%sRecipient address: %s" % (green, end))
body = raw_input("%sBody: %s" % (lightBlue, end))

mailFrom = "MAIL FROM: %s\r\n" % fromAddress
clientSocket.send(mailFrom)
recv2 = clientSocket.recv(1024)
if recv2.startswith("250"):
	print "[Sender set]"

rcptTo = "RCPT TO: %s\r\n" % toAddress
clientSocket.send(rcptTo)
recv3 = clientSocket.recv(1024)
if recv3.startswith("250"):
	print "[Recipient set]"

clientSocket.send("DATA \r\n")
recv45 = clientSocket.recv(1024)
if recv45.startswith("354"):
	print "[Awaiting Input]"

data = "Date: %s\r\nFrom: %s <%s>\r\nSubject:%s\r\nTo: %s\r\n\n%s\r\n.\r\n" % (date, fromName, fromAddress, subject, toAddress, body)
clientSocket.send(data)
recv4 = clientSocket.recv(1024)

quit = "QUIT\r\n"
clientSocket.send(quit)
recv5 = clientSocket.recv(1024)
if recv5.startswith("250"):
	print "[Queued mail for delivery. %s]" % recv5.split("<")[1].split(">")[1].replace("Queued mail for delivery", "").replace(" ", "").replace("[", "").replace("]", "").replace("\n", "")
