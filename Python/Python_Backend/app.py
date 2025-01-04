import os

def exibir_nome_do_app():
    print("""
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """) # https://fsymbols.com/

def exibir_menu_de_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def finalizar_app():
    #os.system('cls') windows
    os.system('clear') #mac e linux
    print('Encerrando programa...\n')
    
def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #pcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu: {opcao_escolhida}') #interpolação de string
        #print(type(opcao_escolhida))
        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
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