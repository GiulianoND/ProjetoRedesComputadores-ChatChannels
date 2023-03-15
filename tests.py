lista = [[1,2,3],[4,5,6],[7,8,9]]

for numero in lista[0]:
    print(numero)

user = 'someone'
flag = 0
position = 0
truepassword = 0

with open('users.txt', 'r') as f:
	for count, line in enumerate(f):
		if flag == 1:
			truepassword = line
			break
		if count % 2 == 0:
			print(line)
			if line == (user + '\n'):
				flag = 1
				position = count
			
print(f"Flag: {flag}\nPosition: {position}\nPassword: {truepassword} {truepassword}")

print(truepassword)

dicio = {'a':'senha', 'b':'senha', 'c':'senha', 'd':'abc'}
teste = 'a'
teste_senha = 'abc'

if dicio[teste] == teste_senha:
	print('Usuário conectado.')
else:
	print('Não conectado.')

listaqualquer = [['uva', 'laranja', 'pera'], ['melancia', 'morango', 'maçã']]

listaqualquer[1].append('banana')

print('melancia' in listaqualquer[0])

import maskpass
pwd = maskpass.askpass(prompt = 'Password: ', mask = '*')

print('Senha é '+pwd)