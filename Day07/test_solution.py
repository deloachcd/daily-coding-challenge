from solution import count_unival_subtrees, TreeNode


def test_their_cases():
    '''
    my_tree:
       0
      / \
     1   0
        / \
       1   0
      / \
     1   1
    '''
    lowest_subtree = TreeNode(1, left=TreeNode(1), right=TreeNode(1))
    lower_subtree = TreeNode(0, left=lowest_subtree, right=TreeNode(0))
    my_tree = TreeNode(0, left=TreeNode(1), right=lower_subtree)

    assert count_unival_subtrees(my_tree) == 5
