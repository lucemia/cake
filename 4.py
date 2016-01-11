# https://www.interviewcake.com/question/python/merging-ranges

def solve(alist):
    alist.sort()

    v = []
    current = alist[0]

    for i in range(1, len(alist)):
        if current[1] >= alist[i][0]:
            current = (current[0], max(alist[i][1], current[1]))
        else:
            v.append(current)
            current = alist[i]

    v.append(current)
    return v

assert solve([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [(0, 1), (3, 8), (9, 12)]
assert solve([(1, 2), (2, 3)]) == [(1, 3)]
assert solve([(1, 5), (2, 3)]) == [(1, 5)]
assert solve([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)]
