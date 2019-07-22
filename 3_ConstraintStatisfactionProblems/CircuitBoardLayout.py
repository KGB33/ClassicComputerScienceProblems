from functools import lru_cache
from csp import CSP, Constraint
from itertools import product


class CircuitBoardLocation:

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

    def __str__(self):
        return f'Row: {self.row}, Column: {self.column}'


class CircuitBoard:

    def __init__(self, grid_size):
        self.grid = [[' ' for _ in range(grid_size)] for __ in range(grid_size)]
        self.grid_size = grid_size

    def __str__(self):
        result = ''
        for row in self.grid:
            for letter in row:
                result += letter + ' '
            result += '\n'
        return result

    @lru_cache(maxsize=None)
    def generate_domain(self, circuit_height, circuit_length, recurse=True):
        domain = []
        height = length = self.grid_size

        for row in range(height):
            for column in range(length):
                columns = range(column, column + circuit_length)
                rows = range(row, row + circuit_height)

                if column + circuit_length <= length:
                    #  Left to right
                    if row + circuit_height <= height:
                        # Top to bottom
                        domain.append([CircuitBoardLocation(r, c) for r, c in product(rows, columns)])
        if recurse:
            # Rotate boxes 90degrees
            return domain + self.generate_domain(circuit_length, circuit_height, recurse=False)
        return domain


class CircuitBoardConstraint(Constraint):

    def __init__(self, boxes):
        super().__init__(boxes)
        self.boxes = boxes

    def satisfied(self, assignment):
        """
        Checks to see if there is any overlap in boxes
        """
        all_locations = []
        for locations in assignment.values():
            for location in locations:
                all_locations.append((location.row, location.column))
        return len(set(all_locations)) == len(all_locations)


def print_grid(solution, grid_size):
    grid = [[' ' * 3 for _ in range(grid_size)] for __ in range(grid_size)]
    for box, grid_locations in solution.items():
        for gl in grid_locations:
            grid[gl.row][gl.column] = f'{chr(int(box)+1000):^3}'
    for row in grid:
        print(row)


def main():
    GRID_SIZE = 9
    CB = CircuitBoard(GRID_SIZE)
    boxes = (
        # From Book
        '44',
        '33',
        '22',
        '61',
        '25',
        # More Squares
        '31',
        '17',
        '23',
        '11',
        '41',
        '32',
        '51',
        '14',
        # 9x9 area is full
    )
    locations = {}
    for box in boxes:
        locations[box] = CB.generate_domain(int(box[0]), int(box[1]))
    csp = CSP(boxes, locations)
    csp.add_constraint(CircuitBoardConstraint(boxes))
    solution = csp.backtracking_search()
    if solution is None:
        print('No Solution Found')
    else:
        for box, grid_locations in solution.items():
            print(f'Box: {box},'
                  f'Grid Location: {[gl.__str__() for gl in grid_locations]},'
                  f'Area: {len(grid_locations)}\n')
    print_grid(solution, GRID_SIZE)


if __name__ == '__main__':
    main()
