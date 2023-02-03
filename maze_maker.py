import numpy as np
import random as rd
from cell import Cell

visited = []


def makeMaze(rows, cols, path_color, wall_color):
    visited.clear()
    print("Generating maze structure...")
    # creates a numpy 2D array of Cells
    array = np.empty((rows, cols), dtype=object)
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                array[i, j] = Cell(i, j, True)
            else:
                array[i, j] = Cell(i, j)

    # starting cell will be top left
    # ending cell will be bottom right
    array[rows-1][cols-1].setEnd()

    # unvisited will be false when the length of list visited is the same length as array
    visited.append((0, 0))
    hits = [False, False, False, False]
    while len(visited) != rows * cols:
        progress = int(100*(len(visited) / (rows * cols)))
        if not hits[0] and progress >= 20:
            print("\t"+str(progress) + "%")
            hits[0] = True
        elif not hits[1] and progress >= 40:
            print("\t"+str(progress) + "%")
            hits[1] = True
        elif not hits[2] and progress >= 60:
            print("\t"+str(progress) + "%")
            hits[2] = True
        elif not hits[3] and progress >= 80:
            print("\t"+str(progress) + "%")
            hits[3] = True

        rd.shuffle(visited)
        next_cell = None
        for i in range(len(visited)):
            # CHECK TOP
            if visited[i][0] != 0:
                cell_above = array[visited[i][0] - 1, visited[i][1]]
                if not cell_above.isVisited():
                    next_cell = array[visited[i][0], visited[i][1]]
                    break

            # CHECK RIGHT
            if visited[i][1] != len(array[0]) - 1:
                cell_right = array[visited[i][0], visited[i][1] + 1]
                if not cell_right.isVisited():
                    next_cell = array[visited[i][0], visited[i][1]]
                    break

            # CHECK LEFT
            if visited[i][1] != 0:
                cell_left = array[visited[i][0], visited[i][1] - 1]
                if not cell_left.isVisited():
                    next_cell = array[visited[i][0], visited[i][1]]
                    break

            # CHECK BOTTOM
            if visited[i][0] != len(array) - 1:
                cell_below = array[visited[i][0] + 1, visited[i][1]]
                if not cell_below.isVisited():
                    next_cell = array[visited[i][0], visited[i][1]]
                    break
        if next_cell is not None:
            makeAPath(next_cell, array)

    final_array = np.zeros((rows * 4, cols * 4, 3), np.uint8)
    final_array[:0:cols * 4] = (0, 0, 0)
    for i in range(0, len(final_array), 4):
        for j in range(0, len(final_array[0]), 4):
            for a in range(4):
                for b in range(4):
                    if array[i // 4, j // 4].isPath(a, b):
                        final_array[i + a, j + b] = path_color
                    else:
                        final_array[i + a, j + b] = wall_color
    print("\t100%")
    return final_array


def makeAPath(c: Cell, arr):
    # make a list of neighboring cells
    neighbors = []
    # CHECK TOP
    if c.getRow() != 0:
        cell_above = arr[c.getRow() - 1, c.getCol()]
        if not cell_above.isVisited():
            neighbors.append(arr[c.getRow() - 1, c.getCol()])

    # CHECK RIGHT
    if c.getCol() != len(arr[0]) - 1:
        cell_right = arr[c.getRow(), c.getCol() + 1]
        if not cell_right.isVisited():
            neighbors.append(arr[c.getRow(), c.getCol() + 1])

    # CHECK LEFT
    if c.getCol() != 0:
        cell_left = arr[c.getRow(), c.getCol() - 1]
        if not cell_left.isVisited():
            neighbors.append(arr[c.getRow(), c.getCol() - 1])

    # CHECK BOTTOM
    if c.getRow() != len(arr) - 1:
        cell_below = arr[c.getRow() + 1, c.getCol()]
        if not cell_below.isVisited():
            neighbors.append(arr[c.getRow() + 1, c.getCol()])

    # End Condition
    if len(neighbors) == 0:
        return

    # Pick a random member of the neighbors list
    rd.shuffle(neighbors)
    next_cell: Cell = neighbors[0]
    c.Visit()
    next_cell.Visit()
    visited.append((next_cell.getRow(), next_cell.getCol()))
    c.makePath(next_cell)
    makeAPath(next_cell, arr)
