# https://www.interviewcake.com/question/python/cake-thief
# NOTES:

# use linear programing
def max_duffel_bag_value(cakes, capacity):
    results = [0] * (capacity+1)

    for i in xrange(1, capacity+1):
        _max = results[i - 1]
        for weight, value in cakes:
            if weight > i:
                continue

            if value + results[i-weight] > _max:
                _max = value + results[i - weight]

        results[i] = _max

    # print results
    return results[capacity]

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

assert max_duffel_bag_value(cake_tuples, capacity) == 555
