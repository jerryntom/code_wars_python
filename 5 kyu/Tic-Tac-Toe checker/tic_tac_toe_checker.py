def check_win_diagonals(symbol, board):
    is_checked = True

    for i in range(0, len(board)):
        if board[i][i] != symbol:
            is_checked = False
            break

    if is_checked is True:
        return True

    is_checked = True

    for i in range(len(board) - 1, -1, -1):
        if board[i][i] != symbol:
            is_checked = False
            break

    return is_checked


def check_win_rows(symbol, board):
    for i in range(0, len(board)):
        is_checked = True

        for j in range(0, len(board)):
            if board[i][j] != symbol:
                is_checked = False
                break

        if is_checked:
            return True

    return False


def check_win_cols(symbol, board):
    for i in range(0, len(board)):
        is_checked = True

        for j in range(0, len(board)):
            if board[j][i] != symbol:
                is_checked = False
                break

        if is_checked:
            return True

    return False


def check_finished(board):
    for row in board:
        for symbol in row:
            if symbol == 0:
                return False

    return True


def is_solved(board):
    if check_win_diagonals(1, board) or check_win_rows(1, board) or check_win_cols(1, board):
        return 1
    elif check_win_diagonals(2, board) or check_win_rows(2, board) or check_win_cols(2, board):
        return 2

    if check_finished(board):
        return 0
    else:
        return -1
