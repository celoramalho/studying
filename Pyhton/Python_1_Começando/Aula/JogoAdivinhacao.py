print("*********************************")
print("Bem vindo ao jogo de adivinhação", end="!\n")
print("*********************************")


num_secreto = 13
chute_str = input("Digite seu número: ") # O imput sempre devolve uma string (str), para receber int

chute = int(chute_str) # O imput sempre devolve uma string (str), por isso precisamos converter o tipo de variável

print("Você digitou: ", chute)

if (num_secreto == chute):
    print("\nVocê acertou!")
else:
    print("Você errou :(")
print("\n***********Fim do jogo***********")