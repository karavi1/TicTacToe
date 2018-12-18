class Node:

    def __init__(self, position, grid, val, oppVal):
        self.position = position
        self.grid = grid
        self.val = val
        self.oppVal = oppVal

    def get_position(self):
        return self.position

    def get_utility(self):
        util = 0

        test_grid = self.grid.copy()
        test_grid[self.position] = self.val
        if self.is_win(test_grid, self.val):
            util = float('inf')
            return util

        neighbors = self.get_neighbors()
        for i in neighbors:
            if self.grid[i] == self.val:
                util += 10
            elif self.grid[i] == self.oppVal:
                util += 5
        return util

    def is_win(self, grid, val):
        b = grid
        return (b[0] == b[4] == b[8] == self.val \
                or b[2] == b[4] == b[6] == self.val \
                or b[0] == b[1] == b[2] == self.val \
                or b[3] == b[4] == b[5] == self.val \
                or b[6] == b[7] == b[8] == self.val \
                or b[0] == b[3] == b[6] == self.val \
                or b[1] == b[4] == b[7] == self.val \
                or b[2] == b[5] == b[8] == self.val)

    def is_terminal(self):
        return self.is_win(self.val) or self.is_win(self.oppVal) or self.grid.count(None) == 0

    def get_neighbors(self):
        if self.position == 0:
            return [1, 3]
        elif self.position == 1:
            return [0, 2, 4]
        elif self.position == 2:
            return [2, 5]
        elif self.position == 3:
            return [0, 4, 6]
        elif self.position == 4:
            return [1, 3, 5, 7]
        elif self.position == 5:
            return [2, 4, 8]
        elif self.position == 6:
            return [3, 7]
        elif self.position == 7:
            return [4, 6, 8]
        elif self.position == 8:
            return [5, 7]
