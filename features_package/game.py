# lógica do tabuleiro

from . import utils
from . import player
from . import verification




def criar_tabuleiro():
    return [
        [' ', '|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' '],
    ]

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("".join(linha))


def fazer_jogada(tabuleiro, posicao, jogador):
    mapa = {
        '1': (0, 0),
        '2': (0, 2),
        '3': (0, 4),
        '4': (1, 0),
        '5': (1, 2),
        '6': (1, 4),
        '7': (2, 0),
        '8': (2, 2),
        '9': (2, 4),
    }

    linha, coluna = mapa[posicao]

    if tabuleiro[linha][coluna] != ' ':
        return False

    tabuleiro[linha][coluna] = jogador
    return True



def jogo():
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'
    jogadas = 0

    while True:
        utils.limpar_tela()
        mostrar_tabuleiro(tabuleiro)

        jogada = player.pedir_jogada(jogador_atual)

        if not fazer_jogada(tabuleiro, jogada, jogador_atual):
            print('Posição já ocupada!')
            input('Pressione ENTER para continuar...')
            continue

        jogadas += 1

        if verification.verificar_vitoria(tabuleiro, jogador_atual):
            utils.limpar_tela()
            mostrar_tabuleiro(tabuleiro)
            print(f'Jogador {jogador_atual} venceu!')
            break

        if jogadas == 9:
            utils.limpar_tela()
            mostrar_tabuleiro(tabuleiro)
            print('Empate!')
            break

        # troca jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'