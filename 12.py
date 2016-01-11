# https://www.interviewcake.com/question/python/find-in-ordered-set

# binary search


def solve(alist, value):
    length = len(alist)
    if length == 1:
        if alist[0] == value:
            return True
        return False

    mid = length / 2
    if alist[mid] == value:
        return True
    if alist[mid] < value:
        return solve(alist[mid+1:], value)
    else:
        return solve(alist[0:mid-1], value)


assert solve([1, 2, 3], 2)
assert solve([1, 2, 2, 3], 2)
assert solve([1, 2, 2, 4], 5) == False
