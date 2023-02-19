print("*********************************")
print("Bem vindo ao jogo de Adivinhação", end="!\n")
print("*********************************")

numero_secreto = 13

chute_str = input("Digite seu número: ")
#print("Você digitou " , chute_str)
chute = int(chute_str)


acertou = numero_secreto == chute
if(acertou):
    print("Você acertou!!!")
else:
    if(chute > numero_secreto):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(chute < numero_secreto): #posso colocar else claro, se n for igual nem maior só pode ser menor
        print("Você errou! O seu chute foi menor do que o número secreto.")
print("Fim de jogo")