import random


class Words:
    """This class sets a min list at the beginining and it allows to authorized users to
       add new words, remove words and to see the list of words one can guess
    """

    def __init__(self):
        """Sets a min list of words to play the game
        """
        self._words = ['almanac', 'dairy', 'twister', 'rectangle']
        self._word = ""
        self._guess_word = ""
        self._len = 0
        self._resp = []

    def _word_length(self):
        """Sets the length of the choosing word
        """
        self._len = len(self._word)
        self._resp = list("_" * self._len)

    def _pick_word(self):
        """Once the game has initiated, this method return a word to guess

        Returns:
            word(string): word to guess
        """
        self._word = random.choice(self._words)
        self._word_length()
        return self._word

    def _is_in_word(self, letter):
        """checks if the letter is in the word

        Args:
            letter (string): a character to check if a letter belongs in the word to guess

        Returns:
            resp(boolean) : return true or false if the letter exists in the word
        """
        resp = False
        if letter in self._word:
            resp = True
        return resp

    def _return_new_hidden_word(self, letter):
        """returns the new guess word

        Args:
            letter (_string_): user input

        Returns:
            _string_: a new word to print in the format ______
        """
        for index, value in enumerate(list(self._word)):
            if letter == value:
                self._resp[index] = value
        return "".join(self._resp)

    def _add_word(self):
        """Only authorized users will be able to add new words
        """
        new_word = input("Please type the new word to add to the list: ")
        self._words.append(new_word)

    def _remove_word(self, word_to_remove):
        """Only authorized users will be able to remove a word from the list

        Args:
            word_to_remove (string): Word to remove from the list

        Returns:
            message(string) : whether the word was successfully removed or not
        """
        message = ""
        if word_to_remove in self._words:
            self._words.remove(word_to_remove)
            message = word_to_remove + " has been removed from the list"
        else:
            message = word_to_remove + " word is not in the list"
        return message

    def _print_word_list(self):
        """Only authorized users will be able to see the entire list of words
        """
        print(self._words)
