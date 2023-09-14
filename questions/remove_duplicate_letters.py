"""
Problem: Remove Adjacent Duplicates Recursively

Given a string `s`, continuously remove all adjacent duplicate characters from the string. The removal process should be repeated until no more removals can be made.

Function Signature:
def remove_adjacent_dups(s: str) -> str:

Inputs:
    - s (str): A string containing any characters.
    
Returns:
    - str: The modified string after recursively removing all adjacent duplicates.

Examples:

1. Input: s = "abccba"
   Output: ""
   Explanation: First, we remove "cc" to get "abba". Then, we remove "bb" to get "aa". Finally, we remove "aa" to get an empty string.

2. Input: s = "foobar"
   Output: "fbar"
   Explanation: We remove "oo" to get "fbar".

3. Input: s = "abcd"
   Output: "abcd"
   Explanation: No adjacent duplicates so no changes.

Constraints:
- 1 <= s.length <= 10^4

Hints:
    - Use a stack to keep track of characters in the string and pop characters when they are the same as the top of the stack.
    - Iterate over the string, pushing characters onto the stack until a duplicate is found.

Tags:
    - Stack
    - String
"""

from collections import deque

def remove_adjacent_dups(s: str) -> str:
    # TODO: Implement the function
    str_length = len(s)
    queue = deque([]) 
    if str_length == 0:
        return ""
    for char in s:
        if queue and (char == queue[-1]):
            queue.pop()
        else:
            queue.append(char)
    

    return "".join(queue)
