import requests

print('''
                                       _   _                ____   _____   ____  
   ___    ___    _ __    ___   _   _  | | | |_    __ _     / ___| | ____| |  _ \ 
  / __|  / _ \  | '_ \  / __| | | | | | | | __|  / _` |   | |     |  _|   | |_) |
 | (__  | (_) | | | | | \__ \ | |_| | | | | |_  | (_| |   | |___  | |___  |  __/ 
  \___|  \___/  |_| |_| |___/  \__,_| |_|  \__|  \__,_|    \____| |_____| |_|    
                                                                                 
BY: KriptonFlavy
''')

while True:

	print("=" * 40)
	userCep = input('Digite o CEP para a consulta: ')
	print("=" * 40)

	while len(userCep) != 8:

		print("A quantidade de numeros digitadas, não confere o padrão de um CEP (8 Digitos)")
		userCep = input('Digite o CEP para a consulta (CORRETAMENTE): ')

		

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(userCep))
	address_data = request.json()

	if 'erro' not in address_data:
		print("=" * 40)
		print(f"{'CEP LOCALIZAD0' :^40}")
		print("=" * 40)		
  
		print('CEP: {}'.format(address_data['cep']))
		print('Logradouro: {}'.format(address_data['logradouro']))
		print('Complemento: {}'.format(address_data['complemento']))
		print('Bairro: {}'.format(address_data['bairro']))
		print('Cidade: {}'.format(address_data['localidade']))
		print('Estado: {}'.format(address_data['uf']))
		print('DDD: {}'.format(address_data['ddd']))
		print('IBGE: {}'.format(address_data['ibge']))
		
	else:
		print('o CEP digitado por você: {} não obteve resultados [INVALIDO]'.format(userCep))
	
	cont  = input('Deseja consultar mais algum CEP [S/N]:')
 
	while cont not in 'SsnN':
		cont  = input('Deseja consultar mais algum CEP [S/N]:')

	if cont == "N" or cont == 'n':
		break;

print("=" * 40)
print(f"{'FIM' :^40}")
print("=" * 40)
	
