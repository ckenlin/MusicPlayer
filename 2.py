"""
tictactoe.py
An interactive game in Python
Created by Philo van Kemenade
"""

import random

class TicTacToe(object):
    """A game of Tic Tac Toe"""
    def __init__(self):
        self.playing = True
        self.board = Board()
        self.turn = self.whoStarts()
    
    # start the game
    def start(self):
        """Loop game dynamics until game has ended, print result, play again?"""
        print ("\nWelcome to Tic Tac Toe")
        # init resets the board
        self.__init__()
        while self.playing:
            self.board.show_board()
            raw_move = self.get_player_input()
            print ("\n")
            # parse and check move validity of move
            move = self.parse_move(raw_move)
            if move:
                [row, col] = move
                self.board.mark_move(row, col, self.get_turn())
                self.evaluate()
                self.switch_turn()
            else:
                print ("That's not a valid move, please try again")
                continue
        
        self.board.show_board()
        print (self.result)
        if self.play_again():
            self.start()
    
        
    def whoStarts(self):
        """pick random player X or O to start"""
        if random.randint(0,1) == 0:
            return "X"
        else:
            return "O"
    
    def get_turn(self):
        """get current player"""
        return self.turn
    
    def switch_turn(self):
        """switch current player"""
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    def get_player_input(self):
        """get player's input"""
        print ("Current player: "), self.get_turn()
        return raw_input("Please input your move: [row], [column]\n")
    
    def evaluate(self):
        """check if game has ended"""
        ## check for three in a row
        # check horizontal rows
        for row in self.board.cells:
            if self.lineOf3(row):
                self.playing = False
                self.setWinner()
        # check vertical columns
        for i in range(3):
            col = [row[i] for row in self.board.cells]
            if self.lineOf3(col):
                self.playing = False
                self.setWinner()
        # check diagonal
        diag1 = [self.board.cells[i][i] for i in [0,1,2]]
        diag2 = [self.board.cells[i][2-i] for i in [0,1,2]]
        if self.lineOf3(diag1):
            self.playing = False
            self.setWinner()
        if self.lineOf3(diag2):
            self.playing = False
            self.setWinner()
        
        ## check check for full board
        if self.board.is_full():
            self.playing = False
            self.setDraw()
    
    def setWinner(self):
        """set result to reflect current winner"""
        self.result = "*** player " + self.turn + " has won the game! ***"
    
    def setDraw(self):
        """set result to reflect draw"""
        self.result = "*** That's a draw... ***"
    
    def lineOf3(self, cellList):
        '''check if 3 elements cause winner'''
        # check if first element is non-empty
        if cellList[0] != " ":
            # check is all elements in cellList are equal
            if cellList.count(cellList[0]) == len(cellList):
                # return sign
                return True
            else:
                return False
        else:
            return False
    
    def parse_move(self, move):
        """check whether move is valid and parse row and column"""
        try:
            posList = move.split(",", 2)
            [row, col]  = [int(posList[0]), int(posList[1])]
        except:
            print ("please specify two integer coordinates as [row], [column]")
            return None
        if self.valid_move(row, col):
            return [row, col]            
        else:
            return None
    
    def valid_move(self, row, col):
        """check if move to (row, col) is valid"""
        # check if position coords are on board
        if not self.board.is_move_on_board(row, col):
            print ("that position is not on the board")
            return False
        # check whether position is free
        elif not self.board.is_cell_free(row, col):
            print ("that position is not empty")
            return False
        else:
            return True
    
    def play_again(self):
        """ask and return whether player wants another game"""
        again = raw_input("Would you like to play again? [y(es) / n(o)]\n")
        return again.lower().startswith('y')
    
class Board:
    def __init__(self):
        """initialise board with cells"""
        self.cells = self.make_cells() 
    
    def make_cells(self):
        """make empty cells of tictactoe board
        return 1 list of 3 rows
        where each row is a list of 3 "spaces" to represent empty cells
        """
        return [[" ", " ", " "],
                [" ", " ", " "], 
                [" ", " ", " "]]
    
    def show_board(self):
        """ print current board to screen in a fancy way"""
        # get rows from cells
        row1 = self.cells[0]
        row2 = self.cells[1]
        row3 = self.cells[2]
        
        # print first row
        print (row1[0] + "|" + row1[1] + "|" + row1[2])
        
        # print horizontal line
        print "-----"
        
        # print second row
        print (row2[0] + "|" + row2[1] + "|" + row2[2])
        
        # print horizontal line
        print "-----"
        
        # print third row    
        print (row3[0] + "|" + row3[1] + "|" + row3[2])
    
    def mark_move(self, row, col, sign):
        """mark move (row, col) of sign on board"""
        self.cells[row][col] = sign
    
    def is_move_on_board(self, row, col):
        """check if move is within board coordinates"""
        if row in [0,1,2] and col in [0,1,2]:
            return True
        else:
            return False
    
    def is_cell_free(self, row, col):
        """Return True if cell is empty, otherwise return False """
        if self.cells[row][col] == " ":
            return True
        else:
            return False
    
    def is_full(self):
        """Return False if any cell is empty, return True otherwise"""
        for row in range(3):
            for col in range(3):
                if self.is_cell_free(row, col):
                    return False
        return True
    
def main():
    myGame = TicTacToe()
    myGame.start()

if __name__ == '__main__':
  main()
