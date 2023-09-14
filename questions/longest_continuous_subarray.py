"""
Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers and an integer limit, return the size of the longest non-empty subarray 
such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Function Signature:
def longest_subarray(nums: List[int], limit: int) -> int:

Inputs:
    - nums (List[int]): An array of integers of size n (1 <= n <= 10^5), where each integer is between 
      -10^5 and 10^5.
    - limit (int): The allowed absolute difference between any two elements of a subarray.

Returns:
    - int: The size of the longest non-empty subarray that satisfies the condition.

Examples:

    Input: nums = [8,2,4,7], limit = 4
    Output: 2
    Explanation: 
    The subarrays [2,4] and [4,7] are the longest with a maximum absolute difference 
    of 2 and 3, respectively, both of which are less than or equal to 4.

    Input: nums = [10,1,2,4,7,2], limit = 5
    Output: 4
    Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

    Input: nums = [4,2,2,2,4,4,2,2], limit = 0
    Output: 3
    Explanation: All the longest subarrays are of length 3 with absolute difference of 0: [2,2,2], [4,4,4], and [2,2,2].

Hints:
    - Consider two scenarios: when a new number gets added to the subarray, and when a number gets removed from the subarray.
    - Think of how to keep track of the maximum and minimum values in the subarray efficiently.

Tags:
    - Queue
"""

from typing import List
from collections import deque

def longest_subarray(nums: List[int], limit: int) -> int:
    max_deque, min_deque = deque(), deque()
    left, res = 0, 0
    
    for right, num in enumerate(nums):
        # Maintain the max deque
        while max_deque and max_deque[-1] < num:
            max_deque.pop()
        max_deque.append(num)

        # Maintain the min deque
        while min_deque and min_deque[-1] > num:
            min_deque.pop()
        min_deque.append(num)

        # If the current window is invalid, slide the window
        while max_deque[0] - min_deque[0] > limit:
            if nums[left] == min_deque[0]:
                min_deque.popleft()
            if nums[left] == max_deque[0]:
                max_deque.popleft()
            left += 1

        # Update the result
        res = max(res, right - left + 1)

    return res
