import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #endpoint

response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    print('OK')
else:
    print(f'O erro foi {response.status_code}')


"""
print(response)

200: OK
300: Redirecionamento
400: Requisição inválida
404: Requisição não encontrada
500: Erro Interno

"""