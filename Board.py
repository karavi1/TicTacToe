class Board:

    def __init__(self):
        self.grid = [None] * 9

    def visualize(self):
        board = self.grid
        for i in range(len(board)):
            if board[i] is None:
                board[i] = " "
        print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))
        print("-----")
        print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
        print("-----")
        print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))
        for i in range(len(board)):
            if board[i] is " ":
                board[i] = None

    def position_visualize(self):
        updated = [None] * 9
        for i in range(9):
            if self.grid[i] == "X" or self.grid[i] == "O":
                updated[i] = self.grid[i]
            else:
                updated[i] = i
        board = updated
        print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))
        print("-----")
        print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
        print("-----")
        print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))

    def test(self):
        test = Board()
        test.visualize()
        test.position_visualize()
