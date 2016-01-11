# https://www.interviewcake.com/question/python/second-largest-item-in-bst

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def largest_path(node):
    if node.right:
        return largest_path(node.right) + [node]

    else:
        return [node]

# O(1) space
def solve(tree):
    if node.right:
        x = solve(node.right)
        if len(x) == 1:
            return node.value

# O(lnN) space
def solve(tree):
    path = largest_path(tree)

    return path[-2].value
