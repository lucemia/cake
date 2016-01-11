# https://www.interviewcake.com/question/python/delete-node


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def delete_node(b):
    c = b.next
    b.value = c.value
    b.next = c.next

    del c

delete_node(b)
