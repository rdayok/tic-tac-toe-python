from colorama import Fore, Back, Style


class TicTacToeBoard:
    def __init__(self):
        self._board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self._taken_positions = []

    def display(self):
        print(Fore.BLACK + Back.YELLOW + "-" * 13)
        for row in self._board:
            for element in row:
                print(f"| {element} ", end="")
            print("|\n", end="")
            print("-" * 13)
        print(Style.RESET_ALL)

    def get_updated_board(self):
        return self._board

    def add_to_taken_positions(self, selected_position):
        self._taken_positions.append(selected_position)

    def get_taken_positions(self):
        return self._taken_positions

    def reset_board(self):
        self._board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def reset_taken_moves(self):
        self._taken_positions = []

    def record_player_move(self, selected_position, player_symbol):
        if selected_position == 1:
            self._board[0][0] = player_symbol
        elif selected_position == 2:
            self._board[0][1] = player_symbol
        elif selected_position == 3:
            self._board[0][2] = player_symbol
        elif selected_position == 4:
            self._board[1][0] = player_symbol
        elif selected_position == 5:
            self._board[1][1] = player_symbol
        elif selected_position == 6:
            self._board[1][2] = player_symbol
        elif selected_position == 7:
            self._board[2][0] = player_symbol
        elif selected_position == 8:
            self._board[2][1] = player_symbol
        elif selected_position == 9:
            self._board[2][2] = player_symbol
