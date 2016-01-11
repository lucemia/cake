# https://www.interviewcake.com/question/python/highest-product-of-3

def solve(alist):
    alist.sort()

    # largest[-3]
    # largest * smallest[2]
    a = alist[-1] * alist[-2] * alist[-3]
    b = alist[-1] * alist[0] * alist[1]

    return a if a > b else b

def solve(alist):
    # O(1) space
    picka = [None, None, None]
    pickb = [None, None, None]

    # find the largest 3 items
    for i in alist:
        j = i
        for k in range(3):
            if not picka[k] or not picka[k] > j:
                picka[k], j = j, picka[k]

        for k in range(1, 3):
            if not pickb[k] or not pickb[k] < i:
                pickb[k], i = i, pickb[k]

        pickb[0] = picka[0]

    a = picka[0] * picka[1] * picka[2]
    b = pickb[0] * pickb[1] * pickb[2]

    return a if a > b else b

solve([1, 1, 1, 1, 1, 1]) == 1
solve([-10, 0, 12, -10]) == 1200
solve([-10, -10, 1, 3, 2]) == 300
