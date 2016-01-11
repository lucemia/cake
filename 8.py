# https://www.interviewcake.com/question/python/balanced-binary-tree

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def max_depth(tree):
    return max(max_depth(self.left), max_depth(self.right)) + 1

def min_depth(tree):
    return min(min_depth(self.left), min_depth(self.right)) + 1

def solve(tree):
    return max_depth(tree) - min_depth(tree) <= 1

