"""
From Wikipedia

    The Tower of Hanoi consists of three rods and a number of disks of different sizes, which can slide onto any rod.
    The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top,
    thus making a conical shape.

    The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

        - Only one disk can be moved at a time.
        - Each move consists of taking the upper disk from one of
            the stacks and placing it on top of another stackor on an empty rod.
        - No larger disk may be placed on top of a smaller disk.

    With 3 disks, the puzzle can be solved in 7 moves.
    The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks.
"""


class Stack:
    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        #  Will be used to view the contents of the container
        return repr(self._container)


def hanoi(begin, end, temp, n):
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    num_disks = 3
    tower_a = Stack()
    tower_b = Stack()
    tower_c = Stack()
    for i in range(1, num_disks + 1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_disks)
    print(f"Tower A: {tower_a}")
    print(f"Tower B: {tower_b}")
    print(f"Tower C: {tower_c}")
