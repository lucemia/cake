class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

    def p(self):
        if self.next:
            print self.value, self.next.p()
        else:
            print self.value

    def insert(self, v):
        if self.next:
            self.next.insert(v)
        else:
            self.next = LinkedListNode(v)


def reverse(node):
    _prev = None

    while True:
        if node.next == None:
            node.next = _prev
            return node

        _next = node.next
        node.next = _prev
        _prev = node
        node = _next

node = LinkedListNode(1)
node.insert(2)
node.insert(3)

node.p()

reverse(node).p()

