"""
Problem: Maximum Width Ramp

Given an integer array nums, a ramp in nums is defined by a pair (i, j) where i < j and nums[i] <= nums[j]. The width 
of such a ramp is j - i. This problem requires finding the maximum width of a ramp in nums. If there isn't any ramp 
in nums, the function should return 0.

Function Signature:
def maxWidthRamp(nums: List[int]) -> int:

Inputs:
    - nums (List[int]): A list of integers representing the given array.

Returns:
    - int: The maximum width of a ramp in nums. If no ramp is found, return 0.

Examples:

    Input: nums = [6,0,8,2,1,5]
    Output: 4
    Explanation: The maximum width ramp can be observed at (i, j) = (1, 5): where nums[1] = 0 and nums[5] = 5.

    Input: nums = [9,8,1,0,1,9,4,0,4,1]
    Output: 7
    Explanation: The maximum width ramp can be observed at (i, j) = (2, 9): where nums[2] = 1 and nums[9] = 1.

Tags:
    - Stack
"""

from typing import List


def maxWidthRamp(nums: List[int]) -> int:
    # TODO: Implement the function
    return 0
