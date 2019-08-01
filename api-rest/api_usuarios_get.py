import requests
import sys

busca = sys.argv

if len(busca) > 1:
	nome = busca[1]
else:
	nome = ''

response = requests.get('http://192.168.205.144:8080/usuarios?nome={}'.format(nome))

if response.status_code != 200:
	print('deu algum probleeeeeeeeeeemaaaa....')
	exit()

lista_users = response.json()

for user in lista_users:
	print('{} - {}'.format(user.get('_id'), user.get('nome')))
