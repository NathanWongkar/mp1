"""
Problem: Triplets Sum to Zero

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Function Signature:
def search_triplets(arr: List[int]) -> List[List[int]]:

Parameters:
    arr : List[int]
        - A list of unsorted integers.

Returns:
    List[List[int]]
        - A list containing all unique triplets whose sum is equal to zero.
        - Each triplet should be a list of three integers.
        - The triplets should be ordered such that the lists representing them are in ascending order. 
        - The order of the triplets in the main list does not matter.

Examples:
1. Input: arr = [-3, 0, 1, 2, -1, 1, -2]
   Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

2. Input: arr = [-5, 2, -1, -2, 3]
   Output: [[-5, 2, 3], [-2, -1, 3]]

Note:
The function should be able to handle the cases where there are multiple triplets with the sum of zero, as shown in the examples above.

Hints: 
  - Build on top of your two sum solution
  - Make sure to handle duplicates properly

Tags:
  - Array
  - Two Pointers
"""

from typing import List


def search_triplets(arr: List[int]) -> List[List[int]]:
    # TODO: Implement the function
    return [[0]]
