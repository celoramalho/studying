puts ("Bem vindo ao jogo da adivinhação")
puts "Qual é o seu nome?"
nome = gets

puts "Começaremos o jogo para você, " + nome

puts
puts ""
puts ()
puts ("")
puts "\n" #new-line

puts "Escolha um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto"

puts "Tentativa 1"
puts "Entre com o número: "
chute = gets
puts "Será que acertou? Você chutou " + chute
puts "\n\n\n"

puts chute.to_i == numero_secreto



=begin
verificadno se acertou
if chute.to_i == numero_secreto
  puts "Acertou!"
else
 puts "Errou!"
end
=end

acertou = chute.to_i == numero_secreto

if acertou
  puts "Acertou!"
else
  maior = numero_secreto > chute.to_i
  if maior
    puts "O número secreto é maior!"
  else
    puts "O número secreto é menor!"
  end
end

diferenca = numero_secreto - chute.to_i
if diferenca == 0
  puts "Acertou!"
else
  
  if diferenca > 0
    puts "O número secreto é maior!"
  else
    puts "O número secreto é menor!"
  end
end
