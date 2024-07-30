require_relative 'ui'

def le_mapa(numero)
  arquivo = "mapa#{numero}.txt"
  texto = File.read arquivo
  mapa = (texto.gsub("\r", "").split "\n")
end

def encontra_jogador(mapa)
  caractere_do_heroi = "H"
  mapa.each_with_index do |linha_atual, linha| #for linha = 0..(mapa.size-1); linha_atual = mapa[linha]
    coluna_do_heroi = linha_atual.index caractere_do_heroi
    if coluna_do_heroi != nil #Or if coluna_do_heroi
      return[linha, coluna_do_heroi]
    end              
  end
  #nao achei!
end

def calcula_nova_posicao(heroi, direcao)
  heroi = heroi.dup
  movimentos = { 
    "W" => [-1, 0],
    "S" => [1, 0],
    "A" => [0, -1],
    "D" => [0, 1] 
  }
  movimento = movimentos[direcao]
  heroi[0] += movimento[0] #LINHA
  heroi[1] += movimento[1] #COLUNA
  heroi
end

def posicao_valida?(mapa, posicao)
  linhas_size = mapa.size
  colunas_size = mapa[0].size #PEGA A PRIMEIRA LINHA E CONTABILIZA O TAMANHO
  estourou_linhas = posicao[0] < 0 || posicao[0] >= linhas_size
  estourou_colunas = posicao[1] < 0 || posicao[1] >= colunas_size
  
  if estourou_linhas || estourou_colunas
    return false
  end

  valor_atual = mapa[posicao[0]][posicao[1]]
  if valor_atual == "X" || valor_atual == "F"
    return false
  end
  true
end

def posicoes_validas_a_partir_de(mapa, novo_mapa, posicao)
  posicoes = []
  movimentos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
  
  movimentos.each_with_index do | movimento |
    possivel_posicao = posicao.dup
    possivel_posicao[0] += movimento[0]
    possivel_posicao[1] += movimento[1]
    if posicao_valida?(mapa, possivel_posicao) && posicao_valida?(novo_mapa, possivel_posicao)
      posicoes << possivel_posicao
    end
  end

posicoes
end

def move_fantasma(mapa, novo_mapa, linha, coluna)

  posicoes = posicoes_validas_a_partir_de mapa, novo_mapa, [linha, coluna]

  return if posicoes.empty?
  posicao = posicoes[0]
  mapa[linha][coluna] = " "
  novo_mapa[posicao[0]][posicao[1]] = "F"
end

def copia_mapa(mapa)
  novo_mapa = mapa.join("\n").tr("F", " ").split "\n"
end

def move_fantasmas(mapa)
  caractere_do_fantasma = "F"
  novo_mapa = copia_mapa mapa
  mapa.each_with_index do |linha_atual, linha|
    linha_atual.chars.each_with_index do | caractere_atual, coluna|
      eh_fantasma =  caractere_atual == caractere_do_fantasma
      if eh_fantasma
        move_fantasma mapa, novo_mapa, linha, coluna
      end
    end
  end
  novo_mapa
end

def joga(nome)
   #nosso jogo aqui
  mapa = le_mapa 2

  while true
    desenha mapa
    direcao = pede_movimento
    heroi = encontra_jogador mapa
    nova_posicao = calcula_nova_posicao heroi, direcao
    if !posicao_valida? mapa, nova_posicao
      next
    end

    mapa[heroi[0]][heroi[1]] = " "
    mapa[nova_posicao[0]][nova_posicao[1]] = "H"

    mapa = move_fantasmas mapa
  end
end

def inicia_foge_foge
    nome = da_boas_vindas
    joga nome
end