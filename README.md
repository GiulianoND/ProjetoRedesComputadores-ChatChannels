# Chat Application With Multiple Rooms

## Introduction

This work is intended to implement a simple chat application with multiple rooms in *Python Language* aiming at message exchange at application layer. The required Python version is 3.8 or above. Please see *Libraries Used* to learn what to install before running application. The application layer uses a personalized, test level type of messages, simulating message trade protocols like HTML, SMTP, FTP, etc. This application uses TCP in the transfer layer to ensure delivering of all messages exchanged between users.

## Application Protocol Characteristics

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

