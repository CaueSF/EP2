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