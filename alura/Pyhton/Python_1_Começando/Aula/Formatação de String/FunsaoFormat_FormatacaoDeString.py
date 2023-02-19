#1 O valor dentro do format são impressos dentro das chaves de forma respectiva
print("Tentativa {} de {}".format(3,10))


#2 Os número dento das chaves indicam qual elemento inserir ali, o primeiro {0}, o segundo {1}, etc
print("Tentativa {1} de {0}".format(1,9)) 

#3 Testando formas de impressão de valores
print("R$ {}".format(1.59))

#4 Imprime o valor como float
print("R$ {:f}".format(1.59)) 

#Imprime o valor como float exibindo 3 casas após a vírgula
print("R$: {:.2f}".format(1)) 
print("R$: {:.2f}".format(1.5)) 
print("R$: {:.2f}".format(49.5))
print("R$: {:.2f}".format(1234.4))
print("R$: {:7.2f}".format(1234.4))
print("R$: {:7.2f}".format(4.5))
print("R$: {:07.2f}".format(4.5))
print("R$: {:7d}".format(4))
print("R$: {:07d}".format(4))
print("R$: {:07.2f}".format(4))

# Datas
print("Data {:02d}/{:02d}".format(4,12))
print("Data {:02d}/{:02d}/{:4d}".format(4,12,2003)) #interpolação de string

