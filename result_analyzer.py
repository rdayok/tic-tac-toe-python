
class ResultAnalyzer:
    def __init__(self):
        self._board = None
    
    def analyze_board(self, player_one, player_two, board):
        self._board = board

        if self._is_winner(player_one.get_board_symbol()):
            return player_one
        if self._is_winner(player_two.get_board_symbol()):
            return player_two
        return None

    def _is_winner(self, given_symbol):
        if self._is_same_in_any_row(given_symbol):
            return True
        if self._is_same_in_any_column(given_symbol):
            return True
        if self._is_same_in_positions_1_5_9(given_symbol):
            return True
        if self._is_same_in_positions_3_5_7(given_symbol):
            return True
        
    def _is_same_in_any_row(self, given_symbol):
        for row in self._board.get_updated_board():
            if all(given_symbol == column for column in row):
                return True
        return False

    def _is_same_in_any_column(self, given_symbol):
        for column in range(3):
            if all(given_symbol == self._board.get_updated_board()[row][column]
                   for row in range(3)):
                return True
        return False

    def _is_same_in_positions_1_5_9(self, given_symbol):
        for index in range(3):
            if all(given_symbol == self._board.get_updated_board()[index][index]
                   for index in range(3)):
                return True
        return False

    def _is_same_in_positions_3_5_7(self, given_symbol):
        column = 2
        for row in range(3):
            if given_symbol != self._board.get_updated_board()[row][column]:
                return False
            column -= 1
        return True
