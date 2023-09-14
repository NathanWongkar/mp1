r"""
Problem: Zigzag Level Order Traversal of Binary Tree

Description:
Given a binary tree, populate an array to represent its zigzag level order traversal. Populate the values of all nodes of the first level from left to right, then right to left for the next level, and keep alternating in the same manner for the subsequent levels.

Function Signature:
def zigzag_level_order_traversal(root: TreeNode) -> List[List[int]]:

Inputs:
    - root (TreeNode): The root node of the binary tree. The TreeNode is defined as:
        class TreeNode:
            def __init__(self, value=0, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right

Returns:
    - List[List[int]]: A list where each inner list contains the values of the nodes for each level in a zigzag order.

Examples:

1. Input:
        Tree Structure:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
   Output: [[1], [3, 2], [4, 5, 6, 7]]

2. Input:
        Tree Structure:
           12
         /    \
        7     1
       /     / \
      9     10  5
   Output: [[12], [1, 7], [9, 10, 5]]

Notes:
    - Use a queue for BFS. Process each level of nodes, reversing the order for every other level to achieve the zigzag pattern.
    - A flag can be used to indicate the direction of traversal at each level (left-to-right or right-to-left).

Tags:
    - Trees
    - Queue
"""

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_level_order_traversal(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    # TODO: Implement the BFS algorithm with zigzag order to populate the result list
    result = []
    queue = deque([root])
    flag = True
    while queue: #while queue is not emptu
        level_size = len(queue)
        current_lvl = []

        for i in range(level_size):
            node = queue.popleft()
            current_lvl.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if flag:
            result.append(current_lvl)
        else:
            result.append(current_lvl[::-1])
        flag = not flag
    return result
