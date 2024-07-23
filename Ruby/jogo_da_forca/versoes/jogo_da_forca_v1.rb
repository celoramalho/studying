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
nome = da_boas_vindas

def pede_um_chute(chutes, erros, palavra_forca)
  puts "\n\n\n\n"
  puts "Erros até agora: #{erros}"
  puts "Chutes até agora: #{chutes}"
  puts palavra_forca.join(' ')
  puts "Entre com uma letra ou uma palavra"
  chute = gets.strip
  puts "Será que acertou? Você chutou #{chute}"
  chute
end

def joga(nome)
  palavra_secreta = escolhe_palavra_secreta
  erros = 0
  chutes = []
  pontos_ate_agora = 0
  palavra_forca = []

  while erros < 5
    chute = pede_um_chute(chutes, erros, palavra_forca)
    chutes << chute

    chutou_uma_letra = chute.size == 1
    if chutou_uma_letra
      i = 0
      for letra in palavra_secreta.split("")
        if letra == chute
          palavra_forca[i] = chute
        elsif palavra_forca[i] == nil
          palavra_forca[i] = "_"
        end
        i += 1
      end
    
    acertou = (chute == palavra_secreta) or (palavra_forca.include?("_"))
      
    if !acertou and !chutou_uma_letra
        puts "Que pena.. errou"
        pontos_ate_agora -= 30
        erros += 1
      end
    end
    if acertou
      puts "Parabéns!"
      pontos_ate_agora += 100
      break
    end
    # Verificar se acertou ou errou
  end
  puts = "Você ganhou #{pontos_ate_agora} pontos."

end

loop do 
  joga nome
  if nao_quer_jogar?
    break
  end
end