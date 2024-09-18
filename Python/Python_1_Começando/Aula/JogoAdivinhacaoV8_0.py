import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação", end="!\n")
print("*********************************\n")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Qual nível de dificuldade?")
print("(1) Fácil \n(2) Médio \n(3) Difícil")

nivel = int(input("Nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("--------------------[Rodada: {} de {}]----------------------".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número de 1 a 100: ")
    chute = int(chute_str)
    print("Você digitou: ", chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!\n")
        continue  # VAI PRA PROXIMA INTERACAO

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = (chute < numero_secreto)
    if (acertou):
        print("                      Você acertou!!!")
        break  # ENCERRA O LAÇO
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
print("O número era", numero_secreto)
print("-----------------------Fim de Jogo------------------------")
