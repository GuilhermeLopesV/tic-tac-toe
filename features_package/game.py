from . import utils
from . import player
from . import verification




def create_board():
    """
       Creates an empty game board.
       """
    return [
        [' ', '|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' '],
    ]

def show_board(board):
    """
    Displays the board in the terminal.
    """
    for line in board:
        print("".join(line))


def make_move(board, position, gamester):
    """
        Executes a move on the board.

        Args:
            board (list): Game board
            position (str): Position chosen (1-9)
            player (str): Current player ('X' or 'O')

        Returns:
            bool: True if move is valid, False otherwise
        """

    position_map = {
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

    row, col = position_map[position]

    if board[row][col] != ' ':
        return False

    board[row][col] = gamester
    return True



def game():
    board = create_board()
    current_player = 'X'
    plays = 0

    while True:
        utils.clean_screen()
        show_board(board)

        play = player.request_a_play(current_player)

        if not make_move(board, play, current_player):
            print('Posição já ocupada!')
            input('Pressione ENTER para continuar...')
            continue

        plays += 1

        if verification.verify_victory(board, current_player):
            utils.clean_screen()
            show_board(board)
            print(f'Jogador {current_player} venceu!')
            break

        if plays == 9:
            utils.clean_screen()
            show_board(board)
            print('Empate!')
            break

        # troca jogador
        current_player = 'O' if current_player == 'X' else 'X'