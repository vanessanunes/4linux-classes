import requests
import sys

id_u = input('Digite o id: ')

response = requests.get('http://192.168.205.144:8080/usuarios')

if response.status_code == 200:
	# print(response.json())
	print('sucesso')
else:
	print('Nao consegui acessar a api!: {}'.format(response.text))
	exit()

dados = None
for user in response.json():
	if user.get('_id') == int(id_u):
		dados = user
		break

if dados is None:
	print('id nao encontrado')
	exit()

nome = input('Digite o novo nome: ')
email = input('Digite o novo email: ')

usuario = {'nome': nome, 'email': email}

response = requests.put('http://192.168.205.144:8080/usuarios/{}'.format(dados.get('_id')), json=usuario)

print(response.json())
