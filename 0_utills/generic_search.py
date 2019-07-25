from collections import deque
from heapq import heappop, heappush



def linear_contains(iterable, key):
    for item in iterable:
        if item == key:
            return True
    return False


def binary_contains(iterable, key):
    low = 0
    high = len(iterable) - 1
    while low <= high:  # While there is still a search space
        mid = (low + high) // 2
        if iterable[mid] < key:
            low = mid + 1
        elif iterable[mid] > key:
            high = mid - 1
        else:
            return True
    return False


class Stack:

    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def pop(self):
        return self._container.pop()

    def push(self, item):
        self._container.append(item)

    def __repr__(self):
        return repr(self._container)


class Queue:

    def __init__(self):
        self._container = deque()

    def __bool__(self):
        return self._container

    @property
    def empty(self):
        return not self.__bool__()

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __repr__(self):
        return repr(self._container)


class PriorityQueue:

    def __init__(self):
        self._container = []

    def __bool__(self):
        return self._container

    @property
    def empty(self):
        return not self.__bool__()

    def push(self, item):
        heappush(self._container, item)

    def pop(self):
        return heappop(self._container)

    def __repr__(self):
        return repr(self._container)


class Node:

    def __init__(self, state, parent, cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def node_to_path(node):
    path = [node.state, ]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


def dfs(initial, goal_test, successors, count=False):
    frontier = Stack()
    frontier.push(Node(initial, None))

    explored = {initial, }
    counter = 0

    while not frontier.empty:
        counter += 1
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            if count:
                return current_node, counter
            else:
                return current_node
        for child in successors(current_state):
            if child in explored:
                continue  # Skip already explored nodes
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def bfs(initial, goal_test, successors, count=False):
    frontier = Queue()
    frontier.push(Node(initial, None))

    explored = {initial, }
    counter = 0

    while not frontier.empty:
        counter += 1
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            if count:
                return current_node, counter
            else:
                return current_node
        for child in successors(current_state):
            if child in explored:
                continue  # Skip already explored nodes
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def a_star(initial, goal_test, successors, heuristic, count=False):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))

    explored = {initial: 0.0, }
    counter = 0

    while not frontier.empty:
        counter += 1
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            if count:
                return current_node, counter
            else:
                return current_node
        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None


