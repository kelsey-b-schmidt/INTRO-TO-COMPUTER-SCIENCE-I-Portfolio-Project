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
            1. a representation of the board (4 lists within a list)
            2. the current state, which holds one of the three following values:
                "RED_WON", "YELLOW_WON", or "UNFINISHED"
    The class includes the following methods:
        1. An init method that takes no parameters,
            initializes the starting board positions,
            and initializes the current state to "UNFINISHED"
        2. A method named print_board that prints out the board.
            (Does not return anything, print function is within the method)
        3. A get method named get_current_state, which returns the current state.
        4. A method named make_move that takes four parameters (in the specific order listed):
                A. The row of the piece being moved
                B. The column of the piece being moved
                C. The row of the intended position that piece will be moved to
                D. The column f the intended position that piece will be moved to
        Rows are numbered from top to bottom (0, 1, 2, 3),
        Columns are numbered from left to right (0, 1, 2, 3)
        If the game has already been won, or if the move is not valid,
        make_move will return False.
        Otherwise, it will record the move, update the board,
        update the current state if the move caused a win, and return True.
    """

    def __init__(self):
        self._board = [["R","R","R","R"],[".",".",".","."],[".",".",".","."],["Y","Y","Y","Y"]]
        self._current_state = "UNFINISHED"  # the default state of the game with no moves made is "UNFINISHED"

    def get_current_state(self):        # get method to get the current game state (Who won?)
        return self._current_state      # returns "RED_WON", "YELLOW_WON", or "UNFINISHED"

    def print_board(self):              # prints the board in a pretty fashion
        print("_" * 11)
        for line in self._board:
            print("|", *line[:], "|")
        print("‾" * 11)

    def make_move(self, piece_row, piece_column, position_row, position_column):    # method to make each move
        if self._current_state != "UNFINISHED":     # if the game state is anything but "UNFINISHED"
            print("The game is already over!")
            return False                            # returns False, as the current game is already over

        if (piece_row or piece_column or position_row or position_column) not in range(0,4):
                                            # if any of the piece or position values are not 0-3 (not valid positions)
            print("Not a valid board position")
            return False                    # returns False, and a new valid move must be made

        if self._board[piece_row][piece_column] == ".":     # if the chosen starting piece position does not
                                                            # have a piece there (".")
            print("There is not a piece there to move!")
            return False                                    # returns False, and a new valid move must be made

        if self._board[position_row][position_column] == "Y" or "R":  # if the chosen position already has a piece there
                                                                        #  ("Y" or "R")
            print("There's already a piece there!")
            return False                                    # returns False, and a new valid move must be made







board = OrthokonBoard()
board.print_board()
board.make_move(3,2,0,2)  # The yellow player moves a piece diagonally, flipping one red piece to yellow
print(board.get_current_state())
