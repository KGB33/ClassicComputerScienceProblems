from csp import CSP, Constraint


class QueenConstraint(Constraint):

    def __init__(self, col):
        super().__init__(col)
        self.columns = col

    def satisfied(self, assignment):
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):
                        return False
        return True


if __name__ == '__main__':
    columns = [x for x in range(1, 9)]
    rows = {}
    for column in columns:
        rows[column] = [x for x in range(1, 9)]
    csp = CSP(columns, rows)
    csp.add_constraint(QueenConstraint(columns))
    solution = csp.backtracking_search()
    if solution is None:
        print('No Solution Found!')
    else:
        print(solution)
        