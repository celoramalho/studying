
numero1 = 10
numero2 = "20"
soma = numero1 + numero2
#Em JavaScript numero1 é convertido
#para string (str) imprimindo: "1020"

#Em python não funciona, e a seguinte mensagem de erro é mostrada
#TypeError: unsupported operand type(s) for +: 'int' and 'str'


numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)
#Agora em JavaScript, o número 2 que é convertido para número inteiro (int)
#Exibindo assim o resultado: 200  (10*20)

#Já em python, mesmo sendo rígido nesse sentido, não da erro com sinal de * entre variaveis de tipo str e int.
#Na verdade agora será impresso: 20202020202020202020  (É impresso 10 vezes o número 20)
#Não há conversão nesse caso do pythom, trata-se de um SYNTAX SUGAR do mundo python. Um 
#SYNTAX SUGAR, açúcar sintático da linguagem, apenas simplifica algo que seria trabalhoso, mas não muda a 
#característica da linguagem. Então, a invés de escrever dez vezes o número 20, podemos simplificar e escrever 10 * "20"


print("""O que é um sintático?")
adjetivo Relacionado com a sintaxe, com a parte da gramática que se dedica
ao estudo das palavras enquanto constituintes de uma frase. Em conformidade com as
regras da sintaxe: o texto não possui correção ou perfeição sintática.""")