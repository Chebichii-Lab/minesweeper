# we are going to use RECURSION and CLASSES for this game

class Board:
    def __init__(self, dim_size, num_bombs):
        # lets keep track of these parameters.
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function:
        self.board = self.make_new_board() # plant the bombs

        # initialize a set to keep track of which locations we've uncovered
        # we'll save(row, col) tuples into this set
        self.dug = set()

# goal of this function is to play the game
def play(dim_size = 10, num_bombs = 10):
    # Step 1: create the board and plant bombs
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #           next to a bomb
    # Step 4: repeat steps 2 and 3 unti;; there are no more places to dig -> VICTORY!
    pass