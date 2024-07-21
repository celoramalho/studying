def da_boas_vindas
  puts "Bem vindo ao jogo da adivinhação\nQual é o seu nome?" #+ nome = gets
  puts "Começaremos o jogo para você, " + nome=gets.strip
  return nome
end

def pede_dificuldade
      puts  "Qual o nível de dificuldade que deseja? (1 fácil, 5 difícil)"
      dificuldade = gets.to_i
      return dificuldade
end

def sorteia_numero_secreto(dificuldade)
  case dificuldade
    when 1
      maximo = 30
    when 2
      maximo = 60
    when 3
      maximo = 100
    when 4
      maximo = 150
    else
      maximo = 200
    end
  puts "Escolha um número secreto entre 1 e #{maximo}..."
  numero_sorteado = rand(maximo) + 1
  puts "Escolhido... que tal adivinhar hoje nosso número secreto"
  return numero_sorteado
end

def joga(nome, dificuldade)
  numero_secreto = sorteia_numero_secreto(dificuldade)
  limite_tentativas = 5
  pontos_ate_agora = 1000
  chutes = []

  for tentativa in 1..limite_tentativas
    chute = pede_um_numero(chutes, tentativa, limite_tentativas)
    #chutes[chutes.size] = chute
    chutes << chute
    
    if nome == "Griffo"
        puts "Acertou!"
        break
    end
  
    break if verifica_se_acertou(numero_secreto, chute)
    pontos_a_perder = (chute - numero_secreto).abs / 2.0
    pontos_ate_agora -= pontos_a_perder
  end
  puts "Você ganhou com #{pontos_ate_agora} pontos."
end

def pede_um_numero(chutes, tentativa, limite_tentativas)
  puts "===========Tentativa #{tentativa} de #{limite_tentativas}==========="
  puts "Chutes até agora: #{chutes}"
  puts "Entre com o número: "
  chute = gets.strip
  puts "Será que acertou? Você chutou #{chute}"
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

def quer_jogar
    puts "Deseja jogar novamente? [S/N]: "
    desejo = gets.strip
    desejo.upcase == "S"
end

nome = da_boas_vindas
dificuldade = pede_dificuldade

loop do
  joga nome, dificuldade
  if !quer_jogar
      break
  end
end
