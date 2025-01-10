import random

CARTAS_BASICAS = ['0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','BLOQUEIO','INVERSO','MaisDois','BLOQUEIO','INVERSO','MaisDois']
CARTAS_ESPECIAIS = ['CURINGA','MaisQuatro','CURINGA','MaisQuatro','CURINGA','MaisQuatro','CURINGA','MaisQuatro'] ##cartas
TODAS_CARTAS = (CARTAS_BASICAS + CARTAS_ESPECIAIS)
TIPOS = ('Especial','Azul','Vermelho','Amarelo','Verde')

Cartas_Amarelas = CARTAS_BASICAS.copy()
Cartas_Vermelhas = CARTAS_BASICAS.copy() ##criar as de cada cor
Cartas_Azuis  = CARTAS_BASICAS.copy()
Cartas_Verdes = CARTAS_BASICAS.copy()

id_cartas = []
id_carta_mão = []
id_carta_monte = []

cartas_jogador = [] #cartas na mao do jogador
tipo_cartas_jogador = [] #tipo de carta na mão do jnogador

monte = [] #cartas para serem coletadas
tipo_cartas_monte = [] #tipo da carta no monte
ultima_carta = '' #carta mais recente na mesa
tipo_ultima_carta = ''
CARTAS_INICIAIS = 7 #quantidade de cartas iniciais


def EmbaralharCartas():

#juntar as cartas no monte

    while True:
        monte.append(Cartas_Amarelas.pop())
        tipo_cartas_monte.append('Amarelo')
        if Cartas_Amarelas == []:
            break
    while True:
        monte.append(Cartas_Vermelhas.pop())
        tipo_cartas_monte.append('Vermelho')
        if Cartas_Vermelhas == []:
            break
    while True:
        monte.append(Cartas_Azuis.pop())
        tipo_cartas_monte.append('Azul')
        if Cartas_Azuis == []:
            break
    while True:
        monte.append(Cartas_Verdes.pop())
        tipo_cartas_monte.append('Verde')
        if Cartas_Verdes == []:
            break
    while True:
        monte.append(CARTAS_ESPECIAIS.pop())
        tipo_cartas_monte.append('Especial')
        if CARTAS_ESPECIAIS == []:
            break
    while True:
        id_cartas.append(monte.pop() + ' ' + tipo_cartas_monte.pop())
        if(monte == [] and tipo_cartas_monte == []):
            break
    
    random.shuffle(id_cartas)

def Entregar_cartas():
    for i in range(0,CARTAS_INICIAIS):
        id_carta_mão.append(id_cartas.pop())
        for ii in TIPOS:
            if ii in id_carta_mão[i]:
                tipo_cartas_jogador.append(ii)
                break
        for numero_da_carta in TODAS_CARTAS:
            if numero_da_carta in id_carta_mão[i]:
                cartas_jogador.append(numero_da_carta)
                break
    
def AtualizarMão():
    tipo_cartas_jogador.clear()
    cartas_jogador.clear()
    for i in range(0,len(id_carta_mão)):
        for ii in TIPOS:
            if ii in id_carta_mão[i]:
                tipo_cartas_jogador.append(ii)
                break
        for numero_da_carta in TODAS_CARTAS:
            if numero_da_carta in id_carta_mão[i]:
                cartas_jogador.append(numero_da_carta)
                break



EmbaralharCartas()
Entregar_cartas()


for i1 in TIPOS:
    if i1 in id_cartas[0]:
        tipo_ultima_carta = i1
        continue
for i2 in TODAS_CARTAS:
    if i2 in id_cartas[0]:
        ultima_carta = i2
        continue

    

print('Carta na mesa: ',ultima_carta, tipo_ultima_carta, '\n')
print(cartas_jogador)
print(tipo_cartas_jogador)
print(id_carta_mão)



jogada_possivel = (tipo_ultima_carta in tipo_cartas_jogador or ultima_carta in cartas_jogador)

if(jogada_possivel):
    while True:
        escolha_carta = int(input('Escolha uma carta para ser jogada'))
        escolha_carta -=1 #primeira carta ser zero, segunda ser um...
        #checar se a jogada é valida
        jogada_valida = (tipo_cartas_jogador[escolha_carta] == tipo_ultima_carta 
        or cartas_jogador[escolha_carta] == ultima_carta
        or tipo_ultima_carta == 'Especial' 
        or tipo_cartas_jogador[escolha_carta] == 'Especial')

        if(jogada_valida == True):
            print("Jogada valida")
            break
        else:
            print("jogada invalida")
    id_carta_mão[escolha_carta] = 'jogada' #transforma a carta atual em uma jogada
    id_carta_mão.remove('jogada')
    AtualizarMão() #atualiza o ID das cartas para verificação
    id_cartas.append(id_cartas.pop(0)) #atualizar o monte(joga a mais velha para o inicio da fila)

else:
    id_carta_mão.append(id_cartas.pop()) #comprar uma carta
    AtualizarMão()

for i1 in TIPOS:
    if i1 in id_cartas[0]:
        tipo_ultima_carta = i1
        continue
for i2 in TODAS_CARTAS:
    if i2 in id_cartas[0]:
        ultima_carta = i2
        continue
print('Carta na mesa: ',ultima_carta, tipo_ultima_carta, '\n')
print(cartas_jogador)
print(tipo_cartas_jogador)
print(id_carta_mão)


