# Author: Kelsey Schmidt
# Date: 5-20-21
# Description:  # Creates a class called OrthokonBoard that represents the board
                # for a two-player game that is played on a 4x4 grid.
                # This class does not do everything needed to play a game
                # - it's just responsible for handling the rules concerning the game board.
                # The board starts with four red pieces on row 0 and four yellow pieces on row 3.
                # A valid move consists of a player moving one of their pieces orthogonally or diagonally
                # as far as it can go until it hits another piece or the edge of the board
                # (it must move at least one space).
                # After the piece stops, any opponent pieces on orthogonally adjacent squares
                # are flipped over to its color.
                # The OrthokonBoard class doesn't keep track of whose turn it is,
                # so it will allow multiple moves by the same player consecutively.
                # A player wins upon making a move that either flips over
                # the remaining opponent pieces or leaves the opponent without a move.

class OrthokonBoard:
    """
    Creates a class called OrthokonBoard that represents the board
    for a two-player game that is played on a 4x4 grid.
    This class does not do everything needed to play a game
    - it's just responsible for handling the rules concerning the game board.
    The board starts with four Red pieces (R) on row 0 and four Yellow pieces (Y) on row 3.
    A valid move consists of a player moving one of their pieces orthogonally or diagonally
    as far as it can go until it hits another piece or the edge of the board
    (it must move at least one space).
    After the piece stops, any opponent pieces on orthogonally adjacent squares
    are flipped over to its color.
    The OrthokonBoard class doesn't keep track of whose turn it is,
    so it will allow multiple moves by the same player consecutively.
    A player wins upon making a move that either flips over
    the remaining opponent pieces or leaves the opponent without a move.
    The class has private data members for:
            1. A representation of the board (4 lists within a list)
            2. The current state, which holds one of the three following values:
                "RED_WON", "YELLOW_WON", or "UNFINISHED"
            3. A list that holds the current valid moves for the selected piece (in tuples)
    The class includes the following methods:
        1. An init method that takes no parameters and initializes all data members.
        2. A method named print_board that prints out the board.
            (Does not return anything, print function is within the method)
        3. A get method named get_current_state, which returns the current state.
        4. A method named valid_moves that checks for available valid moves for a selected piece.
            Takes two parameters (in the specific order listed):
                A. The row of the piece being moved
                B. The column of the piece being moved
        5. A method called who_won that checks if anyone has won
        6. A method named make_move that takes four parameters (in the specific order listed):
                A. The row of the piece being moved
                B. The column of the piece being moved
                C. The row of the intended position that piece will be moved to
                D. The column f the intended position that piece will be moved to

        Rows are numbered from top to bottom (0, 1, 2, 3),
        Columns are numbered from left to right (0, 1, 2, 3)
        If the game has already been won, or if the move is not valid, make_move will return False.
        Otherwise, it will record the move, update the board,
        update the current state if the move caused a win, and return True.
    """

    def __init__(self):
        self._board = [["R","R","R","R"],[".",".",".","."],[".",".",".","."],["Y","Y","Y","Y"]]     # inital game board
        self._current_state = "UNFINISHED"  # the default state of the game with no moves made is "UNFINISHED"
        self._valid_moves = []      # empty list to hold valid moves of selected piece

    def get_current_state(self):        # get method to get the current game state
        return self._current_state      # returns "RED_WON", "YELLOW_WON", or "UNFINISHED"

    def print_board(self):              # prints the board in a pretty fashion
        print("_" * 11)
        for line in self._board:
            print("|", *line[:], "|")
        print("‾" * 11)

    def valid_moves(self, piece_row, piece_column): # checks for valid moves for selected piece

        self._valid_moves = []      # empties the valid moves list at start of call
        row_int = ""  # records relevant integers to be a row_int value
        column_int = ""             # records relevant integers to be a column_int value

        for int in range(piece_column + 1):  # check to the left of piece for valid move in that direction
            if piece_column == 0:
                break
            if int == 0:
                continue
            if self._board[piece_row][piece_column - int] == ".":
                column_int = piece_column - int
                continue
            else:
                break
        if column_int != "":
            self._valid_moves.append((piece_row, column_int))
            column_int = ""

        for int in range(4 - piece_column):  # check to the right of piece for valid move in that direction
            if piece_column == 3:
                break
            if int == 0:
                continue
            if self._board[piece_row][piece_column + int] == ".":
                column_int = piece_column + int
                continue
            else:
                break
        if column_int != "":
            self._valid_moves.append((piece_row, column_int))
            column_int = ""

        for int in range(piece_row + 1):  # check upwards of piece for valid move in that direction
            if piece_row == 0:
                break
            if int == 0:
                continue
            if self._board[piece_row - int][piece_column] == ".":
                row_int = piece_row - int
                continue
            else:
                break
        if row_int != "":
            self._valid_moves.append((row_int, piece_column))
            row_int = ""

        for int in range(4 - piece_row):  # check downwards of piece for valid move in that direction
            if piece_row == 3:
                break
            if int == 0:
                continue
            if self._board[piece_row + int][piece_column] == ".":
                row_int = piece_row + int
                continue
            else:
                break
        if row_int != "":
            self._valid_moves.append((row_int, piece_column))
            row_int = ""

        for int in range(4):  # check diag-up-left of piece for valid move in that direction
            if piece_row == 0:
                break
            if piece_column == 0:
                break
            if int == 0:
                continue
            if (int == 1) and ((piece_row == 1) or (piece_column == 1)):
                if self._board[piece_row - int][piece_column - int] == ".":
                    row_int = piece_row - int
                    column_int = piece_column - int
                    break
                else:
                    break
            if (int == 2) and ((piece_row == 2 or 3) and (piece_column == 2 or 3)):
                for int in range(3):
                    if int == 0:
                        continue
                    if self._board[piece_row - int][piece_column - int] == ".":
                        row_int = piece_row - int
                        column_int = piece_column - int
                        continue
                    else:
                        break
            if (int == 3) and ((piece_row == 3) and (piece_column == 3)):
                for int in range(4):
                    if int == 0:
                        continue
                    if self._board[piece_row - int][piece_column - int] == ".":
                        row_int = piece_row - int
                        column_int = piece_column - int
                        continue
                    else:
                        break
        if (row_int and column_int) != "":
            self._valid_moves.append((row_int, column_int))
            row_int = ""
            column_int = ""

        for int in range(4):  # check diag-down-right of piece for valid move in that direction
            if piece_row == 3:
                break
            if piece_column == 3:
                break
            if int == 0:
                continue
            if (int == 1) and ((piece_row == 2) or (piece_column == 2)):
                if self._board[piece_row + int][piece_column + int] == ".":
                    row_int = piece_row + int
                    column_int = piece_column + int
                    break
                else:
                    break
            if (int == 2) and ((piece_row == 0 or 1) and (piece_column == 0 or 1)):
                for int in range(3):
                    if int == 0:
                        continue
                    if self._board[piece_row + int][piece_column + int] == ".":
                        row_int = piece_row + int
                        column_int = piece_column + int
                        continue
                    else:
                        break
            if (int == 3) and ((piece_row == 0) and (piece_column == 0)):
                for int in range(4):
                    if int == 0:
                        continue
                    if self._board[piece_row + int][piece_column + int] == ".":
                        row_int = piece_row + int
                        column_int = piece_column + int
                        continue
                    else:
                        break
        if (row_int and column_int) != "":
            self._valid_moves.append((row_int, column_int))
            row_int = ""
            column_int = ""

        for int in range(4):  # check diag-down-left of piece for valid move in that direction
            if piece_row == 3:
                break
            if piece_column == 0:
                break
            if int == 0:
                continue
            if (int == 1) and ((piece_row == 2) or (piece_column == 1)):
                if self._board[piece_row + int][piece_column - int] == ".":
                    row_int = piece_row + int
                    column_int = piece_column - int
                    break
                else:
                    break
            if (int == 2) and ((piece_row == 1) or (piece_column == 2)):
                for int in range(3):
                    if int == 0:
                        continue
                    if self._board[piece_row + int][piece_column - int] == ".":
                        row_int = piece_row + int
                        column_int = piece_column - int
                        continue
                    else:
                        break
            if (int == 3) and ((piece_row == 0) and (piece_column == 3)):
                for int in range(4):
                    if int == 0:
                        continue
                    if self._board[piece_row + int][piece_column - int] == ".":
                        row_int = piece_row + int
                        column_int = piece_column - int
                        continue
                    else:
                        break
        if (row_int and column_int) != "":
            self._valid_moves.append((row_int, column_int))
            row_int = ""
            column_int = ""

        for int in range(4):  # check diag-up-right of piece for valid move in that direction
            if piece_row == 0:
                break
            if piece_column == 3:
                break
            if int == 0:
                continue
            if (int == 1) and ((piece_row == 1) or (piece_column == 2)):
                if self._board[piece_row - int][piece_column + int] == ".":
                    row_int = piece_row - int
                    column_int = piece_column + int
                    break
                else:
                    break
            if (int == 2) and ((piece_row == 2) or (piece_column == 1)):
                for int in range(3):
                    if int == 0:
                        continue
                    if self._board[piece_row - int][piece_column + int] == ".":
                        row_int = piece_row - int
                        column_int = piece_column + int
                        continue
                    else:
                        break
            if (int == 3) and ((piece_row == 3) and (piece_column == 0)):
                for int in range(4):
                    if int == 0:
                        continue
                    if self._board[piece_row - int][piece_column + int] == ".":
                        row_int = piece_row - int
                        column_int = piece_column + int
                        continue
                    else:
                        break
        if (row_int and column_int) != "":
            self._valid_moves.append((row_int, column_int))
            row_int = ""
            column_int = ""

    def who_won(self):
        self._valid_moves = []  # clear the valid moves list
        red_list = []  # an empty list to hold the current Red cell values, to check if Red pieces can make moves
        yellow_list = []  # an empty list to hold the current Yellow cell values, to check if Yellow pieces can make moves

        for row in self._board:     # checks to see if all pieces are Yellow, thus Yellow wins
            if "R" not in row:
                continue
            else:
                break
            self._current_state = "YELLOW_WON"
            return True
        for row in self._board:     # checks to see if all pieces are Red, thus Red wins
            if "Y" not in row:
                continue
            else:
                break
            self._current_state = "RED_WON"
            return True

        for row in range(4):                            # adds the current Red and Yellow Cell values to their lists
            for column in range(4):
                if self._board[row][column] == ".":
                    continue
                if self._board[row][column] == "R":
                    red_list.append((row, column))
                elif self._board[row][column] == "Y":
                    yellow_list.append((row, column))

        for tuple in red_list:                      # check if any Red pieces can move
            board.valid_moves(tuple[0], tuple[1])

        if self._valid_moves == []:                 # if no valid moves for any of the red pieces,
            self._current_state = "YELLOW_WON"      # Yellow wins
            return True

        for tuple in yellow_list:                      # check if any Yellow pieces can move
            board.valid_moves(tuple[0], tuple[1])

        if self._valid_moves == []:                 # if no valid moves for any of the yellow pieces,
            self._current_state = "RED_WON"      # Red wins
            return True

        return True

    def make_move(self, piece_row, piece_column, position_row, position_column):   # Actually moves the piece, if valid

        if self._current_state != "UNFINISHED":     # if the game state is anything but "UNFINISHED"
            return False                            # returns False, as the current game is already over

        if (piece_row or piece_column or position_row or position_column) not in range(0,4):
                                            # if any of the piece or position values are not 0-3 (not valid positions)
            return False                    # returns False, and a new valid move must be made

        if self._board[piece_row][piece_column] == "." :    # if no piece at intended piece position,
            return False                                    # returns False, and a new valid move must be made

        board.valid_moves(piece_row, piece_column)      # calls valid_moves function, which updates the
                                                        # valid_moves list

        if (position_row, position_column) not in self._valid_moves:  # check intended move against valid_moves
            return False

        if self._board[piece_row][piece_column] == "Y":         # Flips the pieces next to moving Y piece, if applicable
            self._board[position_row][position_column] = "Y"
            self._board[piece_row][piece_column] = "."
            if position_column > 0:  # check left for piece to change
                if self._board[position_row][position_column - 1] != ".":
                    self._board[position_row][position_column - 1] = "Y"
            if position_column < 3:  # check right for piece to change
                if self._board[position_row][position_column + 1] != ".":
                    self._board[position_row][position_column + 1] = "Y"
            if position_row > 0:  # check up for piece to change
                if self._board[position_row - 1][position_column] != ".":
                    self._board[position_row - 1][position_column] = "Y"
            if position_row < 3:  # check down for piece to change
                if self._board[position_row + 1][position_column] != ".":
                    self._board[position_row + 1][position_column] = "Y"
        if self._board[piece_row][piece_column] == "R":         # Flips the pieces next to moving R piece, if applicable
            self._board[position_row][position_column] = "R"
            self._board[piece_row][piece_column] = "."
            if position_column > 0:  # check left for piece to change
                if self._board[position_row][position_column - 1] != ".":
                    self._board[position_row][position_column - 1] = "R"
            if position_column < 3:  # check right for piece to change
                if self._board[position_row][position_column + 1] != ".":
                    self._board[position_row][position_column + 1] = "R"
            if position_row > 0:  # check up for piece to change
                if self._board[position_row - 1][position_column] != ".":
                    self._board[position_row - 1][position_column] = "R"
            if position_row < 3:  # check down for piece to change
                if self._board[position_row + 1][position_column] != ".":
                    self._board[position_row + 1][position_column] = "R"

        board.who_won()     # calls who_won to see if any winning conditions have been met


board = OrthokonBoard()
board.print_board()

board.make_move(3,2,1,2)
board.print_board()
print(board.get_current_state())



