def da_boas_vindas
  puts "Bem vindo ao jogo da adivinhação\nQual é o seu nome?" #+ nome = gets
  puts "Começaremos o jogo para você, " + nome=gets
end

def sorteia_numero_secreto
  puts "Escolha um número secreto entre 0 e 200..."
  numero_sorteado = 175
  puts "Escolhido... que tal adivinhar hoje nosso número secreto"
  return numero_sorteado
end

def pede_um_numero(chutes, tentativa, limite_tentativas)
  puts "===========Tentativa " + tentativa.to_s + " de " + limite_tentativas.to_s + "==========="
  puts "Chutes até agora: " + chutes.to_s
  puts "Entre com o número: "
  chute = gets
  puts "Será que acertou? Você chutou " + chute
  puts "\n\n\n"
  chute.to_i
end

def verifica_se_acertou(numero_secreto, chute)
  acertou = numero_secreto == chute.to_i

  if acertou
    puts "Acertou!"
    return true
  end

  maior = numero_secreto > chute
  if maior
    puts "O número secreto é maior!"
  else
    puts "O número secreto é menor!"
  end
  false
end

da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_tentativas = 5
chutes = []
total_de_chutes = 0
for tentativa in 1..limite_tentativas
  chute = pede_um_numero(chutes, tentativa, limite_tentativas)
  chutes[total_de_chutes] = chute
  total_de_chutes +=1

  puts chute == numero_secreto
  if verifica_se_acertou(numero_secreto, chute)
        break
  end
end