total = 0
palavra = "marcelo"
acabou = False
while (not acabou):
    acabou = (total == len(palavra))
    total = total + 1
print(total)