# https://www.interviewcake.com/question/python/find-rotation-point


def solve(alist):
    return binary(alist, 0, len(alist))


# the space is O(lgN)
def binary(alist, i, j):
    mid = (j-i) / 2
    mid_value = alist[mid]

    if alist[mid-1] > mid_value:
        return mid

    if mid_value > alist[0]:
        # should be the right side
        return binary(alist, mid, j)

    if mid_value < alist[-1]:
        # should be the left side
        return binary(alist, i, mid)

# only O(1)
def solve(alist):
    i, j = 0, len(alist)

    while True:
        mid = (j-i) / 2
        mid_value = alist[mid]

        if alist[mid-1] > mid_value:
            return mid

        if mid_value > alist[0]:
            i = mid

        elif mid_value < alist[-1]:
            j = mid

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

assert solve(words) == 5
