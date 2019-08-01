import requests
import sys

cad = sys.argv

usuario = {'nome': cad[1], 'email': cad[2]}

response = requests.post('http://192.168.205.144:8080/usuarios', json=usuario)

if response.status_code >= 200:
	print(response.json().get('mensagem'))
else:
	print('Nao consegui cadastrar!: {}'.format(response.text))

# print(response.text)