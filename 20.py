# https://www.interviewcake.com/question/python/largest-stack

# O(1)
class Stack:
    # initialize an empty list
    def __init__(self):
        self.items = []
        self.current_max = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)
        if item > self.current_max[-1]:
            self.current_max.append(item)
        else:
            self.current_max.append(self.current_max[-1])

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        self.current_max.pop()
        return self.items.pop()

    # see what the last item is
    def peek(self):
        # if the stack is empty, return None
        if not self.items: return None

        return self.items[len(self.items)-1]

    def get_max(self):
        return self.current_max[-1]
