import random
from CCSP.ProfilerTools import Timer
from CCSP.generic_search import linear_contains, binary_contains, dfs, bfs, a_star
from MazeSolving import Maze, manhattan_distance


def exercise_1(maximum):
    ls = [random.randint(0, maximum) for _ in range(1_000_000)]

    @Timer(message="Linear Search")
    def call_linear_search():
        return linear_contains(ls, random.randint(0, maximum))

    @Timer(message="Binary Search")
    def call_binary_search():
        return binary_contains(ls, random.randint(0, maximum))

    call_linear_search()
    call_binary_search()
    print("\n\nList Sorted")
    ls.sort()
    call_linear_search()
    call_binary_search()


def exercise_2(num_mazes):
    searches = [dfs, bfs, a_star]
    states_avg = [1, 1, 1]
    impossible_mazes = 0
    for i, search in enumerate(searches):
        for _ in range(num_mazes):
            m = Maze()
            if i == 2:
                solution = search(
                    m.start,
                    m.goal_test,
                    m.successors,
                    manhattan_distance(m.goal),
                    count=True,
                )
            else:
                solution = search(m.start, m.goal_test, m.successors, count=True)
            if solution is None:
                impossible_mazes += 1
            else:
                states_avg[i] = (states_avg[i] + solution[1]) / 2

    print(f"Depth First Search: {states_avg[0]:.2f} Nodes")
    print(f"Breadth First Search: {states_avg[1]:.2f} Nodes")
    print(f"A* First Search: {states_avg[2]:.2f} Nodes")
    print(f"Impossible Mazes: {impossible_mazes}/{num_mazes}")


"""
A Note on Exercise 3:
    The Missionary Cannibal problem is impossible with more than 3 M & C, this is rather disappointing.
"""


if __name__ == "__main__":
    #  exercise_1(100)
    exercise_2(200)
