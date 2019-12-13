from enum import Enum
import random
from math import sqrt
from CCSP.generic_search import dfs, bfs, node_to_path, a_star


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return int("1" + str(self.row) + str(self.column))

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        try:
            switch = {0: self.row, 1: self.column}
            result = switch[self.i]
            self.i += 1
            return result
        except KeyError:
            raise StopIteration


class Maze:
    def __init__(self, rows=10, columns=10, sparseness=0.20, start=MazeLocation(0, 0)):
        goal = MazeLocation(rows - 1, columns - 1)
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def __str__(self):
        output = " " + "_" * self._columns + "\n"
        for row in self._grid:
            output += "|" + "".join([c.value for c in row]) + "|\n"
        return output + " " + "_" * self._columns + "\n"

    def _randomly_fill(self, rows, columns, sparseness):
        for r in range(rows):
            for c in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[r][c] = Cell.BLOCKED

    def goal_test(self, current_location):
        return current_location == self.goal

    def successors(self, location):
        heirs = []
        # Check up/down
        if (
            location.row + 1 < self._rows
            and self._grid[location.row + 1][location.column] != Cell.BLOCKED
        ):
            heirs.append(MazeLocation(location.row + 1, location.column))
        if (
            location.row - 1 >= 0
            and self._grid[location.row - 1][location.column] != Cell.BLOCKED
        ):
            heirs.append(MazeLocation(location.row - 1, location.column))
        # Check left/right
        if (
            location.column + 1 < self._columns
            and self._grid[location.row][location.column + 1] != Cell.BLOCKED
        ):
            heirs.append(MazeLocation(location.row, location.column + 1))
        if (
            location.column - 1 >= 0
            and self._grid[location.row][location.column - 1] != Cell.BLOCKED
        ):
            heirs.append(MazeLocation(location.row, location.column - 1))
        return heirs

    def mark(self, path, clear=False):
        fill = Cell.EMPTY if clear else Cell.PATH
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = fill
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


def euclidean_distance(goal):
    return lambda location: sqrt(sum([x - y for x, y in zip(location, goal)]))


def manhattan_distance(goal):
    return lambda location: sum([abs(x - y) for x, y in zip(location, goal)])


def test_dfs(m):
    solution = dfs(m.start, m.goal_test, m.successors)
    if solution is None:
        print("No solution using Depth First Search")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        print(f'DFS Path Length: {len(path)}, "Effecency": {19/len(path)}')
        m.mark(path, clear=True)


def test_bfs(m):
    solution = bfs(m.start, m.goal_test, m.successors)
    if solution is None:
        print("No solution using Breadth First Search")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        print(f"BFS Path Length: {len(path)}")
        m.mark(path, clear=True)


def test_a_star(m):
    solution = a_star(m.start, m.goal_test, m.successors, manhattan_distance(m.goal))
    if solution is None:
        print("No solution using A* Search")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        print(f"A* Path Length: {len(path)}")
        m.mark(path, clear=True)


if __name__ == "__main__":
    maze = Maze()
    print(maze)
    test_dfs(maze)
    test_bfs(maze)
    test_a_star(maze)
