# https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e


def kth_to_last_node(k, node):
    node_i = node
    node_j = node

    for i in xrange(k-1):
        node_j = node_j.next

    while True:
        if not node_j.next:
            print node_i.value
            return node_i.value

        node_i = node_i.next
        node_j = node_j.next


assert kth_to_last_node(2, a) == "Devil's Food"

