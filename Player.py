class Player:

    def __init__(self, b, v):
        self.board = b
        self.val = v

    def play(self):
        position = int(input("What position would you like to play? "))
        while self.board[position] is not None:
            position = int(input("Invalid Position. What position would you like to play? "))
        self.board[position] = self.val



