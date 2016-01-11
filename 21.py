# https://www.interviewcake.com/question/python/find-unique-int-among-duplicates
# NOTES XOR

# O(n) space
def solve(alist):
    s = set()
    for i in alist:
        if i in s:
            s.remove(i)
        else:
            s.add(i)

    return s.pop()

def find_unique_delivery_id(delivery_ids):

    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    # print unique_delivery_id
    return unique_delivery_id

print find_unique_delivery_id([1,3,1, 2, 2,4,4,3,1, 130, 330, 130,330])
