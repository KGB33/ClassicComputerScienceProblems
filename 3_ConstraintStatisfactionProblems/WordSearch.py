from random import choice
from string import ascii_uppercase
from functools import lru_cache
from csp import CSP, Constraint


class GridLocation:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        try:
            switch = {0: self.row,
                      1: self.column}
            result = switch[self.i]
            self.i += 1
            return result
        except KeyError:
            raise StopIteration


class Grid:

    def __init__(self, grid_size):
        self.grid = [[choice(ascii_uppercase) for _ in range(grid_size)] for __ in range(grid_size)]
        self.grid_size = grid_size

    def __str__(self):
        result = ''
        for row in self.grid:
            for letter in row:
                result += letter + ' '
            result += '\n'
        return result

    @lru_cache(maxsize=None)
    def generate_domain(self, word_length):
        domain = []
        height = width = self.grid_size

        for row in range(height):
            for column in range(width):
                columns = range(column, column + word_length + 1)
                rows = range(row, row + word_length + 1)

                if column + word_length <= width:
                    #  Left to right
                    domain.append([GridLocation(row, c) for c in columns])
                    if row + word_length <= height:
                        #  Diagonal towards bottom right
                        domain.append([GridLocation(r, column + (r - row)) for r in rows])

                if row + word_length <= height:
                    #  Top to bottom
                    domain.append([GridLocation(r, column) for r in rows])
                    if column - word_length >= 0:
                        #  Diagonal towards bottom left
                        domain.append([GridLocation(r, column - (r - row)) for r in rows])
        return domain


class WordSearchConstraint(Constraint):

    def __init__(self, words):
        super().__init__(words)
        self.words = words

    def satisfied(self, assignment):
        """
        Checks to see if there is any overlap in words
        """
        all_locations = []
        for locations in assignment.values():
            for location in locations:
                all_locations.append((location.row, location.column))
        return len(set(all_locations)) == len(all_locations)


def main():
    grid = Grid(15)
    words = [
        'Mathew',
        'Joe',
        'Marry',
        'Sarah',
        'Sally',
        'constraint',
        'satisfaction',
        'problem',
    ]
    locations = {}
    for word in words:
        locations[word] = grid.generate_domain(len(word))
    csp = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution = csp.backtracking_search()
    if solution is None:
        print('No Solution Found')
    else:
        for word, grid_locations in solution.items():
            #  Randomly reverse words 1/2 the time
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid.grid[row][col] = letter.upper()
        print(grid)


if __name__ == '__main__':
    main()


