import copy
import time

from board import Board
from ranking import Ranking


class TicTacToeGame:
    def __init__(self):
        self.x_pos = 1
        self.y_pos = 1
        self.played = False
        self.player1 = None
        self.player2 = None
        self.board = Board()
        self.game_over = True
        self.ranking = Ranking()
        self.player_choice = None
        self.current_player = None
        self.start_time = None
        self.end_time = 0
        self.elapsed_time = 0
        self.total_time = 0
        self.board_states = []

    def reset(self):
        """ Reset class attributes in case players wish to play again. """
        self.x_pos = 1
        self.y_pos = 1
        self.played = False
        self.player1 = None
        self.player2 = None
        self.board.reset_board()
        self.game_over = True
        self.board_states = []
        self.player_choice = None
        self.current_player = None
        self.start_time = None
        self.end_time = 0
        self.elapsed_time = 0
        self.total_time = 0

    def input(self, key):
        """ Manage key input operations. """
        if key == "KEY_UP":
            self.y_pos = max(0, self.y_pos - 1)
        elif key == "KEY_DOWN":
            self.y_pos = min(2, self.y_pos + 1)
        elif key == "KEY_LEFT":
            self.x_pos = max(0, self.x_pos - 1)
        elif key == "KEY_RIGHT":
            self.x_pos = min(2, self.x_pos + 1)
        elif key == " ":
            self.play()

    def play(self):
        """  Handle play made from pressing 'spacebar'. Do nothing if spot is already marked. """
        if self.is_empty():
            self.played = True
            self.board.mark_play(self.current_player.symbol, self.y_pos, self.x_pos)
            self.board_states.append(copy.deepcopy(self.board.get_board_state()))
            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time
            self.current_player.update(game_over=False, temp_time=self.elapsed_time)
            self.total_time += self.elapsed_time

            if self.check_win():
                self.game_over = True
                self.current_player.update(temp_time=self.current_player.temp_time, game_over=True, won=True,
                                           keep_time=True)
                other_player = next(self.player_choice)
                other_player.update(temp_time=other_player.temp_time, game_over=True, won=False)
                self.ranking.update(self.current_player, other_player)

            elif self.check_tie():
                self.game_over = True

            self.current_player = next(self.player_choice)
            self.start_time = time.time()

        # TODO:
            # if self.game_over:
            #     if self.play_again(row):
            #         self.reset()
            #     else:
            #         self.stop()

    def is_empty(self):
        return self.board.get_character(self.y_pos, self.x_pos) == ' '

    def check_win(self):
        """
        Verify if the current game state resulted in a win.
        This is called after every play, so the winner is always the current player.

        Return:
            Boolean True if current play resulted in a win, False if not.
        """

        def all_same(symbol_list):
            """
            Check if all elements of a list are the same.

            Parameters:
                symbol_list: List to check (Duh).
            """
            if symbol_list.count(symbol_list[0]) == len(symbol_list) and symbol_list[0] != " ":
                return True
            return False

        # Check horizontal winner
        for row in self.board.board:
            if all_same(row):
                return True

        # Check vertical winner
        for col in range(3):
            check = []
            for row in self.board.board:
                check.append(row[col])
            if all_same(check):
                return True

        # Check upper-left-to-lower-right diagonal winner
        diags = []
        for ix in range(3):
            diags.append(self.board.board[ix][ix])
        if all_same(diags):
            return True

        # Check lower-left-to-upper-right diagonal winner
        diags = []
        for col, row in enumerate(reversed(range(3))):
            diags.append(self.board.board[row][col])
        if all_same(diags):
            return True

        return False

    def check_tie(self):
        """
        Verify if the current game state resulted in a tie.
        Iterate through the game board and check if it contains a whitespace string,
        if it does, the game is still not over.

        Return:
            is_tie: Boolean True if current game state is a tie, False if not.
        """
        is_tie = True
        for row in self.board.board:
            if " " in row:
                is_tie = False
                break
        return is_tie
