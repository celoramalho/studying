require_relative 'ui'
require_relative 'heroi'

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
      jogador = Heroi.new
      jogador.linha = linha
      jogador.coluna = coluna_do_heroi
      return jogador
    end              
  end
  nil
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

def soma_vetor(vetor1, vetor2)
  [vetor1[0] +vetor2[0], vetor1[1]+ vetor2[1]]
end

def posicoes_validas_a_partir_de(mapa, novo_mapa, posicao)
  posicoes = []
  movimentos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
  movimentos.each_with_index do | movimento |
    possivel_posicao = soma_vetor(movimento, posicao)
    if posicao_valida?(mapa, possivel_posicao) && posicao_valida?(novo_mapa, possivel_posicao)
      posicoes << possivel_posicao
    end
  end

posicoes
end

def move_fantasma(mapa, novo_mapa, linha, coluna)

  posicoes = posicoes_validas_a_partir_de mapa, novo_mapa, [linha, coluna]

  return if posicoes.empty?

  aleatoria =  rand posicoes.size
  posicao = posicoes[aleatoria]
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

def jogador_perdeu?(mapa)
  perdeu = !encontra_jogador(mapa)
end

def joga(nome)
   #nosso jogo aqui
  mapa = le_mapa 3

  while true
    desenha mapa
    direcao = pede_movimento
    heroi = encontra_jogador mapa #objeto
    nova_posicao = heroi.calcula_nova_posicao direcao #objeto

    if !posicao_valida? mapa, nova_posicao.to_array
      next
    end

    heroi.remove_do mapa
    if mapa[nova_posicao.linha][nova_posicao.coluna] == "*"
        mapa[nova_posicao.linha][nova_posicao.coluna + 1] = " "
        mapa[nova_posicao.linha][nova_posicao.coluna + 2] = " "
        mapa[nova_posicao.linha][nova_posicao.coluna + 3] = " "
        mapa[nova_posicao.linha][nova_posicao.coluna + 4] = " "
    end
    
    nova_posicao.coloca_no mapa

    mapa = move_fantasmas mapa

    if jogador_perdeu?(mapa)
      game_over(nome)
      break
    end
  end
end

def inicia_foge_foge
    nome = da_boas_vindas
    joga nome
end