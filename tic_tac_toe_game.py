from tictactoeboard import TicTacToeBoard
from input_validator import InputValidator
from player import Player
from colorama import Fore, Back, Style
from result_analyzer import ResultAnalyzer


class TicTacToeGame:
    def __init__(self):
        self._board = TicTacToeBoard()
        self._player_one = Player()
        self._player_two = Player()
        self._players_symbols = []

    def play(self):
        self._setup_game()
        self._take_players_moves()

    def _setup_game(self):
        welcome = "Hello! Welcome, have fun Playing Tic Tac Toe"
        print(welcome)
        self._register_players()
        self._give_game_hint()

    def _register_players(self):
        for count_of_players_to_register in range(1, 3):
            player_name = self._set_player_name(count_of_players_to_register)
            player_symbol = self._set_player_symbol(count_of_players_to_register)
            self._players_symbols.append(player_symbol)
            if count_of_players_to_register == 1:
                self._player_one.set_name(player_name)
                self._player_one.set_symbol(player_symbol)
            else:
                self._player_two.set_name(player_name)
                self._player_two.set_symbol(player_symbol)

    @staticmethod
    def _set_player_name(player_number):
        inputted_name_is_not_valid = True
        while inputted_name_is_not_valid:
            player_inputted_name = input(f"Player {player_number} please enter your name: ")
            name_validated = InputValidator.validate_player_name(player_inputted_name)
            if name_validated:
                return player_inputted_name.title()

    def _set_player_symbol(self, player_number):
        inputted_symbol_is_not_valid = True
        while inputted_symbol_is_not_valid:
            player_symbol = input(f"Player {player_number} please choose your symbol: ").upper()
            symbol_validated = InputValidator.validate_player_symbol(player_symbol.upper(), self._players_symbols)
            if symbol_validated:
                return player_symbol.upper()

    def _give_game_hint(self):
        print(Fore.BLACK + Back.LIGHTWHITE_EX + f"\nHere is the board {self._player_one.get_name()} and {self._player_two.get_name()}. "
              f"\nThe boxes are labeled "
              "1 to 9 \nStarting from the first row down to the last "
              "\nYou choose any of the numbers to take such position on the board. GOOD LUCK!\n" + Style.RESET_ALL)
        self._board.display()

    def _take_players_moves(self):
        for moves in range(1, 10):
            if moves > 4:
                self._check_for_winner()
            if moves % 2 == 1:
                self._take_move_of(self._player_one)
            else:
                self._take_move_of(self._player_two)
            self._board.display()
        print(Fore.BLACK + Back.LIGHTWHITE_EX + "This game was a draw." + Style.RESET_ALL)
        self._play_another_round()

    def _take_move_of(self, given_player):
        while True:
            selected_position = given_player.make_a_move()
            position_is_available = (InputValidator
                                     .validate_position_is_available
                                     (selected_position, self._board.get_taken_positions()))
            if position_is_available:
                self._board.record_player_move(selected_position, given_player.get_board_symbol())
                self._board.add_to_taken_positions(selected_position)
                return selected_position

    def _play_another_round(self):
        response = input("Press Y if you wish to play another round or N to exit: ")
        if response.upper() == "Y":
            self._setup_game_again()
        elif response.upper() == "N":
            print(Fore.BLACK + Back.YELLOW + "BYE! HOPE YOU HAD FUN? STAY SAFE " + Style.RESET_ALL)
            exit()
        else:
            print(Fore.BLACK + Back.LIGHTRED_EX + "Please select a required input: " + Style.RESET_ALL)
            self._play_another_round()

    def _setup_game_again(self):
        self._board.reset_board()
        self._board.reset_taken_moves()
        print("*** Let the game begin ***")
        self._board.display()
        self._take_players_moves()

    def _check_for_winner(self):
        self._analyzer = ResultAnalyzer()
        winner = self._analyzer.analyze_board(self._player_one, self._player_two, self._board)
        if winner is not None:
            self._announce(winner)

    def _announce(self, given_player):
        print(Fore.BLACK + Back.LIGHTGREEN_EX + f"***** {given_player.get_name()} "
                                                f"won this round of game *****" + Style.RESET_ALL)
        self._play_another_round()
