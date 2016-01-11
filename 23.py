# https://www.interviewcake.com/question/python/linked-list-cycles

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

# O(n) time, O(n) space
def solve(node):
    x = set()

    while True:
        if node in x:
            return True

        if node.next == None:
            return False

        x.add(node)
        node = node.next

# O(n) time, O(1) space
def solve(node):
    p1 = node
    p2 = node

    while True:
        if p1 == p2 and p1.next and p2.next:
            return True

        try:
            p1 = p1.next
            p2 = p2.next.next
        except:
            return False

# find the loop
def solve(node):
    p1 = node
    p2 = node

    while True:
        if p1 == p2 and p1.next and p2.next:
            break

        try:
            p1 = p1.next
            p2 = p2.next.next
        except:
            return False

    p1 = node
    while True:
        if p1 == p2:
            return p1

        p1 = p1.next
        p2 = p2.next
