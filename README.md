# Chat Application With Multiple Rooms

## Introduction

This work is intended to implement a simple chat application with multiple rooms in *Python Language* aiming at message exchange at application layer. The required Python version is 3.8 or above. Please see *Libraries Used* to learn what to install before running application. The application layer uses a personalized, test level type of messages, simulating message trade protocols like HTML, SMTP, FTP, etc. This application uses TCP in the transfer layer to ensure delivering of all messages exchanged between users.

## Application Protocol Characteristics

This application uses server-client approach: there is a server which deals and distributes all messages to connected clients. Whenever a new client connects to server, it persists until client requests to disconnect. Protocol uses band-controlled informations, e.g. an incoming message will have a standart message and headers. Application utilizes push/pull, e.g. when room list is requested (pull) and when client sends new message (push). Server behaves as client when requested to broadcast message to users inside a room.

## Running Client and Server

To run client and server sides, insert at your terminal:
<br>
`python3 server.py`
<br>
`python3 client.py`

## Getting Started

This version provides standard chat rooms, which you can choose after the login. In your first use, you can create new login with user and password. Then, choose to login and insert your information.

## Chat Rooms

Once logged in, the application will fetch all available rooms. The next step is to insert your preferred room based on a topic. You can choose to close program on this step too.

## Sending Messages

During the time at a room, you will receive messages from all participants. You can type too and when pressing Enter your message will travel to the server then to the users at that room. Type the key-word to leave room and choose another place.

## Code Construction

### Server Side

The server side is built with a main thread which deals with all logged in users. When a new client is on, server triggers a new thread to read incoming messages and perform correspondent functions. A builtin database controls all users and respective passcodes. Whenever a user inside a room sends some message, server invokes transmission function to analyse which users are going to receive that inserted message.

### Client Side

Clients access the application in the following order: app requests if user wants to log in, create new user or close program; after login, user can choose a room; during room time, user can leave and then choose another room or close program. Whenever a user creates a new account or logs in, the inserted password will be covered by a mask provided by maskpass library. Threads will only trigger when a user is inside a room. The threads are: messageFromChat, sendMessageToChat. These functions will deal with income messages and typed characters from user's keyboard, respectively, running at same time. Functions will end operation when user chooses to leave the room.


## Requisitos de bibliotecas:
* threading
* socket
* maskpass
* json


## Requisitos Tecnologias:

* Python instalado no computador. Para realização da instalação pode-se seguir o tutorial: 
  * Para realizar a instalação no windows: https://python.org.br/instalacao-windows/
  * Para realizar a instalação no Linux: https://python.org.br/instalacao-linux/
 * Caso necessário, utilize os comandos abaixo para instalar as bibliotecas necessárias:
  * pip install json
  * pip install threading
  * pip install socket
  * pip install maskpass

## Utilizando o programa

Para abrir o programa localmente, primeiro é necessário executar o arquivo "server.py" que contém o código do servidor. 
Para realizar essa ação, entre no diretório com os arquivos e execute o seguinte comando: 
* python .\server.py
Após, abra um novo terminal e execute o arquivo "client.py" que contém o código do cliente.
* python .\client.py

O programa te dá três opções no menu principal: 
* 1 - Login to your account - Se selecionada, solicita a autenticação do usuário e o leva para o lobby de canais disponíveis
* 2 - Create an user - Se selecionada, pede que o usuário crie um novo usuário e senha para 
* 3 - Quit

Ao selecionar a opção 1, o usuário deverá informar um nome de usuário e senha válidos, caso contrário, uma mensagem de erro será exibida. Caso as credenciais sejam válidas, ele irá para o lobby, onde poderá escolher qual canal quer interagir.
Ao selecionar a opção 2, o usuário deverá informar um nome de usuário novo e uma senha, caso contrário, uma mensagem de erro será exibida. Caso as credenciais estejam ok, um novo usuário será adicionado.
Ao selecionar a opção 3, o usuário fechará a aplicação.

Uma lista com os canais disponíveis para interação será exibida quando o usuário estiver no lobby. Nessa etapa, o usuário poderá digitar o texto de um dos canais configurados(#games, #tech, #pets, #series, #movies) ou o comando \exit. 
Caso ele digite o texto de um dos canais, ele será direcionado para interagir com os usuários conectados naquele canal, caso ele digite o comando "\exit" a aplicação será encerrada.

Dentro de um canal, o usuário poderá enviar mensagens e estas serão direcionadas para os outros usuários conectados naquele canal. Ele também pode escrever o comando "\leave" que o levará para o Lobby novamente.
* Autenticação
  * O arquivo "user.json" contém os dados das credenciais dos usuários. É possível realizar o cadastro de novos usuários durante a execução do programa.

