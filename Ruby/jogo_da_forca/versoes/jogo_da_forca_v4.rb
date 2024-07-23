def da_boas_vindas
  puts "Qual é o seu nome?"
  nome = gets.strip
  puts "Começaremos o jogo para você, #{nome}."
  nome
end

def escolhe_palavra_secreta
  puts "Escolhendo uma palavra secreta..."
  palavra_secreta = "programador"
  puts "Palavra secreta com #{palavra_secreta.size} letras.... boa sorte!"
  palavra_secreta
end

def nao_quer_jogar?
  puts "Deseja jogar novamente? [S/N]"
  quero_jogar = gets.strip
  nao_quero_jogar = quero_jogar.upcase == "N"

end


def pede_um_chute(chutes, erros) #user_interface
  puts "\n\n\n\n"
  puts "Erros até agora: #{erros}"
  puts "Chutes até agora: #{chutes}"
  puts "Entre com uma letra ou uma palavra"
  chute = gets.strip
  puts "Será que acertou? Você chutou #{chute}"
  chute
end

=begin #Substitui pela função nativa count
def conta(texto, letra)
  total_encontrado = 0
    for caractere in texto.char #i in 0..(texto.size-1)
      if caractere == letra
        total_encontrado += 1
      end
    end
    total_encontrado
end
=end

def joga(nome) #business
  palavra_secreta = escolhe_palavra_secreta
  erros = 0
  chutes = []
  pontos_ate_agora = 0
  palavra_forca = []

  while erros < 5
    chute = pede_um_chute(chutes, erros)
    if chutes.include? chute
      puts "Você já chutou #{chute}"
      next # Proxima iteração
    end
    chutes << chute

    chutou_uma_letra = chute.size == 1
    if chutou_uma_letra
      letra_procurada = chute[0]
      letra_encontrado = 0
      total_encontrado = palavra_secreta.count letra_procurada   #Usei função nativa count
    if total_encontrado == 0         #retirei a dupla negação != else -> == else
      puts "Letra não encontrada."
      erros += 1
    else
      puts "Letra encontrada #{total_encontrado} vezes."
    end
  else
    acertou = chute == palavra_secreta
    if acertou
      puts "Parabéns!"
      pontos_ate_agora += 100
      break
    else
      puts "Que pena... Você errou."
      pontos_ate_agora -= 30
    end
    # Verificar se acertou ou errou
  end
end
  puts = "Você ganhou #{pontos_ate_agora} pontos."
end


nome = da_boas_vindas
loop do 
  joga nome
  if nao_quer_jogar?
    break
  end
end