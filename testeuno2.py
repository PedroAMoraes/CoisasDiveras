jogadores = {
    'j1' : [1,2,3],
    'j2' : [4,5,6],
    'j3' : [7,8,9]
    }

class Jogador:
    def __init__(self, cartas):
        self.cartas_mao = cartas



prefixo = 'j'
numero = 0

print(jogadores['j1'])

# for i in range(1,4):
#     numerojogador = prefixo + str(i)
#     cartas = Jogador(jogadores[numerojogador])
#     print(cartas.cartas_mao)
