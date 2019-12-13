from CCSP.generic_search import bfs, node_to_path, a_star


MAX_NUM = 3


class MissionariesCannibalsState:
    def __init__(self, missionaries, cannibals, boat, max_persons=MAX_NUM):
        self.west_missionaries = missionaries
        self.east_missionaries = max_persons - missionaries
        self.west_cannibals = cannibals
        self.east_cannibals = max_persons - cannibals
        self.boat = boat
        self.max_num = max_persons

    def __str__(self):
        return (
            "    West    ****    East    \n"
            "------------****------------\n"
            "            ****            \n"
            f'{" M " * self.west_missionaries:^12}****{" M " * self.east_missionaries:^12}\n'
            "            ****            \n"
            f'{"           B****            " if self.boat else "            ****B           "}\n'
            "            ****            \n"
            f'{" C " * self.west_cannibals:^12}****{" C " * self.east_cannibals:^12}\n\n\n'
        )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __lt__(self, other):
        return self.min_boat_trips() < other.min_boat_trips()

    def __hash__(self):
        return int(
            str(self.max_num)
            + str(self.west_missionaries)
            + str(self.west_cannibals)
            + str(int(self.boat))
        )

    def wordy_print(self):
        return (
            f"On the West bank there are {self.west_missionaries} missionaries and {self.west_cannibals} cannibals\n"
            f"On the East bank there are {self.east_missionaries} missionaries and {self.east_cannibals} cannibals\n"
            f'The boat is on the {"west" if self.boat else "East"}\n\n'
        )

    @property
    def is_legal(self):
        if self.west_cannibals > self.west_missionaries > 0:
            return False
        if self.east_cannibals > self.east_missionaries > 0:
            return False
        if self.max_num != (self.west_cannibals + self.east_cannibals):
            return False
        if self.max_num != (self.west_missionaries + self.east_missionaries):
            return False
        return True

    def goal_test(self):
        return (
            self.is_legal
            and self.east_missionaries == self.max_num
            and self.east_cannibals == self.max_num
        )

    def successors(self):
        heirs = []
        if self.boat:  # Boat is on the west Side
            if self.west_missionaries > 1:  # Two Missionaries on the boat
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries - 2, self.west_cannibals, not self.boat
                    )
                )
            if self.west_missionaries > 0:  # One Missionary
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries - 1, self.west_cannibals, not self.boat
                    )
                )
            if self.west_cannibals > 1:  # Two Cannibals
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries, self.west_cannibals - 2, not self.boat
                    )
                )
            if self.west_cannibals > 0:  # One Cannibal
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries, self.west_cannibals - 1, not self.boat
                    )
                )
            if self.west_cannibals > 0 and self.west_missionaries > 0:  # One Of Each
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries - 1,
                        self.west_cannibals - 1,
                        not self.boat,
                    )
                )
        else:  # Boat on east side
            if self.east_missionaries > 1:  # Two Missionaries on the boat
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries + 2, self.west_cannibals, not self.boat
                    )
                )
            if self.east_missionaries > 0:  # One Missionary
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries + 1, self.west_cannibals, not self.boat
                    )
                )
            if self.east_cannibals > 1:  # Two Cannibals
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries, self.west_cannibals + 2, not self.boat
                    )
                )
            if self.east_cannibals > 0:  # One Cannibal
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries, self.west_cannibals + 1, not self.boat
                    )
                )
            if self.east_cannibals > 0 and self.west_missionaries > 0:  # One Of Each
                heirs.append(
                    MissionariesCannibalsState(
                        self.west_missionaries + 1,
                        self.west_cannibals + 1,
                        not self.boat,
                    )
                )
        return [x for x in heirs if x.is_legal]

    def min_boat_trips(self):
        return (self.west_missionaries + self.west_cannibals) // 2 + 1


def display_solution(p):
    if len(p) == 0:
        return
    old_state = p[0]
    print(old_state)
    for current_state in p[1:]:
        if current_state.boat:
            print(
                f"{old_state.east_missionaries - current_state.east_missionaries} missionaries and "
                f"{old_state.east_cannibals - current_state.east_cannibals} cannibals moved from "
                f"the east Bank to the west bank"
            )
        else:
            print(
                f"{old_state.west_missionaries - current_state.west_missionaries} missionaries and "
                f"{old_state.west_cannibals - current_state.west_cannibals} cannibals moved from "
                f"the west Bank to the east bank"
            )
        print(current_state)
        old_state = current_state


if __name__ == "__main__":
    start = MissionariesCannibalsState(MAX_NUM, MAX_NUM, True, max_persons=MAX_NUM)
    solution = a_star(
        start,
        MissionariesCannibalsState.goal_test,
        MissionariesCannibalsState.successors,
        MissionariesCannibalsState.min_boat_trips,
    )

    if solution is None:
        print("No Solution Found :(\n\tAt least the Cannibals got lunch")
    else:
        path = node_to_path(solution)
        display_solution(path)
