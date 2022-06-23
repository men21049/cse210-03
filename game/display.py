class Display:
    """This class is in charge of printing the different interactions with the player
    """

    def __init__(self):
        """This method instantiate the object
        """
        self.parachute = ['----', '/____\\',
                          '\\    /', '\\  /', ' o', ' /|\\', ' / \\', ' ^^^^^^^']

    def _print_parachute(self, exclude_line=0):
        """This method prints on screen the initial parachute and the parachute as the game progress

        Args:
            exclude_line (int, optional): number of lines we are not to print. Defaults to 0.

        """
        new_char = []
        if exclude_line == 4:
            """ exclude_line == 5 because 4 is the max num of guess"""
            self.parachute[4] = ' x'

        for item in range(exclude_line, len(self.parachute)):
            character_to_print = self.parachute[item]
            new_char = character_to_print.center(11)
            print(new_char)

    def _print_word(self, word):
        """print the word as the game goes along

        Args:
            word (string): word in the format x_x_x_x
        """
        print(word)
