# https://www.interviewcake.com/question/python/product-of-other-numbers

# NOTES

def solve(alist):
    # 2 O(n)
    new_list = [1] * len(alist)
    s = 1
    for index, i in enumerate(alist):
        new_list[index] *= s
        s *= i

    s = 1
    j = len(alist) - 1
    while j >= 0:
        new_list[j] *= s
        s *= alist[j]
        j -= 1

    # print new_list
    return new_list


assert solve([1, 7, 3, 4]) == [84, 12, 28, 21]
assert solve([1, 7, 0, 4]) == [0, 0, 28, 0]
