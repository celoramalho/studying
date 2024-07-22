import os
import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("*********Jogo da Velha!**********")
    print("*********************************")


def imprime_tabuleiro(tabuleiro):
    os.system('cls') or None
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])


def bot_escolha_aleatoria(tabuleiro):
    marcado = False

    print("VEZ DO COMPUTADOR")

    while (not marcado):
        escolha_horizontal = random.randrange(3)
        escolha_vertical = random.randrange(3)
        escolha_horizontal = int(escolha_horizontal)
        escolha_vertical = int(escolha_vertical)

        pode_ou_nao_marcar = verifica_posicao_ocupada(
            escolha_horizontal, escolha_vertical, tabuleiro)

        if (pode_ou_nao_marcar):
            tabuleiro[escolha_horizontal][escolha_vertical] = 2
            marcado = True
        else:
            pass

    return tabuleiro


def jogador_escolha(tabuleiro):
    marcado = False

    while (not marcado):
        escolha_horizontal = input("Linha: ")
        escolha_vertical = input("Coluna: ")
        escolha_horizontal = int(escolha_horizontal)
        escolha_vertical = int(escolha_vertical)

        pode_ou_nao_marcar = verifica_posicao_ocupada(
            escolha_horizontal, escolha_vertical, tabuleiro)

        if (pode_ou_nao_marcar):
            tabuleiro[escolha_horizontal][escolha_vertical] = 1
            marcado = True
        else:
            print("Posição já ocupada")
    return tabuleiro


def verifica_posicao_ocupada(x, y, tabuleiro):
    if (tabuleiro[x][y] == 0):
        return True
    else:
        return False


def verifica_jogo_acabou(tabuleiro):
    ainda_tem_espaco = 0
    sequencia_horizontal_jogador = 0
    sequencia_horizontal_computador = 0
    sequencia_vertical_jogador = [0, 0, 0]
    sequencia_vertical_computador = [0, 0, 0]
    sequencia_diagonal_jogador = 0
    sequencia_diagonal_computador = 0
    sequencia_diagonal_invertido_jogador = 0
    sequencia_diagonal_invertido_computador = 0
    ganhou = False
    x = 0

    for i in range(0, 3):
        for j in range(0, 3):

            if (tabuleiro[i][j] == 0):
                ainda_tem_espaco += 1
                sequencia_horizontal_jogador = 0
                sequencia_horizontal_computador = 0

            elif (tabuleiro[i][j] == 1):
                sequencia_horizontal_computador = 0
                sequencia_horizontal_jogador += 1
                sequencia_vertical_jogador[j] += 1

            elif (tabuleiro[i][j] == 2):
                sequencia_horizontal_jogador = 0
                sequencia_horizontal_computador += 1
                sequencia_vertical_computador[j] += 1

            if (sequencia_horizontal_computador == 3 or sequencia_horizontal_jogador == 3):
                ganhador = tabuleiro[i][j]
                ganhou = True
                print("O ganhador foi o", ganhador)

            if (j == i):
                if (tabuleiro[i][j] == 0):
                    pass
                elif (tabuleiro[i][j] == 1):
                    sequencia_diagonal_jogador += 1
                elif (tabuleiro[i][j] == 2):
                    sequencia_diagonal_computador += 1

            elif (i + j == 2):
                if (tabuleiro[i][j] == 0):
                    pass
                elif (tabuleiro[i][j] == 1):
                    sequencia_diagonal_invertido_jogador += 1
                elif (tabuleiro[i][j] == 2):
                    sequencia_diagonal_invertido_computador += 1
        if (ganhou):
            break

    if (sequencia_diagonal_jogador == 3 or sequencia_diagonal_invertido_jogador == 3):
        ganhador = 1
        ganhou = True
        print("O ganhador foi o", ganhador)
    elif (sequencia_horizontal_computador == 3 or sequencia_diagonal_invertido_computador == 3):
        ganhador = 2
        ganhou = True
        print("O ganhador foi o", ganhador)

    while (x < 3):
        if (sequencia_vertical_jogador[x] == 3):
            ganhador = 1
            ganhou = True
            print("O ganhador foi o", ganhador)
        elif (sequencia_vertical_computador[x] == 3):
            ganhador = 2
            ganhou = True
            print("O ganhador foi o", ganhador)
        x += 1

    # print("Ainda tem {} espaços pra marcar".format(ainda_tem_espaco))
    if (ainda_tem_espaco == 0 or ganhou):
        return True
    else:
        return False

# def tk_interface():


def jogar():
    tabuleiro_xisoubolinha = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    acabou = False
    imprime_mensagem_abertura()

    while (not acabou):
        imprime_tabuleiro(tabuleiro_xisoubolinha)
        tabuleiro_xisoubolinha = jogador_escolha(tabuleiro_xisoubolinha)
        imprime_tabuleiro(tabuleiro_xisoubolinha)
        acabou = verifica_jogo_acabou(tabuleiro_xisoubolinha)

        if (not acabou):
            tabuleiro_xisoubolinha = bot_escolha_aleatoria(
                tabuleiro_xisoubolinha)
            imprime_tabuleiro(tabuleiro_xisoubolinha)
            acabou = verifica_jogo_acabou(tabuleiro_xisoubolinha)
        
        else:
            print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
