# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space


def sol(alist):
    def _next(index):
        return alist[index]

    p1 = alist[-1]
    p2 = alist[-1]

    p1 = _next(p1)
    p2 = _next(_next(p2))

    while p1 != p2:
        p1 = _next(p1)
        p2 = _next(_next(p2))

    p1 = alist[-1]

