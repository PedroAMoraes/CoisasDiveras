import random

TIPO_CARTA = [
    '0','1','2','3','4','5','6','7','8','9',
    '1','2','3','4','5','6','7','8','9', 
    'BLOQUEIO','INVERSO','MaisDois',
    'BLOQUEIO','INVERSO','MaisDois'
              ]
CARTAS_ESPECIAIS = [
    'CURINGA','MaisQuatro','CURINGA','MaisQuatro',
    'CURINGA','MaisQuatro','CURINGA','MaisQuatro'
                    ]
CATEGORIA_CARTA = ('Especial','Azul','Vermelho','Amarelo','Verde')
CARTAS_INICIAIS = 7


jogadores = dict({
    'jogador_1' : [],
    'jogador_2' : [],
    'jogador_3' : [],
    'jogador_4' : []
})

prefixo_nome_jogador = 'jogador_'
carta_mesa = ''
cor_mesa = ''
tipo_mesa = ''
jogador_atual = 1
nome_jogador_atual = ''
nome_jogador = []

def Criar_monte(categoria_da_carta, cartas_especiais, tipo_da_carta):
    monte = []
    # juntar tipo + categoria e colocar em 'monte'
    for categoria_carta in categoria_da_carta:
        if categoria_carta == 'Especial':
            for tipo_especial in cartas_especiais:
                carta_temp = f'{tipo_especial} : {categoria_carta}'
                monte.append(carta_temp)
        else:
            for tipo_carta in tipo_da_carta:
                carta_temp = f'{tipo_carta} : {categoria_carta}'
                monte.append(carta_temp)
    return monte

def Embaralhas_monte(monte):
    # embaralhar para que não repita a ordem sempre
    random.shuffle(monte) 
    return monte

def Nomear_Jogadores(prefixo):
    nomes = []
    for i in range(1,5):
        nomes.append(prefixo + str(i))
    return nomes

def Identificar_Jogador_Atual(nro_jogador_atual, nomes):
    nro_jogador_atual -=1
    return nomes[nro_jogador_atual]


def Entregar_cartas(monte,cartas_iniciais, carta_mesa, cor_mesa, categorias_cartas, tipo_cartas, nome_jogador, **cartas_jogadores):
    for i in range(4):
        for n_de_cartas in range(cartas_iniciais): # entregar a carta pelo numero N de cartas iniciais
            jogadores[nome_jogador[i]].append(monte.pop()) # remover a carta do 'monte' ao dar para o jogador X

        carta_mesa = (monte.pop(0)) # passar uma carta do monte a mesa
        while 'Especial' in carta_mesa: #evitar que a primeira carta seja do tipo 'especial'
            monte.append(carta_mesa)
            carta_mesa = (monte.pop(0))

    cor_mesa, tipo_mesa = Identificar_cor_tipo(carta_mesa= carta_mesa, categorias_cartas= categorias_cartas, tipos_cartas= tipo_cartas  )


    return jogadores, carta_mesa, monte, cor_mesa, tipo_mesa

def Identificar_cor_tipo( carta_mesa,categorias_cartas, tipos_cartas):
    if 'Especial' in carta_mesa: # jogador escolher a cor
        print("Escolha uma cor! \n 1 - AZUL 2- VERMELHO \n 3 - AMARELO  4 - VERDE  ")
        escolha_cor = int(input())
        cor_carta_da_mesa = categorias_cartas[escolha_cor]
        print(f'cor escolhida - {categorias_cartas[escolha_cor]}')
        tipo_mesa = '(cor escolhida)'
    else:
        for cor in categorias_cartas: # detectar cor mesa
            if cor == 'Especial':
                continue
            if cor in carta_mesa:
                cor_carta_da_mesa = cor
                break
        for tipo in tipos_cartas:
            if tipo in carta_mesa:
                tipo_mesa = tipo
                break
    
    return cor_carta_da_mesa, tipo_mesa

def Validar_jogada( carta_mesa, categorias_carta, tipos_carta, nome_jogador_atual, **cartas_disponiveis_mao_jogador):
    valido = False

    cor_mesa,tipo_mesa = Identificar_cor_tipo(
        carta_mesa= carta_mesa, 
        categorias_cartas= categorias_carta, 
        tipos_cartas= tipos_carta )
    for carta_jogador_comparando in jogadores[nome_jogador_atual]: # analisar se a carta é valida par a jogada
        if tipo_mesa in carta_jogador_comparando: # se a jogada é valida pelo tipo de carta
            valido = True
        if cor_mesa in carta_jogador_comparando or 'Especial' in carta_jogador_comparando: # se a jogada é valida pela cor ou pelo jogador ter uma carta ESPECIAL
            valido = True
        
    if valido:   
        return True, cor_mesa, tipo_mesa
    else:
        return False, cor_mesa, tipo_mesa

# inicio jogo

monte = Criar_monte(
            categoria_da_carta=CATEGORIA_CARTA, 
            cartas_especiais=CARTAS_ESPECIAIS, 
            tipo_da_carta=TIPO_CARTA)

monte = Embaralhas_monte(monte)
nome_jogador = Nomear_Jogadores(prefixo= prefixo_nome_jogador)

nome_jogador_atual = Identificar_Jogador_Atual(jogador_atual, nome_jogador)

jogadores, carta_mesa, monte, cor_mesa, tipo_mesa = Entregar_cartas(
            monte = monte, cartas_iniciais= CARTAS_INICIAIS, cartas_jogadores= jogadores,
            carta_mesa= carta_mesa, cor_mesa= cor_mesa, categorias_cartas= CATEGORIA_CARTA,
            tipo_cartas= TIPO_CARTA, nome_jogador= nome_jogador)

while True:
    nome_jogador_atual = Identificar_Jogador_Atual(jogador_atual, nome_jogador)
    valido, cor_mesa, tipo_mesa = Validar_jogada(
                cartas_disponiveis_mao_jogador= jogadores, 
                carta_mesa= carta_mesa, categorias_carta= CATEGORIA_CARTA, 
                tipos_carta= TIPO_CARTA, nome_jogador_atual= nome_jogador_atual)

    print(carta_mesa)
    print(jogadores[nome_jogador_atual]) 

    if valido:
        carta_jogada = int(input('escolha carta: ')) # escolher a carta
        while carta_jogada > len(jogadores[nome_jogador_atual]):
            print('numero invalido')
            carta_jogada = int(input('escolha carta: '))
        while True:
            tipo_cor_valido = cor_mesa in jogadores[nome_jogador_atual][carta_jogada-1] or 'Especial' in jogadores[nome_jogador_atual][carta_jogada-1] or tipo_mesa in jogadores[nome_jogador_atual][carta_jogada-1]
            if tipo_cor_valido:
                break
            else:
                carta_jogada = int(input('escolha outra carta: '))

        monte.append(carta_mesa)
        carta_mesa = jogadores[nome_jogador_atual][carta_jogada-1]
        jogadores[nome_jogador_atual].remove(carta_mesa)
    else:
        print('Compre uma carta')
        jogadores[nome_jogador_atual].append(monte.pop(0)) #comprar a carta mais velha do monte

    print('\n')
    print(carta_mesa)
    print(jogadores[nome_jogador_atual])
    # print(f'Cor mesa: {cor_mesa}')
    # print(f'Tipo mesa: {tipo_mesa}')
    # print(jogadores['jogador_1'])
    # print(jogadores['jogador_2'])
    # print(jogadores['jogador_3'])
    # print(jogadores['jogador_4'])