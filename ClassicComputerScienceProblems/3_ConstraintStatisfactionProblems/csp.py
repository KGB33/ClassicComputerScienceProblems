from abc import ABC, abstractmethod


class Constraint(ABC):
    """
    Each Constraint contains the variables it contains,
    and a method to check if it is satisfied()
    """

    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment):
        pass


class CSP:

    def __init__(self, variables, domains):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for var in self.variables:
            self.constraints[var] = []
            if var not in self.domains:
                raise LookupError(f'Every Var needs a Domain. {var}')

    def add_constraint(self, constraint):
        for var in constraint.variables:
            if var not in self.variables:
                raise LookupError(f'Variable in Constraint not in CSP. {var}')
            else:
                self.constraints[var].append(constraint)

    def consistent(self, var, assignment):
        for constraint in self.constraints[var]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]

        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None


if __name__ == '__main__':
    pass
