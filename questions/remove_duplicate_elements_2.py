"""
Problem: Remove Groups of Identical Characters

Given a string `s` and an integer `k`, the task is to remove groups of consecutive, identical characters 
from the string such that each group contains exactly `k` characters. Continue removing such groups 
until no more removals can be made. Return the resulting string after all possible removals.

Function Signature:
def removeGroups(s: str, k: int) -> str:

Inputs:
    - s (str): A string containing any characters.
    - k (int): The size of groups of identical characters to be removed.

Returns:
    - str: The modified string after removing groups of consecutive, identical characters.

Examples:

1. Input: s = "abbbaaca", k = 3
   Output: "ca"
   Explanation: Initially, the string contains "bbb". Removing it results in "aaaca". 
   Next, "aaa" is removed to leave "ca".

2. Input: s = "abbaccaa", k = 3
   Output: "abbaccaa"
   Explanation: The string doesn't have any group of 3 consecutive identical characters.

3. Input: s = "abbacccaa", k = 3
   Output: "abb"
   Explanation: "ccc" is removed first to yield "abbaaa". Then, "aaa" is removed, resulting in "abb".

Hints:
    - Consider iterating through the string to identify and remove the qualifying groups.
    - Use a loop to ensure that removals continue until no more can be made.

Tags:
    - String
"""
def remove_groups(s: str, k: int) -> str:
    while True:
        start = 0
        end = 0
        found = False
        new_s = []
        
        while end < len(s):
            # Move 'end' pointer to find the end of a group
            while end < len(s) and s[start] == s[end]:
                end += 1

            # If group size is equal to k, skip appending it to the new string
            if end - start == k:
                found = True
            else:
                new_s.append(s[start:end])

            start = end

        s = ''.join(new_s)

        # If no group of size k is found, break
        if not found:
            break

    return s

