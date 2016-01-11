# https://www.interviewcake.com/question/python/matching-parens

t = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing"

# O(n) space
def solve(t, index):
    stack = []
    for i, c in enumerate(t):
        if c == "(":
            stack.append(i)

        if c == ")":
            x = stack.pop()

            if x == index:
                return i

# O(1) space

def solve(t, index):
    count = 0
    _index = 0
    for i, c in enumerate(t):
        if c == "(":
            if index == i:
                _index = count

            count += 1

        if c == ")":
            count -= 1

            if _index == count:
                return i

assert solve(t, 10) == 79
