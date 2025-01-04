import os

restaurantes = [{'nome': 'Subuai', 'categoria': 'Fast Food', 'ativo': True},
                {'nome': 'Burger Ting', 'categoria': 'Fast Food', 'ativo': True},
                {'nome': 'Niniuta', 'categoria': 'Culinária Brasileira', 'ativo': True},
                {'nome': '74 Osteria', 'categoria': 'Osteria', 'ativo': True}]


def exibir_nome_do_app():
    print("""
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """) # https://fsymbols.com/


def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!\n' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!\n'
            print(mensagem)
            break
    else:
        print(f'Restaurante {nome_restaurante} nao encontrado!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()
    
def exibir_subtitulo(texto):
    os.system('clear')
    print(f"\n{texto}")
    #print('-'*len(texto))
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        
        print(f'.{nome_restaurante} - {categoria} - {ativo}')
    voltar_ao_menu_principal()

def exibir_menu_de_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def finalizar_app():
    #os.system('cls') windows
    exibir_subtitulo('Finalizando programa...')
  
def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #pcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu: {opcao_escolhida}') #interpolação de string
        #print(type(opcao_escolhida))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    os.system('clear')
    exibir_nome_do_app()
    exibir_menu_de_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    

#'aspas simples ignora espaços no inicio e fim?'

'''
aspas simples tripla
'''
"""
aspas duplas tripla

The Zen of Python, by Tim Peters
Beautiful is better than ugly.\

Explicit is better than implicit.\

Simple is better than complex.\

Complex is better than complicated.\

Flat is better than nested.\

Sparse is better than dense.\

Readability counts.\

Special cases aren't special enough to break the rules.\

Although practicality beats purity.\

Errors should never pass silently.\

Unless explicitly silenced.\

In the face of ambiguity, refuse the temptation to guess.\

There should be one-- and preferably only one --obvious way to do it.\

Although that way may not be obvious at first unless you're Dutch.\

Now is better than never.\

Although never is often better than right now.\

If the implementation is hard to explain, it's a bad idea.\

If the implementation is easy to explain, it may be a good idea.\

Namespaces are one honking great idea -- let's do more of those!\
    
"""



"""
The Zen of Python, by Tim Peters em português

Bonito é melhor que feio.\

Explícito é melhor que implícito.\

Simples é melhor que complexo.\

Complexo é melhor que complicado.\

Plano é melhor que aninhado.\

Esparso é melhor que denso.\

Legibilidade conta.\

Casos especiais não são especiais o bastante para quebrar as regras.\

Embora praticidade vença a pureza.\

Erros nunca devem passar silenciosamente.\

A menos que sejam explicitamente silenciados.\

Diante da ambiguidade, recuse a tentação de adivinhar.\

Deveria haver uma — e preferencialmente só uma — maneira óbvia de fazer algo.\

Embora essa maneira possa não ser óbvia a princípio a menos que você seja holandês.\

Agora é melhor que nunca.\

Embora nunca seja frequentemente melhor que agora mesmo.\

Se a implementação é difícil de explicar, é uma má ideia.\

Se a implementação é fácil de explicar, pode ser uma boa ideia.\

Namespaces são uma grande ideia — vamos fazer mais dessas!\
        
"""

#sep = '\n' separador da função print


# __dunder__ methods


"""
# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

"""


"""
# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])

"""