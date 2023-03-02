from socket import *

serverIP = '192.168.8.49'
serverPort = 9999

clientSocket = socket(AF_INET, SOCK_STREAM)

#tela inicial: pergunta se quer fazer login ou criar usuário

print('Welcome to MSN!')
op = int(input('1. Login to your account\n2. Create an user\n'))

if op == 1:
    clientSocket.connect((serverIP, serverPort)) #conecta com o servidor
    while True:

        user = input('User: ')
        password = input('Password: ')
        message = 'LOGIN ' + user + ' ' + password
        encodedMessage = message.encode()

        clientSocket.send(encodedMessage) #envia a mensagem de login
        replyMessage = clientSocket.recv(1500) #espera a resposta
        decodedMessage = replyMessage.decode()
        if decodedMessage == ('AUTHEN 100 ' + user):
            print('User ' + user + ' online!')
            break
        elif decodedMessage == 'ERR 999':
            print('Failed connecting with your user. Try again.')
else:
    print('Not available')

clientSocket.close()