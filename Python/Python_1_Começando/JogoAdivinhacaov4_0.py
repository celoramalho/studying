print("*********************************")
print("Bem vindo ao jogo de Adivinhação", end="!\n")
print("*********************************")

numero_secreto = 13
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Rodada: {} de {}".format(rodada, total_de_tentativas)) #sem a função format fica assim print("Rodada: ", rodada, "de ",total_de_tentativas)
    chute_str = input("Digite seu número: ")
    #print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = (chute < numero_secreto)
    if (acertou):
        print("Você acertou!!!")
        rodada = total_de_tentativas + 1
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor): #posso colocar else claro, se n for igual nem maior só pode ser menor
            print("Você errou! O seu chute foi menor do que o número secreto.")
        rodada = rodada + 1
print("Fim de jogo")

#python não tem um laço com uma condiçãio de saída,
#diferente de outras linguagens de priogramação conhecida como do-while