import random


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavra.txt", "r")
    palavras_lista = []

    for linha in arquivo:
        linha = linha.strip()
        palavras_lista.append(linha)

    arquivo.close()

    numeroaleat = random.randrange(0,len(palavras_lista))

    palavra_secreta = palavras_lista[numeroaleat].upper()

    #palavra_secreta = "maça".upper()
    letras_acertadas = []

    for letra in palavra_secreta:   # lista = ["_" for letra in palavra] ->List Comprehensions
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1      # erros = erros + 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6       # if (erros == 6): enforcou = true
        acertou = "_" not in letras_acertadas
        print(erros)
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu :(")
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
