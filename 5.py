# https://www.interviewcake.com/question/python/coin
# TODO: button up approach

def solve(amount, denominations):
    denominations.sort(reverse=True)

    return [tuple(reversed(k)) for k in solve_sorted(amount, denominations)]


def solve_sorted(amount, denominations):
    if len(denominations) == 1:
        if amount % denominations[0] == 0:
            return [[amount / denominations[0]]]
        return []

    v = []
    coin = denominations[0]

    for i in range(amount / coin + 1):
        if amount - i*coin < 0:
            break

        for sol in solve_sorted(amount-i*coin, denominations[1:]):
            v.append(tuple([i] + list(sol)))

    return v


def solve(amount, denominations):
    pass



assert set(solve(4, [1, 2, 3])) == set([(4, 0, 0), (2, 1, 0), (1, 0, 1), (0, 2, 0)])
