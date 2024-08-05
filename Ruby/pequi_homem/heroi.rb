class Heroi
  attr_accessor :linha, :coluna

  def calcula_nova_posicao(direcao)
    heroi = self.dup
    movimentos = { 
      "W" => [-1, 0],
      "S" => [1, 0],
      "A" => [0, -1],
      "D" => [0, 1] 
    }
    movimento = movimentos[direcao]
    heroi.linha += movimento[0] #LINHA
    heroi.coluna += movimento[1] #COLUNA
    heroi
  end

end
=begin
guilherme = Heroi.new
guilherme.linha = 15
guilherme.coluna = 3

puts "O guilherme está em #{guilherme.linha} #{guilherme.coluna}"
puts guilherme

carlos = Heroi.new
carlos.linha = 6
carlos.coluna  = 18
=end

