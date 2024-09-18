print("*********************************")
print("Bem vindo ao jogo de Adivinhação", end="!\n")
print("*********************************")

numero_secreto = 13

chute_str = input("Digite seu número: ")
#print("Você digitou " , chute_str)
chute = int(chute_str)


acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = (chute < numero_secreto) #O ideal é usar parênteses em comparações, mas funciona sem tb
if acertou: #exemplo de if sem parênteses
    print("Você acertou!!!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor): #posso colocar else claro, se n for igual nem maior só pode ser menor
        print("Você errou! O seu chute foi menor do que o número secreto.")
print("Fim de jogo")
