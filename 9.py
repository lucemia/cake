# https://www.interviewcake.com/question/python/bst-checker

# a binary search tree we can print the node in order
# if the order is sorted, than it is
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


def order(node):
    x = []
    if node.left:
        x = order(node.left)

    x.append(node.value)

    if node.right:
        x.extend(order(node.right))

def solve(tree):
    node_list = order(tree)

    x = node_list[0]
    for i in range(1, len(node_list)):
        if node_list[i] < x:
            return False

        x = node_list[i]

    return True

# for O(lgN) space
def solve(node):
    try:
        test(node)
        return True
    except:
        return False


def test(node):
    if node.left:
        l_min, _max = order(node.left)

        if _max > node.value:
            raise Exception()

    if node.right:
        _min, r_max = order(node.right)

        if _min < node.value:
            raise Exception()

    return l_min, r_max

