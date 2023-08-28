"""
Problem: Dutch National Flag Sorting

Description:
Given an array containing only integers 0, 1, and 2, sort the array in-place without using any additional storage. This problem is also known as the Dutch National Flag Problem due to its similarity to the Dutch flag that consists of three colors: red, white, and blue.

Function Signature:
def sort_array(arr: List[int]) -> None:

Inputs:
    - arr (List[int]): A list containing integers which are only 0, 1, and 2.

Returns:
    - None: The function should sort the array in-place without returning any value.

Notes:
    - The input array should be sorted in-place without using any extra memory.
    - Ensure that the solution is efficient and does not use counting of 0s, 1s, and 2s to recreate the array.
    
Examples:

1. Input: [1, 0, 2, 1, 0]
   Output: [0, 0, 1, 1, 2]
   Explanation: The input array is sorted in ascending order.

2. Input: [2, 2, 0, 1, 2, 0]
   Output: [0, 0, 1, 2, 2, 2]
   Explanation: The input array is sorted in ascending order.

3. Input: [1]
   Output: [1]
   Explanation: The input array contains only one element and is already sorted.

Hints:
    - Consider using a two-pointer technique to segregate 0s, 1s, and 2s.
    - You may need to swap the values at different indices in the array for sorting.

Tags:
    - Array
    - Two Pointers
"""

from typing import List

def sort_array(arr: List[int]) -> None:
    # TODO: Implement the function
    return None
