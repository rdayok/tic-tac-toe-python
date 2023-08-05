from colorama import Fore, Back, Style

from input_validator import InputValidator


class Player:
    def __init__(self,):
        self._name = None
        self._player_symbol = None

    def make_a_move(self):
        while True:
            inputted_position = input(f" {self._name} Please choose a position: ")
            it_is_a_single_digit_number = InputValidator.validate_if_is_a_single_digit_number(inputted_position)
            if it_is_a_single_digit_number:
                is_a_digit_within_1and9 = InputValidator.validate_if_digit_is_within_1and9(inputted_position)
                if is_a_digit_within_1and9:
                    return int(inputted_position)

    def get_name(self):
        return self._name

    def set_name(self, new_player_name):
        self._name = new_player_name

    def get_board_symbol(self):
        return self._player_symbol

    def set_symbol(self, new_player_symbol):
        self._player_symbol = new_player_symbol
