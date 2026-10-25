# J-D Laurence

# Task 6

class TictactoeException (Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

class Board():
    valid_moves=["upper left", "upper center", "upper right",
                  "middle left", "center", "middle right", 
                  "lower left", "lower center", "lower right"]
    
    def __init__ (self):
        self.board_array = [[" "] * 3 for _ in range(3)]
        self.turn = "X"

    # I prefer my own version of __str__ to the supplied one
    def __str__(self):
        top_row = "|".join([x if x != " " else "-" for x in self.board_array[0]])
        mid_row = "|".join([x if x != " " else "-" for x in self.board_array[1]])
        bot_row = "|".join([x if x != " " else "-" for x in self.board_array[2]])
        board_str = "\n".join([top_row, mid_row, bot_row])
        # a one line version is here but maybe less readable
        #board = "\n".join("|".join([x if x != "" else "-" for x in board_array[i]]) for i in range(3))
        return f"\n{board_str} \n"

    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")

# Implementation of the game
board1 = Board()
print("\n------Let's play TicTacToe!-------- \n")
game_is_finished = False
print(board1)
while not game_is_finished:  
    print("Here are the valid moves:")
    print(board1.valid_moves)
    move = input("Enter your move: ")
    try:
        board1.move(move)
    except TictactoeException as e:
        print(e.message)
    print(board1)
    game_is_finished, message = board1.whats_next()
    print(message)


    
        
 


    