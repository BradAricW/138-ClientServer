from socket import *
from datetime import datetime

serverName = '127.0.0.1'
serverPort = 12051

count = 0

while count < 10:
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.settimeout(1.0)
	message = 'Ping!'
	address = (serverName, serverPort)
	go = datetime.now()
	clientSocket.sendto(message, address)
	try:
		newmessage, server = clientSocket.recvfrom(1024)
		stop = datetime.now() 
		print newmessage + " " + str(count+1) + " " + str(stop - go)
	except timeout:
		print 'Timed Out'
		
	count += 1