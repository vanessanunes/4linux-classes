import requests
import sys

id_u = sys.argv[1]

response = requests.delete('http://192.168.205.144:8080/usuarios/{}'.format(id_u))

if response.status_code == 200:
	print('ID: {}, {}'.format(id_u, response.json()))
else:
	print('Deu ruim: ID {}, {}'.format(id_u, response.text))

