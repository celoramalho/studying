import os
import random


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Letra: ")
    chute = chute.strip().upper()
    os.system('cls') or None
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print(" _______\n|/      |\n|\n|\n|\n|\n---")


def imprime_mensagem_vencedor():
    os.system('cls') or None
    print("      VOCÊ ACERTOU      ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")



def imprime_mensagem_perdedor():
    os.system('cls') or None
    print(" _______\n|/      |          =======                                             ||         ||")
    print("|       O        ||       ||  _______       __           ||   ______   ||         ||")
    print("|      /|\       ||       || ||     || || //   \   ======|| ||      || ||         ||")
    print("|      / \       ||=======   ||======  ||//      ||      || ||======   ||         ||")
    print("|                ||          ||        ||        ||      || ||         ||         ||")
    print("---              ||            ======  ||          ======||   ======     =========\n")


def forca_desenho(erros):
    print(" _______\n|/      |")
    if (erros == 0):
        print("|")
        print("|")
        print("|")
    elif (erros == 1):
        print("|       O")
        print("|")
        print("|")
    elif (erros == 2):
        print("|       O")
        print("|       |")
        print("|")
    elif (erros == 3):
        print("|       O")
        print("|       |\ ")
        print("|")
    elif (erros == 4):
        print("|       O")
        print("|      /|\ ")
        print("|")
    elif (erros == 5):
        print("|       O")
        print("|      /|\ ")
        print("|      /")
    elif (erros == 6):
        print("|       O")
        print("|      /|\ ")
        print("|      / \ ")

    print("|")
    print("---")



def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras_lista = []

    for linha in arquivo:
        linha = linha.strip()
        palavras_lista.append(linha)

    arquivo.close()

    numeroaleat = random.randrange(0, len(palavras_lista))
    palavra_secreta = palavras_lista[numeroaleat].upper()
    return palavra_secreta


def jogar_novamente():
    jogar_denovo = input("Jogar Novamete? (S | N): ")

    if (jogar_denovo.upper() == "S"):
        jogar()
    elif (jogar_denovo.upper() == "N"):
        print("Obrigado por jopgar! XD")


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_chutadas = []

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1      # erros = erros + 1
            letras_chutadas.append(chute)
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6       # if (erros == 6): enforcou = true
        forca_desenho(erros)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("Letras erradas: ", letras_chutadas)

    if (acertou):
        imprime_mensagem_vencedor()
        print("A palavra era ", palavra_secreta)
    else:
        imprime_mensagem_perdedor()
        print("A palavra era ", palavra_secreta)

    jogar_novamente()


if (__name__ == "__main__"):
    jogar()
