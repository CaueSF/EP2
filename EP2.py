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