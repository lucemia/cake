

def solve(alist):
    max_profit = None
    lowest_buy_point = None
    best_sell_point = None

    for i in alist:
        if not lowest_buy_point:
            lowest_buy_point = i
            continue

        profit = i - lowest_buy_point
        if not max_profit or profit > max_profit:
            max_profit = profit
            best_sell_point = i

        if i < lowest_buy_point:
            lowest_buy_point = i

    return max_profit

assert solve([10, 7, 5, 8, 11, 9]) == 6
assert solve([15, 9, 7, 3, 0]) == -2
