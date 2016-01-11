# https://www.interviewcake.com/question/python/inflight-entertainment


def binary_search(alist, value):
    pass


# n ln N
def solve(alist, flight_length):
    alist.sort()

    for index, i in enumerate(alist):
        if i >= flight_length - i:
            return False

        if binary_search(alist[index:], flight_length - i):
            return True

# n
def solve(alist, flight_length):
    x = set()
    for i in alist:
        x.add(flight_length-i)

    for i in alist:
        if i in x and i != flight_length/2:
            return True
