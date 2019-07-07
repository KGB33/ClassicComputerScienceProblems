from csp import Constraint, CSP


class MapColoringConstraint(Constraint):

    def __init__(self, region1, region2):
        super().__init__([region1, region2])
        self.region1 = region1
        self.region2 = region2

    def satisfied(self, assignment):
        """
        Two regions cannot conflict if one of them does not yet have a color
        and
        The colors assigned to each region should not be the same
        """
        if self.region1 not in assignment or self.region2 not in assignment:
            return True
        return assignment[self.region1] != assignment[self.region2]


def main():
    variables = [
        'W. Aus',
        'N. Ter',
        'S. Aus',
        'Queensland',
        'New S. Wales',
        'Victoria',
        'Tasmania',
    ]
    domains = {}
    for var in variables:
        domains[var] = ['red', 'green', 'blue']
    csp = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint('W. Aus', 'N. Ter'))
    csp.add_constraint(MapColoringConstraint('W. Aus', 'S. Aus'))
    csp.add_constraint(MapColoringConstraint('N. Ter', 'Queensland'))
    csp.add_constraint(MapColoringConstraint('N. Ter', 'S. Aus'))
    csp.add_constraint(MapColoringConstraint('S. Aus', 'Queensland'))
    csp.add_constraint(MapColoringConstraint('S. Aus', 'New S. Wales'))
    csp.add_constraint(MapColoringConstraint('S. Aus', 'Victoria'))
    csp.add_constraint(MapColoringConstraint('Queensland', 'New S. Wales'))
    csp.add_constraint(MapColoringConstraint('New S. Wales', 'Victoria'))
    csp.add_constraint(MapColoringConstraint('Victoria', 'Tasmania'))
    solution = csp.backtracking_search()
    if solution is None:
        print('No Solution Found')
    else:
        print(solution)


if __name__ == '__main__':
    main()


