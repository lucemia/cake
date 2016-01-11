# https://www.interviewcake.com/question/python/nth-fibonacci

# O(n) space
def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)


def fib(n):
    n1 = 0
    n2 = 1

    if n == 0:
        return 0
    if n == 1:
        return 1

    i = 2
    while i <= n:
        k = n1 + n2
        n1 = n2
        n2 = k

        i += 1

    return k

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
