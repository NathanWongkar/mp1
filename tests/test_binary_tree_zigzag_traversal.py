from questions.binary_tree_zigzag_traversal import zigzag_level_order_traversal, TreeNode

def test_zigzag_level_order_traversal():
    """
    Tests for zigzag_level_order_traversal.py
    """

    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    result = zigzag_level_order_traversal(tree)
    expected = [[1], [3, 2], [4, 5, 6, 7]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(12, TreeNode(7, TreeNode(9)), TreeNode(1, TreeNode(10), TreeNode(5)))
    result = zigzag_level_order_traversal(tree)
    expected = [[12], [1, 7], [9, 10, 5]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = None
    result = zigzag_level_order_traversal(tree)
    expected = []
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(5)
    result = zigzag_level_order_traversal(tree)
    expected = [[5]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, TreeNode(12), TreeNode(20)))
    result = zigzag_level_order_traversal(tree)
    expected = [[10], [15, 5], [2, 7, 12, 20]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(1, TreeNode(2, TreeNode(3)))
    result = zigzag_level_order_traversal(tree)
    expected = [[1], [2], [3]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    result = zigzag_level_order_traversal(tree)
    expected = [[1], [2], [3]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
    result = zigzag_level_order_traversal(tree)
    expected = [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(5, None, TreeNode(10, None, TreeNode(15)))
    result = zigzag_level_order_traversal(tree)
    expected = [[5], [10], [15]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    tree = TreeNode(5, TreeNode(4, TreeNode(3)))
    result = zigzag_level_order_traversal(tree)
    expected = [[5], [4], [3]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

