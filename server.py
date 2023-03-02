from socket import *

serverIP = '192.168.8.49'
serverPort = 9999

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))

serverSocket.listen(1)

print("Server is ready to receive.")

connectionSocket, addr = serverSocket.accept()

while 1:

	message = connectionSocket.recv(1500)
	decodedMessage = message.decode()
	info = decodedMessage.split(' ')
	
	if info[0] == 'LOGIN':
		user = info[1]
		password = info[2]
		if user == 'rodrigolaforet' and password == 'abcd':
			reply = 'AUTHEN 100 ' + user
			encodedMessage = reply.encode()
			connectionSocket.send(encodedMessage)
			connectionSocket.close()
		else:
			reply = 'ERR 999'
			encodedMessage = reply.encode()
			connectionSocket.send(encodedMessage)