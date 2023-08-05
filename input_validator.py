from colorama import Fore, Back, Style


class InputValidator:

    @staticmethod
    def validate_player_name(player_name):
        if player_name.isalpha() and len(player_name) > 1:
            return True
        else:
            print(Fore.BLACK + Back.LIGHTRED_EX + "Please enter a real name." + Style.RESET_ALL)
            return False

    @staticmethod
    def validate_player_symbol(player_symbol, players_symbols):
        if player_symbol in players_symbols:
            print(Fore.BLACK + Back.LIGHTRED_EX +
                  "Please enter an alphabet different to what the first player has entered." + Style.RESET_ALL)
            return False
        elif len(player_symbol) != 1:
            print(Fore.BLACK + Back.LIGHTRED_EX + "Please enter a single alphabet" + Style.RESET_ALL)
            return False
        elif not player_symbol.isalpha():
            print(Fore.BLACK + Back.LIGHTRED_EX + "Please enter an alphabet" + Style.RESET_ALL)
            return False
        else:
            return True

    @staticmethod
    def validate_if_is_a_single_digit_number(inputted_position):
        if len(inputted_position) != 1:
            print(Fore.BLACK + Back.LIGHTRED_EX + "OOpS!!. Please enter a single digit.." + Style.RESET_ALL)
            return False
        elif not inputted_position.isnumeric():
            print(Fore.BLACK + Back.LIGHTRED_EX + "OOpS!!. Please enter a number.." + Style.RESET_ALL)
            return False
        else:
            return True

    @staticmethod
    def validate_if_digit_is_within_1and9(inputted_position):
        if 0 < int(inputted_position) < 10:
            return True
        else:
            print(Fore.BLACK + Back.LIGHTRED_EX +
                  "Please choose only numbers within 1 and 9 that are available." + Style.RESET_ALL)
            return False

    @staticmethod
    def validate_position_is_available(selected_position, taken_positions):
        if selected_position in taken_positions:
            print(Fore.BLACK + Back.LIGHTRED_EX +
                  "This position has been taken. Please choose the available." + Style.RESET_ALL)
            return False
        else:
            return True
