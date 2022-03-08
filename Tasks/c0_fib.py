def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int: #O(n)
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(n - 1):
        # sum_ = a + b
        # a = b
        # b = sum_
        a, b = b, a + b
    return b

def generator_fib(n):
    a = 0
    yield a
    b = 1
    yield b
    for _ in range(n - 2):
        a, b = b, a + b
        yield b
N = 10
list_ = [fib_iterative(i) for i in range(N)] #O(n**2)
list1_ = [j for j in generator_fib(N)] #O(n)

print(list_)
print(list1_)

