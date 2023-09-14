"""
Problem: Quadruple Sum to Target

Given an array of unsorted numbers, find all unique quadruplets in it whose sum is equal to a specified target number.

Function Signature:
def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:

Inputs:
    - arr (List[int]): A list of unsorted integers.
    - target (int): An integer representing the desired sum for the quadruplets.

Returns:
    - List[List[int]]: A list containing all unique quadruplets that sum up to the target.
        - Each quadruplet is represented as a list of four integers.
        - The quadruplets themselves are sorted in ascending order based on the integers they contain.
        - The order of the quadruplets in the main list does not matter.

Examples:

    Input: arr = [4, 1, 2, -1, 1, -3], target = 1
    Output: [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    Explanation: The provided array has two sets of numbers that sum up to 1 when taken four at a time.

    Input: arr = [2, 0, -1, 1, -2, 2], target = 2
    Output: [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    Explanation: There are two sets of numbers in the array that sum up to 2 when taken four at a time.

Hints:
    - The solution can be built on top of the three sum problem's logic.
    - Consider sorting the array first to simplify the process of finding quadruplets.

Tags:
    - Array
    - Two Pointers
"""

from typing import List

def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:
    arr.sort()
    quad_list = []
    leng = len(arr)
    
    for i in range(leng-3):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for m in range(i+1, leng-2):
            # Skip duplicates
            if m > i + 1 and arr[m] == arr[m-1]:
                continue
            for n in range(m+1, leng-1):
                for o in range(n+1, leng):
                    if arr[i] + arr[m] + arr[n] + arr[o] == target:
                        quad = [arr[i], arr[m], arr[n], arr[o]]
                        if quad not in quad_list:
                            quad_list.append(quad)

    return quad_list
