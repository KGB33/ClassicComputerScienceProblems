from functools import lru_cache
from itertools import product
from math import ceil
from time import time

from csp import Constraint, CSP



"""
From the Wikipedia page 'Mathematics of Sudoku"

    A puzzle can be expressed as a graph coloring problem.
    The aim is to construct a 9-coloring of a particular graph,
    given a partial 9-coloring. The Sudoku graph has 81 vertices,
    one vertex for each cell. The vertices are labeled with ordered pairs
    (x, y), where x and y are integers between 1 and 9.
    In this case, two distinct vertices labeled by (x_1, y_1) and (x_2, y_2) are joined by an edge if and only if:

        x_1 = x_2(same column) or,
        y_1 = y_2(same row) or,
        ⌈ x/3 ⌉ = ⌈ x′/3 ⌉ and ⌈ y/3 ⌉ = ⌈ y′/3 ⌉ (same 3×3 cell)


    The puzzle is then completed by assigning an integer between 1 and 9 to each vertex,
    in such a way that vertices that are joined by an edge do not have the same integer assigned to them.

"""


class Vertex:
    """
    Defines a vertex in the graph.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @lru_cache(maxsize=None)
    def connected(self, other):
        """
        Determines if self and other are connected For a Sudoku graph
        :param other: Vertex
        :return: Boolean
        """
        if self.x == other.x:
            return True
        if self.y == other.y:
            return True
        if ceil((self.x + 1) / 3) == ceil((other.x + 1) / 3) and ceil((self.y + 1) / 3) == ceil((other.y + 1) / 3):
            return True
        else:
            return False

    def __str__(self):
        return f'Vertex: ({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Graph:
    """
    A collection of vertices
    """

    def __init__(self, size=9, dim=2):
        self.vertices = [Vertex(x, y) for x, y in product(range(0, size), repeat=dim)]


class ColoringConstraint(Constraint):

    def __init__(self, vertices):
        super().__init__(vertices)
        self.vertices = vertices

    def satisfied(self, assignment):
        for vertex in assignment:
            copy = assignment.copy()
            del copy[vertex]
            for vertex_2 in copy:
                if vertex.connected(vertex_2):
                    if assignment[vertex] == assignment[vertex_2]:
                        return False
        # if all Vertices have not yet been assigned a color keep searching
        return True


class ClueConstraint(Constraint):
    """
    Makes sure the clues are not modified
    """

    def __init__(self, clues):
        super().__init__([x for x in clues])
        self.clues = clues

    def satisfied(self, assignment):
        for vertex in assignment:
            if vertex in self.clues:
                if assignment[vertex] != self.clues[vertex]:
                    return False
        return True


def make_min_clues():
    clues = {
        Vertex(0, 3): 8,
        Vertex(0, 5): 1,
        Vertex(1, 7): 4,
        Vertex(1, 8): 3,
        Vertex(2, 0): 5,
        Vertex(3, 4): 7,
        Vertex(3, 6): 8,
        Vertex(4, 6): 1,
        Vertex(5, 1): 2,
        Vertex(5, 4): 3,
        Vertex(6, 0): 6,
        Vertex(6, 7): 7,
        Vertex(6, 8): 5,
        Vertex(7, 2): 3,
        Vertex(7, 3): 4,
        Vertex(8, 3): 2,
        Vertex(8, 6): 6,
    }
    return clues


def make_clues_easy():
    clues = {
        Vertex(0, 2): 3,
        Vertex(0, 5): 7,
        Vertex(0, 8): 5,
        Vertex(1, 0): 4,
        Vertex(1, 1): 5,
        Vertex(1, 3): 9,
        Vertex(1, 4): 1,
        Vertex(2, 3): 5,
        Vertex(2, 6): 6,
        Vertex(2, 7): 4,
        Vertex(2, 8): 8,
        Vertex(3, 0): 5,
        Vertex(3, 3): 7,
        Vertex(3, 5): 1,
        Vertex(3, 7): 3,
        Vertex(3, 8): 4,
        Vertex(4, 2): 1,
        Vertex(4, 3): 2,
        Vertex(4, 5): 4,
        Vertex(4, 6): 7,
        Vertex(5, 0): 6,
        Vertex(5, 1): 4,
        Vertex(5, 3): 3,
        Vertex(5, 5): 8,
        Vertex(5, 8): 9,
        Vertex(6, 0): 8,
        Vertex(6, 1): 2,
        Vertex(6, 2): 5,
        Vertex(6, 5): 9,
        Vertex(7, 4): 2,
        Vertex(7, 5): 5,
        Vertex(7, 7): 8,
        Vertex(7, 8): 7,
        Vertex(8, 0): 9,
        Vertex(8, 3): 6,
        Vertex(8, 6): 5,
    }
    return clues


def main():
    grid = Graph()
    colors = {}
    clues = make_min_clues()
    # clues = make_clues_easy()
    for vertex in grid.vertices:
        colors[vertex] = [c for c in range(1, 10)]

    csp = CSP(grid.vertices, colors)
    csp.add_constraint(ColoringConstraint(grid.vertices))
    before = time()
    solution = csp.backtracking_search(assignment=clues)
    print(f'Time Elapsed: {time() - before:.3}s')
    if solution is None:
        print('No Solution Found')
    else:
        for vert, color in solution.items():
            print(vert, f'Color: {color}')


if __name__ == '__main__':
    main()
