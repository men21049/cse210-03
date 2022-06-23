from copyreg import dispatch_table
from game.display import Display
from game.player import Player
from game.words import Words


class Jumper:
    """ The Game of jumper, this class controls the game
    """

    def __init__(self):
        """Construct a new Jumper
        """
        self._display = Display()
        self._player = Player()
        self._wordClass = Words()
        self._picked_word = ""
        self._counter = 0
        self._letter = ""
        self._letters = []
        self._keep_playing = True
        self._exclude_line = 0
        self._token = ""
        self._is_admin = False

    def start_game(self):
        self._get_name()
        if self._is_admin:
            self._admin_options()
        self._pick_word()
        print(f"Welcome {self._player._name}\n Let's go ahead and play")
        while self._keep_playing:
            self._get_letter()
            self._display._print_parachute(self._exclude_line)
            self.print_separator()
            self._check_keep_playing()

    def _admin_options(self):
        exit = False
        while not exit:
            pick_option = int(input(
                "Do you want to: \n(1) Add\n(2) Remove\n(3) Print\n(4) Exit Admin mode: "))
            print(str(pick_option))
            if pick_option == 1:
                self._wordClass._add_word()
            elif pick_option == 2:
                self._wordClass._remove_word()
            elif pick_option == 3:
                self._wordClass._print_word_list()
            else:
                exit = True

    def _get_name(self):
        self._player._name = input("Please enter your name: ")
        if self._player._name == self._player._admin:
            self._token = input("please enter token: ")
            if self._token == self._player._token:
                self._is_admin = True

    def _pick_word(self):
        self._picked_word = self._wordClass._pick_word()
        self._counter = self._wordClass._len

    def _get_letter(self):
        self._letter = input("Guess a letter: ")
        is_in = self._wordClass._is_in_word(self._letter)
        if not is_in:
            self._exclude_line += 1
        else:
            self._counter -= 1
        new_word = self._wordClass._return_new_hidden_word(self._letter)
        self._display._print_word(new_word)

    def _check_keep_playing(self):
        if self._exclude_line == 4 or self._counter == 0:
            self._keep_playing = False
            print("Game Over")

    def print_separator(self):
        """Method to print - separator
        """
        print("-"*50)
