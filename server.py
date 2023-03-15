# Aplicação de Chat
#
# Criado por Giuliano Damasceno e Rodrigo Raupp
# Server side, v 1.0

import threading
from socket import *

#alocando servidor
serverIP = '127.0.0.1'
serverPort = 44444
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen()

#inicializando variáveis para localizar o usuário no chat
clients = []
users = []
server_names = ["#games", "#tech", "#pets", "#series", "#movies"]
server_clients = [[],[],[],[],[]]

print("Inicializando servidor... Pronto!")

#função reply responde às mensagens de protocolo trocadas com os clientes
def reply(message, client):
	encodedMessage = message.encode()
	client.send(encodedMessage)

#servidor recebe mensagem de uma sala e repassa para os usuários que estão nessa sala
def transmission(message, server, user):
	id = server_names.index(server)
	for client in server_clients[id]:
		#client.send(message)
		reply('NEWMSG '+ server + ' ' + user + ' BEGIN ' + message, client)

#tratamento das mensagens enviadas pelo cliente
def clientController(client):
	while True:
		message = client.recv(4000)
		decoded_message = message.decode()
		info = decoded_message.split(' ') #		CONNECT #games   info = ["CONNECT", "#games"]

		if (info[0] == 'FORCEQUIT') or (info[0] == 'SHUTDOWN'):
			reply('GOODBYE', client)
			clients.remove(client)
			if info[0] == 'SHUTDOWN':
				users.remove(user)
			client.close()
			break

		elif info[0] == 'LOGIN':  # 			LOGIN rodrigolaforet abcd		info = ["LOGIN", "rodrigolaforet", "abcd"]
			user = info[1]
			password = info[2]

			flag = 0
			true_password = 0
			with open('users.txt', 'r') as f:
				for count, line in enumerate(f):
					if flag == 1:
						true_password = line
						break
					if count % 2 == 0:
						if line == (user + '\n'):
							flag = 1
			if (flag == 1 and password + '\n' == true_password):
				reply('AUTHEN 100 ' + user, client)
				clients.append(client)
				users.append(user)
			elif (flag == 1 and password != true_password):
				reply('AUTHEN 200 ' + user, client)
			elif(flag == 0):
				reply('AUTHEN 300 ' + user, client)

		elif info[0] == 'SERVERSLIST':
			answer = 'LOBBY '
			for server in server_names:
				answer = answer + server + ' '
			reply(answer, client)
		
		elif info[0] == 'CONNECT':
			if info[1] in server_names:
				server_clients[server_names.index(info[1])].append(client)
				currentServer = info[1]
				reply('SERVERCONNECT 100 ' + info[1], client)
			else:
				reply('SERVERCONNECT 300 ' + info[1], client)
		
		elif info[0] == 'SENDMSG':
			server_name = info[1]
			userMessage = info[2]
			position = str.find("BEGIN ")
			transmission(decoded_message[position+7 : -1], server_name, userMessage)
		
		elif info[0] == 'LEAVE':
			server_clients[server_names.index(info[1])].remove(client)
			reply('LEAVESERVER', client)

		else:
			reply('ERR 999', client)


def welcome():
	while True:
		connectionSocket, addr = serverSocket.accept()

		thread = threading.Thread(target = clientController, args = (connectionSocket,))
		thread.start()

welcome()