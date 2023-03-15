# Aplicação de Chat
#
# Criado por Giuliano Damasceno e Rodrigo Raupp
# Client side, v 1.0

import threading
from socket import *

serverIP = '127.0.0.1'
serverPort = 44444

clientSocket = socket(AF_INET, SOCK_STREAM)

logged_in = False
currentServer = ''

def request(message, client):
	encodedMessage = message.encode()
	client.send(encodedMessage)
        
def messageFromServer(client):
    reply_message = client.recv(1024)
    decodedMessage = reply_message.decode()
    return decodedMessage
    
def messageFromChat():
    while True:
        decodedMessage = messageFromServer(clientSocket)
        splitMessage = decodedMessage.split(' ')
        if splitMessage[0] == 'LEAVESERVER':
            break
        chatMessage = splitMessage[2] + ': ' + decodedMessage[decodedMessage.find('BEGIN') + 5:]
        print(chatMessage)

def sendMessageToChat():
    while True:
        message = input('>')
        if message == '\leave':
            break
        request(message, clientSocket)

        
#tela inicial: pergunta se quer fazer login ou criar usuário

print('Welcome!')
clientSocket.connect((serverIP, serverPort)) #conecta com o servidor

while True:
    op = int(input('1. Login to your account\n2. Create an user\n3. Quit\n'))
    if op == 1:
        user = input('User: ')
        password = input('Password: ')
        message = 'LOGIN ' + user + ' ' + password
        encodedMessage = message.encode()

        clientSocket.send(encodedMessage) #envia a mensagem de login
        replyMessage = clientSocket.recv(1024) #espera a resposta
        decodedMessage = replyMessage.decode()
        if decodedMessage == 'AUTHEN 200 ' + user:
            print('Failed connecting with your user. Try again.')
        elif decodedMessage == 'AUTHEN 300 ' + user:
            print('User not found. Try again.')
        elif decodedMessage == ('AUTHEN 100 ' + user):
            print('User ' + user + ' online!')
            logged_in = True
            break
    elif op == 3:
        message = 'FORCEQUIT'
        encodedMessage = message.encode()
        clientSocket.send(encodedMessage) #envia a mensagem
        replyMessage = clientSocket.recv(1024)
        print(replyMessage.decode())
        clientSocket.close()
        break
    else:
        print('Not available')

if logged_in:
    while True:
        message = 'SERVERSLIST'
        encodedMessage = message.encode()
        clientSocket.send(encodedMessage) #envia a mensagem
        reply_message = clientSocket.recv(1024)
        decodedMessage = reply_message.decode()
        print('Type prefered room: ')
        server_list = decodedMessage[5:].split(' ')
        server_list.remove('')
        for server in server_list:
            print(server)
        print('\\exit to close program')
        serverOption = input('>')

        if serverOption == '\exit': #é necessário fazer o fechamento da conexão TCP
            request('SHUTDOWN', clientSocket)
            clientSocket.close()
            break
        
        replyMessage = 'CONNECT ' + serverOption
        request(replyMessage, clientSocket)
        reply = messageFromServer(clientSocket)
        
        if reply == 'SERVERCONNECT 100 ' + serverOption:
            currentServer = serverOption
            print('Welcome to room ' + serverOption + '!  Type \\leave to leave.')
            
            receive_message = threading.Thread(target = messageFromChat)
            write_thread = threading.Thread(target = sendMessageToChat)
            
            receive_message.start()
            write_thread.start()

            receive_message.join()
            write_thread.join()
        currentServer = ''