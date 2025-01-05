import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #endpoint

response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    
    
    dados_restaurante = {}
    
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
    
    print(dados_restaurante)
    
else:
    print(f'O erro foi {response.status_code}')

print(dados_restaurante['McDonald’s']) # Alt + 0, 1, 4, 6 ’


"""
print(response)

200: OK
300: Redirecionamento
400: Requisição inválida
404: Requisição não encontrada
500: Erro Interno

"""