class TreeNode:
    parent = None

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def count_unival_subtrees(tree_node: TreeNode):
    def inner_count(node):
        if not (node.left or node.right):
            rval = (node.value, 1)
        else:
            left_bit, left_count = inner_count(node.left)
            right_bit, right_count = inner_count(node.right)
            if left_bit == right_bit == node.value:
                rval = (node.value, left_count + right_count + 1)
            else:
                rval = (None, left_count + right_count)
        return rval

    return inner_count(tree_node)[1]
