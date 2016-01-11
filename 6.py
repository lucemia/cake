# https://www.interviewcake.com/question/python/rectangular-love

def inter(a, b, c, d):
    if a <= c <= b:
        return c, min(b, d)
    if c <= a <= d:
        return a, min(b, d)

    return 0, 0


def solve(rect1, rect2):
    min_x, max_x = inter(rect1["x"], rect1["x"] + rect1["width"], rect2["x"], rect2["x"] + rect2["width"])
    min_y, max_y = inter(rect1["y"], rect1["y"] + rect1["height"], rect2["y"], rect2["y"] + rect2["height"])

    if min_x == max_x == 0:
        return {}

    if min_y == max_y == 0:
        return {}

    return {
        "x": min_x,
        "y": min_y,
        "width": max_x - min_x,
        "height": max_y - min_y
    }

