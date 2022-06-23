class Player:
    """Class to define a player on jumper game
    """

    def __init__(self):
        """Method to instantiate player
        """
        self._name = ""
        self._token = "nomemires"
        self._admin = "admin"

    def auth_player(self, player, token):
        """If auth player logs in, the player would be able to add or remove 
           guessing words
        """
        auth = False
        if self._admin == player and self._token == token:
            auth = True

        return auth
