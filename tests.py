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

lista = ['a', 'b', 'c', 'd']
teste = 'd'

if teste in lista:
	print('Está na lista.')