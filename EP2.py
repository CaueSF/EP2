# DEFINE POSIÇÕES
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    lugar = []
    if orientacao == 'vertical':
        for pos in range(tamanho):
            lugar = [linha + pos, coluna]
            posicoes.append(lugar)
    elif orientacao == 'horizontal':
        for pos in range(tamanho):
            lugar = [linha, coluna + pos]
            posicoes.append(lugar)
    return posicoes

# PREENCHE FROTA
def preenche_frota(info_frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in info_frota:
        info_frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
        info_frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    return info_frota

# FAZ JOGADA
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

# POSICIONA FROTA
def posiciona_frota(info_navios):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for nomes in info_navios:
        listao = info_navios[nomes]
        for lista in listao:
            for i in lista:
                linha = i[0]
                coluna = i[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro

# QUANTAS EMBARCAÇÕES AFUNDADAS
def afundados(info_navios, tabuleiro):
    afundou = 0
    for nomes in info_navios:
        listao = info_navios[nomes]
        for navio in listao:
            x = 0
            tamanho = len(navio)
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    x += 1
            if x == tamanho:
                afundou += 1
    return afundou

#POSIÇÃO VÁLIDA
def posicao_valida(info_frota, linha, coluna, orientacao, tamanho):
    def_pos = define_posicoes(linha, coluna, orientacao, tamanho)
    for i in def_pos:
        linha2 = i[0]
        coluna2 = i[1]
        if linha2 < 0 or linha2 > 9:
            return False
        if coluna2 < 0 or coluna2 > 9:
            return False
    for i in def_pos:
        linha2 = i[0]
        coluna2 = i[1]

        for nomes in info_frota:
            x = info_frota[nomes]
            for y in x:
                for z in range(len(y)):
                    linha3 = y[z][0]
                    coluna3 = y[z][1]
                    if linha3 == linha2 and coluna3 == coluna2:
                        return False
    return True