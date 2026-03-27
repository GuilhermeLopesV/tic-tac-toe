def verify_victory(board, player):
    """
    Checks if the given player has won the game.
    """

    # Rows
    for row in board:
        if row[0] == player and row[2] == player and row[4] == player:
            return True

    # Columns
    for col in [0, 2, 4]:
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Diagonals
    if board[0][0] == player and board[1][2] == player and board[2][4] == player:
        return True

    if board[0][4] == player and board[1][2] == player and board[2][0] == player:
        return True

    return False
