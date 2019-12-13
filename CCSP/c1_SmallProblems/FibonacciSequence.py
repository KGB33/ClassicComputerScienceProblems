from functools import lru_cache


def fib_1(n):
    """
    Will raise Recursion Error due to no base cases
    """
    return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    """
    Works for smaller n's but falters for lager ones because fib_2(n-a) is called exponentially
    """
    if n < 2:  # Base Case
        return n
    return fib_2(n - 1) + fib_2(n - 2)


memo = {0: 0, 1: 1}  # Base Case for fib_3


def fib_3(n):
    """
    Uses memoization to decrease the times fib_3(n - a) is called.
    """
    if n not in memo:
        memo[n] = fib_3(n - 1) + fib_3(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib_4(n):
    """
    Uses the lru_cache decorator from functools to automate memoization
    """
    if n < 2:  # Base Case
        return n
    return fib_4(n - 1) + fib_4(n - 2)


def fib_5(n):
    """
    Uses Iteration to solve even faster
    """
    if n == 0:
        return n
    f_2 = 0
    f_1 = 1
    for _ in range(1, n):
        f_2, f_1 = f_1, f_2 + f_1
    return f_1


def fib_6(n):
    """
    Fibonacci Generator
    """
    yield 0
    if n > 0:
        yield 1
    f_2 = 0
    f_1 = 1
    for _ in range(1, n):
        f_2, f_1 = f_1, f_2 + f_1
        yield f_1


if __name__ == "__main__":
    print(f"Fib 3: {fib_3(50)}")
    print(f"Fib 4: {fib_4(50)}")
    print(f"Fib 5: {fib_5(50)}")
    for i in fib_6(50):
        print(f"Fib 6, {i}")
