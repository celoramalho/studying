def exercicio_4(n):
    if n < 0 or n >= 100:
        print("Número fora do intervalo")
        res = None
    else:
        unidade_extenso = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete",
                        "oito", "nove"]
        meio_extenso = ["dez", "onze", "doze", "treze", "quatorze",
                        "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", ]
        dezena_extenso = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta",
                        "oitenta", "noventa", "cem"]
        pegar_unidade = int(n % 10)
        pegar_dezena = int(n/10)
        if n < 10:
            res = unidade_extenso[n]
        elif n >= 10 and n < 20:
            res = meio_extenso[pegar_unidade]
        elif n >= 20:
            if pegar_unidade == 0:
                res = dezena_extenso[pegar_dezena-2]
            else:
                res = dezena_extenso[pegar_dezena-2] + " e " + unidade_extenso[pegar_unidade]
        return res


for n in range (-1,101):
    print(f'n:{n} ext:{exercicio_4(n)}')
