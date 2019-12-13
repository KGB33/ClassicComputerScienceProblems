from csp import Constraint, CSP


class SendMoreMoneyConstraint(Constraint):
    def __init__(self, word_1, word_2, sum_word, letters):
        super().__init__(letters)
        self.letters = letters
        self.word_1 = word_1
        self.word_2 = word_2
        self.sum_word = sum_word

    def satisfied(self, assignment):

        #  Check to see if there are duplicate vals
        if len(set(assignment.values())) < len(assignment):
            return False

        #  Check to see if it is a complete solution
        if len(assignment) == len(self.letters):
            addend_1 = sum(
                [
                    assignment[letter] * pow(10, slot)
                    for slot, letter in enumerate(self.word_1[::-1])
                ]
            )
            addend_2 = sum(
                [
                    assignment[letter] * pow(10, slot)
                    for slot, letter in enumerate(self.word_2[::-1])
                ]
            )
            word_sum = sum(
                [
                    assignment[letter] * pow(10, slot)
                    for slot, letter in enumerate(self.sum_word[::-1])
                ]
            )
            return addend_1 + addend_2 == word_sum

        # If it is an incomplete solution return true
        return True


def main():
    word_1 = "SEND"
    word_2 = "MORE"
    sum_word = "MONEY"
    letters = set([letter for letter in word_1 + word_2 + sum_word])
    possible_digits = {}
    for letter in set([letter for letter in word_1 + word_2 + sum_word]):
        possible_digits[letter] = [x for x in range(10)]

    # possible_digits['M'] = [x for x in range(1, 10)]  # To prevent answers starting with a Zero

    csp = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(word_1, word_2, sum_word, letters))
    solution = csp.backtracking_search()
    if solution is None:
        print("No Solution Found")
    else:
        print(solution)


if __name__ == "__main__":
    main()
