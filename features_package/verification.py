# verificar vitória


def verificar_vitoria(tabuleiro, jogador):
    # Linhas
    for linha in tabuleiro:
        if linha[0] == jogador and linha[2] == jogador and linha[4] == jogador:
            return True

    # Colunas
    for col in [0, 2, 4]:
        if tabuleiro[0][col] == jogador and tabuleiro[1][col] == jogador and tabuleiro[2][col] == jogador:
            return True

    # Diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][2] == jogador and tabuleiro[2][4] == jogador:
        return True

    if tabuleiro[0][4] == jogador and tabuleiro[1][2] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False
