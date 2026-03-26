# entrada dos jogadores

def pedir_jogada(jogador):
    while True:
        jogada = input(f'Jogador {jogador}, escolha posição (1-9): ').upper()

        if jogada in [str(i) for i in range(1, 10)]:
            return jogada

        print('Entrada inválida!')
