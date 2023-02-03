import numpy as np
import sys


class Cell:
    # row and column denote location
    row = 0
    col = 0
    visited = False
    # 4x4 grid to represent this one cell
    # 0 indicates path
    # 1 indicates wall

    def __init__(self, r, c, start = False):
        if start:
            self.local_grid = np.ones((4, 4), dtype=int)
            for i in range(4):
                for j in range(4):
                    if (i == 1 or i == 2) and (j == 1 or j == 2):
                        self.local_grid[i, j] = 0
            self.setPath(1, 0)
            self.setPath(2, 0)
            self.row = 0
            self.col = 0
        else:
            self.local_grid = np.ones((4, 4), dtype=int)
            self.row = r
            self.col = c

    def setEnd(self):
        self.setPath(1, 3)
        self.setPath(2, 3)

    def isPath(self, row, col):
        return self.local_grid[row, col] == 0

    def setPath(self, r, c):
        self.local_grid[r, c] = 0

    def isVisited(self):
        return self.visited

    def Visit(self):
        self.visited = True

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def determineOrientation(self, c):
        # Return documentation
        # 0 = UP
        # 1 = RIGHT
        # 2 = DOWN
        # 3 = LEFT
        # 4 = NOT ADJACENT
        if self.row == c.getRow():
            # Cells are within the same row
            if self.col > c.getCol():
                # Cell c is to the left
                return 3
            elif self.col < c.getCol():
                # Cell c is to the right
                return 1
            else:
                sys.exit("Error: attempt to determine orientation with self. ")
        elif self.col == c.getCol():
            # Cells are within the same column
            if self.row > c.getRow():
                # Cell C is above
                return 0
            elif self.row < c.getRow():
                # Cell C is below
                return 2
        else:
            # Cells are not adjacent
            return 4

    def makePath(self, c):
        # make the center 2x2 of the 4x4 of each cell into space
        for i in range(4):
            for j in range(4):
                if (i == 1 or i == 2) and (j == 1 or j == 2):
                    self.local_grid[i, j] = 0
                    c.local_grid[i, j] = 0
        # make the 4x4 area shared between the cells space
        direction = self.determineOrientation(c)
        if direction == 0:
            # Set top of self and bottom of C to space
            self.setPath(0, 1)
            self.setPath(0, 2)
            c.setPath(3, 1)
            c.setPath(3, 2)
        elif direction == 1:
            # Set right of self and left of C to space
            self.setPath(1, 3)
            self.setPath(2, 3)
            c.setPath(1, 0)
            c.setPath(2, 0)
        elif direction == 2:
            # Set bottom of self and top of C to space
            self.setPath(3, 1)
            self.setPath(3, 2)
            c.setPath(0, 1)
            c.setPath(0, 2)
        elif direction == 3:
            # Set left of self and right of C to space
            self.setPath(1, 0)
            self.setPath(2, 0)
            c.setPath(1, 3)
            c.setPath(2, 3)
        elif direction == 4:
            sys.exit("Error: Attempt to make path between cells that are not adjacent")

    def __repr__(self):
        ret_str = "C[" + str(self.row) + "," + str(self.col) + "]\n"
        for i in range(4):
            for j in range(4):
                ret_str += str(self.local_grid[i, j]) + " "
            ret_str += "\n"
        return ret_str
