class Board:
    """  Class that represents our tic-tac-toe battlefield. """
    def __init__(self):
        self.board = [list("   ") for _ in range(3)]

    def reset_board(self):
        """  Simply reset the board with empty characters. """
        self.board = [list("   ") for _ in range(3)]

    def mark_play(self, symbol, y_pos, x_pos):
        """
        Update board with given indexes and the board's graphical representation with given coordinates.

        Parameters:
            symbol: Character to be used in play marking.
            y_pos, x_pos: Indexes to be used in the actual board list.
        Return:
            Updated Board instance.
        """
        self.board[y_pos][x_pos] = symbol
        return self

    def get_board_state(self):
        """ Board attribute getter. """
        return self.board
