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
    arr.sort()
    triplets_list = []
    leng = len(arr)
    current_list = []
    target = 0 

    for m in range(leng-2):
      current_list = []
      if m > 0 and arr[m] == arr[m-1]:
        continue
      for n in range(m+1, leng-1):
         temp_sum = arr[n] + arr[m]
         for o in range (n+1, leng):
            if temp_sum + arr[o] == 0:
              current_list = [arr[m],arr[n],arr[o]]
              if current_list not in triplets_list:
                triplets_list.append(current_list)
    
      
    return triplets_list
