"""
Leibniz formula:
    pi/4 = (sum([(pow(-1, k))/(2k + 1) for k in range(0, inf)])) = (1 - 1/3 + 1/5 - 1/7 + 1/9 ...)
"""


def calculate_pi(n_terms):
    """
    Example from the book
    """
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2
        operation *= -1
    return pi


if __name__ == "__main__":
    n_terms = 1_000_000
    print(f"{n_terms} Terms")
    print(f"Book's Solution: {calculate_pi(n_terms)}")
    print(f"My Solution: {4 * (sum([(pow(-1, k))/(2*k + 1) for k in range(n_terms)]))}")
    """
    Book's solution is noticeably faster due to the number of times pow is called
    """
