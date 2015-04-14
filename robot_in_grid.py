"""
On a rectangular grid (M,N), compute the number of ways a little robot can
go from the bottom left to the upper right corner of the grid if the only
moves allowed are up and right.
+ obstacles [(x1, y1), (x2, y2)]

This solution assumes the grid is provided from top to bottom. That is, the
bottom left is given by (0, M).
You could perhaps simplify it a bit by reversing the 2D array such that the
bottom left is (0,0) and the top right is (M, N).
"""

M = 0
N = 1
class TraverseGrid(object):
    def __init__(self, grid, obstacles=None):
        self.solutions = {}
        self.grid = grid
        self.obstacles = obstacles

        self.M = len(self.grid)
        self.N = len(self.grid[0])

    def get_solutions(self, pos):
        if pos in self.solutions:
            return self.solutions[pos]

        self.solutions[pos] = 0

        # move right
        new_pos = (pos[M] + 1, pos[N])
        if self.is_valid_pos(new_pos):
            self.solutions[pos] += self.get_solutions(new_pos)

        # move up
        new_pos = (pos[M], pos[N] - 1)
        if self.is_valid_pos(new_pos):
            self.solutions[pos] += self.get_solutions(new_pos)

        if self.is_grid_end(pos) and self.is_valid_pos(pos):
            self.solutions[pos] += 1

        return self.solutions[pos]


    def is_grid_end(self, pos):
        return pos[M] >= self.M-1 and pos[N] <= 0
        
    def is_valid_pos(self, pos):
        if self.is_obstacle(pos):
            return False
        if pos[M] >= self.M or pos[M] < 0:
            return False
        if pos[N] >= self.N or pos[N] < 0:
            return False

        return True

    def is_obstacle(self, pos):
        return self.obstacles and pos in self.obstacles

test_grid = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Should print 0
print TraverseGrid(test_grid, {(2, 0)}).get_solutions((0, len(test_grid)-1))

# Should print 5
print TraverseGrid(test_grid, {(0, 0)}).get_solutions((0, len(test_grid)-1))

# Should print 2
print TraverseGrid(test_grid, {(1, 1)}).get_solutions((0, len(test_grid)-1))

# Should print 6
print TraverseGrid(test_grid).get_solutions((0, len(test_grid)-1))
