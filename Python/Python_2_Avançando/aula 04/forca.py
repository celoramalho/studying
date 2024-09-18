import random


def jogar():

    imprime_msg_abertura()   # Mensagem de boas vindas
    palavra_secreta = carrega_palavra_secreta()   # Carrega e escolhe a palavra secreta de forma randomica lendo o arquivo palavras.txt
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1      # erros = erros + 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6       # if (erros == 6): enforcou = true
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


if (__name__ == "__main__"):
    jogar()


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_msg_abertura():  # Mensagem de boas vindas
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def imprime_mensagem_vencedor():
    print("Você Ganhou!")


def imprime_mensagem_perdedor():
    print("Você Perdeu")


def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras_lista = []

    for linha in arquivo:
        linha = linha.strip()
        palavras_lista.append(linha)

    arquivo.close()

    numeroaleat = random.randrange(0, len(palavras_lista))
    palavra_secreta = palavras_lista[numeroaleat].upper()
    return palavra_secreta
