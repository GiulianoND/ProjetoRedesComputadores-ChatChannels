# ProjetoRedesComputadores-ChatGpt

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
* 1. Login to your account - Se selecionada, solicita a autenticação do usuário e o leva para o lobby de canais disponíveis
* 2. Create an user - Se selecionada, pede que o usuário crie um novo usuário e senha para 
* 3. Quit
* Autenticação
  * O arquivo "user.json" contém os dados de identificação dos usuários. É possível realizar o cadastro de novos usuários durante a execução do programa.
* No menu principal: é disponibilizada três opções para o usuário: 1 - Login
