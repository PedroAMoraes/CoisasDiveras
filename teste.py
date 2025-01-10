jogadores = dict({
    'jogador_1' : [1],
    'jogador_2' : [2],
    'jogador_3' : [3]
})

def Funcao(nome, **dicionario):
    print(jogadores[nome])
    jogadores[nome].append('agua')
    return(dicionario)

x = 'jogador_1'

a = Funcao(dicionario= jogadores, nome = x)

print(a)
# jogadores['jogador_3'] # [3]



# jogadoratual = 32443
# nomejogador = 'jogador_'

# nomejogadoratual = nomejogador + str(jogadoratual)

# print(nomejogadoratual)