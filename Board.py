class Board():

    def __init__(self):
        self.board = [None] * 9

    def visualize(self):

        board = self.board
        for i in range(len(board)):
            if board[i] is None:
                board[i] = " "
        print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))
        print("-----")
        print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
        print("-----")
        print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))

    def position_visualize(self):
        updated = [None] * 9
        for i in range(9):
            if self.board[i] == "X" or self.board[i] == "O":
                updated[i] = self.board[i]
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

b = Board()
b.test()


