from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'www.google.com'
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 20))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
clientSocket.send("MAIL From: bradwaechter@gmail.com\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send RCPT TO command and print server response.
clientSocket.send("RCPT To: mybaldbeliefs@gmail.com\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send DATA command and print server response.
clientSocket.send("DATA\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send message data.
# Message ends with a single period.
clientSocket.send("SUBJECT: Test\nThis is a test\n.\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print('250 reply not received from server.')

