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

#POSICIONANDO FROTA
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

i = 0
while i < 1:
    print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
    q_linha = int(input('Qual linha? '))
    q_coluna = int(input('Qual coluna? '))
    q_orientacao = int(input(('[1] Vertical [2] Horizontal >')))
    if q_orientacao == 1:
        q_orientacao = 'vertical'
    elif q_orientacao == 2:
        q_orientacao = 'horizontal'

    if posicao_valida(frota, q_linha, q_coluna, q_orientacao, 4) == True:
        preenche_frota(frota, 'porta-aviões', q_linha, q_coluna, q_orientacao, 4)
        i += 1
    else:
        print('Esta posição não está válida!')

i = 0
while i < 2:
    print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
    q_linha = int(input('Qual linha? '))
    q_coluna = int(input('Qual coluna? '))
    q_orientacao = int(input(('[1] Vertical [2] Horizontal >')))
    if q_orientacao == 1:
        q_orientacao = 'vertical'
    elif q_orientacao == 2:
        q_orientacao = 'horizontal'

    if posicao_valida(frota, q_linha, q_coluna, q_orientacao, 3) == True:
        preenche_frota(frota, 'navio-tanque', q_linha, q_coluna, q_orientacao, 3)
        i += 1
    else:
        print('Esta posição não está válida!')

i = 0
while i < 3:
    print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
    q_linha = int(input('Qual linha? '))
    q_coluna = int(input('Qual coluna? '))
    q_orientacao = int(input(('[1] Vertical [2] Horizontal >')))
    if q_orientacao == 1:
        q_orientacao = 'vertical'
    elif q_orientacao == 2:
        q_orientacao = 'horizontal'

    if posicao_valida(frota, q_linha, q_coluna, q_orientacao, 2) == True:
        preenche_frota(frota, 'contratorpedeiro', q_linha, q_coluna, q_orientacao, 2)
        i += 1
    else:
        print('Esta posição não está válida!')

i = 0
while i < 4:
    print('Insira as informações referentes ao navio submarino que possui tamanho 1')
    q_linha = int(input('Qual linha? '))
    q_coluna = int(input('Qual coluna? '))

    if posicao_valida(frota, q_linha, q_coluna, q_orientacao, 1) == True:
        preenche_frota(frota, 'submarino', q_linha, q_coluna, q_orientacao, 1)
        i += 1
    else:
        print('Esta posição não está válida!')

print(frota)