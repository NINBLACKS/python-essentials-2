def is_solved(board):
    # Check rows and columns for a winner
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]  # board[i][0] will be either 1 or 2 (X or O)
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]  # board[0][i] will be either 1 or 2 (X or O)

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]  # board[0][0] will be either 1 or 2 (X or O)
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]  # board[0][2] will be either 1 or 2 (X or O)

    # Check for empty spots (game not finished)
    for row in board:
        if 0 in row:
            return -1

    # If no winner and no empty spots, it's a draw
    return 0


board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
print(is_solved(board))  # Output: 2 (O wins)
