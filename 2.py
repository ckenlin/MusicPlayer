# Tic Tac Toe

import streamlit as st

import random

# 列印方法
def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    st.write('   |   |')
    st.write(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    st.write('   |   |')
    st.write('-----------')
    st.write('   |   |')
    st.write(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    st.write('   |   |')
    st.write('-----------')
    st.write('   |   |')
    st.write(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    st.write('   |   |')

#letter = st.sidebar.text_input('please input X or O?' , 'X O')

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        st.write('Do you want to be X or O?')
        #letter = st.sider.text_input('please input X or O?' , 'X O')
        letter = st.sidebar.text_input('please input X or O?' , 'X O')
        letter = letter.upper()
    
    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    st.write('Do you want to play again? (yes or no)')
    return st.sider.text_input.lower().startswith('y')

# 下子
def makeMove(board, letter, move):
    board[move] = letter

# 判斷遊戲是否結束
def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

def getBoardCopy(board):
    # 複製一份棋盤，供電腦落子時使用
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # 判斷這個位置是否有子，沒子返回True
    return board[move] == ' '

move = st.sidebar.text_input

def getPlayerMove(board):
    # 玩家落子
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        st.write('What is your next move? (1-9)')
        #move = st.sidebar.text_input
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # 隨機返回一個可以落子的座標
    # 如果沒有所給的movesList中沒有可以落子的，返回None
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # 確定電腦的落子位置
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Tic Tac Toe AI核心演算法:
    # 首先判斷電腦方能否通過一次落子直接獲得遊戲勝利
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # 判斷玩家下一次落子能否獲得勝利，如果能，給它堵上
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # 如果角上能落子的話，在角上落子
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 如果能在中心落子的話，在中心落子
    if isSpaceFree(board, 5):
        return 5

    # 在邊上落子
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # 如果棋盤滿了，返回True
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

    st.write('Welcome to Tic Tac Toe!')

while True:
    # 更新棋盤
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    st.write('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # 玩家回合
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                st.write('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    st.write('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # 電腦回合
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                st.write('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    st.write('The game is a tie!')
                    break
                else:
                    turn = 'player'
                    
    if not playAgain():
        break
