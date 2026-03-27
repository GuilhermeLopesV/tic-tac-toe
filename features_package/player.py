def request_a_play(player):
    while True:
        """
        Requests a valid move from the player.
        """
        play = input(f'Jogador {player}, escolha posição (1-9): ').upper()

        if play in '123456789':
            return play

        print('Entrada inválida!')
