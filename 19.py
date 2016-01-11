
stack1 = []
stack2 = []

def push(n):
    stack2.push(n)

# O(m)
def pop():
    if len(stack1) == 0:
        while len(stack2) > 0:
            stack1.push(stack2.pop())

    return stack1.pop()
