"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    xCount = 0
    oCount = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            pos = board[row][col]
            if not pos:
                continue
            if pos == X:
                xCount +=1
            if pos == O:
                oCount +=1
    return  X if xCount == oCount else O
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    allActions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                allActions.append([row,col])
    return allActions
    """
    use for ai to choose
    Returns set of all possible actions (i, j) available on the board.
    """


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
            return boardcopy
    except IndexError:
        print("Spot already occupied")


def winner(board):
    for row in board:
        xcounter = row.count(X)
        ocounter = row.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O

    columns = []

    for j in range(len(board)):
        column = [row[j] for row in board]
        columns.append(column)

    for col in columns:
        xcounter = col.count(X)
        ocounter = col.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O
     #checks diagonally
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    #checks tie
    return None
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    return winner(board) is not None
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    current_player = player(board)
    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k =maxValue(result(board,action))
            if k > v:
                v = k
                best_action = action
    else:
        v = math.inf
        for action in actions(board):
            k =minValue(result(board,action))
            if k < v:
                v = k
                best_action = action
    return best_action

    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board,action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board,action)))
    return v