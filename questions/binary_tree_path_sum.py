"""
Problem: Binary Tree Path Sum

Description:
Given a binary tree and a number 'S', determine if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals 'S'. 

Function Signature:
def has_path_sum(root: TreeNode, sum: int) -> bool:

Inputs:
    - root (TreeNode): The root node of the binary tree. The TreeNode is defined as:
        class TreeNode:
            def __init__(self, value=0, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right
    - sum (int): The target sum to check for from root to leaf.

Returns:
    - bool: True if there's a path from root-to-leaf with the given sum, otherwise False.

Examples:

1. Input:
        Tree Structure:
             12
           /   \
          7     1
         /     / \
        9     10  5
        Sum: 23
   Output: True 
   Explanation: The path 12 -> 1 -> 10 gives the sum 23.

2. Input:
        Tree Structure:
            12
           /  \
          1    3
        Sum: 16
   Output: False 
   Explanation: There's no path with the sum 16.

Notes:
    - Use a recursive approach to check for the sum from the root to each leaf node.
    - Reduce the sum by the node value at each level. If we reach a leaf node and the sum is 0, then there's a valid path.

Tags:
    - Trees
    - Recursion
"""

from typing import List


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, target: int) -> bool:
    # TODO Implement me
    if not root:
        return False
    if not root.left and not root.right:
        target = target-root.value
        if target == 0:
            return True 
    if root.left and has_path_sum(root.left, target - root.value):
        return True
    if root.right and has_path_sum(root.right, target - root.value):
        return True    
    return False



