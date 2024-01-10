import random

# we are going to use RECURSION and CLASSES for this game

class Board:
    def __init__(self, dim_size, num_bombs):
        # lets keep track of these parameters.
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function:
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save(row, col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0, 0)}

    def make_new_board(self):
        #generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(self.dim_size**2-1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # this meand we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*'  # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                   # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
       self.dug.add((row, col)) # keep track of where we have dug

       if self.board[row][col] == '*':
           return False
       elif self.board[row][col] > 0:
           return True
       
       for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue  # don't dig where you've already dug
                self.dig(r, c)

        return True
           
# goal of this function is to play the game
def play(dim_size = 10, num_bombs = 10):
    # Step 1: create the board and plant bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #           next to a bomb
    # Step 4: repeat steps 2 and 3 unti;; there are no more places to dig -> VICTORY!
    pass

