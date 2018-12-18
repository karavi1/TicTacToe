import Board
import Node

class Player:

    def __init__(self, b, v):
        self.board = b
        self.grid = b.grid
        self.val = v

    def play(self):
        self.board.position_visualize()
        print()
        self.board.visualize()
        position = int(input("What position would you like to play? "))
        while self.grid[position] is not None:
            self.board.position_visualize()
            print()
            self.board.visualize()
            position = int(input("Invalid Position. What position would you like to play? "))
        self.grid[position] = self.val

    def AIplay(self, successors):
        def key_with_max_val(d):
            v = list(d.values())
            k = list(d.keys())
            return k[v.index(max(v))]

        self.board.position_visualize()
        print()
        self.board.visualize()
        utils = {}
        for i in successors:
            position = i.get_position()
            utility = i.get_utility()
            utils[position] = utility

        final_position = key_with_max_val(utils)
        self.grid[final_position] = self.val



def main():
    b = Board.Board()
    p1 = Player(b, 'x')
    p2 = Player(b, 'o')
