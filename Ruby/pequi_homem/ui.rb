def da_boas_vindas
  puts "Bem vindo ao Foge-Foge"
  puts "Qual é o seu nome?"
  nome = gets.strip
  puts "\n\n\n\n\n"
  puts "Começando o jogo para você, #{nome}"
  nome
end

def desenha (mapa)
  puts mapa
end

def pede_movimento
    puts "Para onde deseja ir?"
    movimento = gets.strip.upcase
end

def game_over(nome)
  puts "\n\n\n\n\n"
  puts "GAME OVER"
  puts "Que pena, você perdeu #{nome}!"
end