import requests
import sys

cep = sys.argv[1]
# cep = input('Digite o CEP: ')
response = requests.get('http://viacep.com.br/ws/{}/json'.format(cep))

if response.status_code == 200:
    res_json = response.json()
    bairro = res_json.get('bairro')
    lagradouro = res_json.get('logradouro')

    print('Rua: {}\nBairro: {}'.format(lagradouro, bairro))
elif response.status_code == 400:
	print('formato invalido')
else:
    print('erro desconhecido')
