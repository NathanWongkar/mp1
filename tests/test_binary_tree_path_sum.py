"""
Unit tests for binary_tree_path_sum.py
"""

from questions.binary_tree_path_sum import has_path_sum, TreeNode

def test_has_path_sum():
    """
    Tests for has_path_sum.py
    """

    tree = TreeNode(12, TreeNode(7, TreeNode(9)), TreeNode(1, TreeNode(10), TreeNode(5)))
    result = has_path_sum(tree, 28)
    assert result == True, f"Test Failed: Expected True, Got {result}"

    tree = TreeNode(12, TreeNode(1), TreeNode(3))
    result = has_path_sum(tree, 16)
    assert result == False, f"Test Failed: Expected False, Got {result}"

    tree = None
    result = has_path_sum(tree, 0)
    assert result == False, f"Test Failed: Expected False, Got {result}"

    tree = TreeNode(5)
    result = has_path_sum(tree, 5)
    assert result == True, f"Test Failed: Expected True, Got {result}"

    tree = TreeNode(5)
    result = has_path_sum(tree, 10)
    assert result == False, f"Test Failed: Expected False, Got {result}"

    tree = TreeNode(5, None, TreeNode(10, None, TreeNode(15)))
    result = has_path_sum(tree, 30)
    assert result == True, f"Test Failed: Expected True, Got {result}"

    tree = TreeNode(5, TreeNode(4, TreeNode(3)))
    result = has_path_sum(tree, 10)
    assert result == False, f"Test Failed: Expected False, Got {result}"

    tree = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, TreeNode(12), TreeNode(20)))
    result = has_path_sum(tree, 17)
    assert result == True, f"Test Failed: Expected True, Got {result}"

    tree = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, TreeNode(12), TreeNode(20)))
    result = has_path_sum(tree, 100)
    assert result == False, f"Test Failed: Expected False, Got {result}"

    tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7), TreeNode(8)), TreeNode(5, TreeNode(9), TreeNode(10))), TreeNode(3, TreeNode(6)))
    result = has_path_sum(tree, 14)
    assert result == True, f"Test Failed: Expected True, Got {result}"
