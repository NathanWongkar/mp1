"""
Problem: Palindrome LinkedList

Description:
Determine whether a given singly linked list is a palindrome. A palindrome reads the same forwards and backward. 
Ensure your algorithm does not modify the original linked list after the function is executed.

Function Signature:
def is_palindrome(head: ListNode) -> bool:

Inputs:
    - head (ListNode): The head node of the singly linked list, with each node containing an integer value.

Returns:
    - bool: True if the linked list is a palindrome, and False otherwise.

Notes:
    - The linked list will have at least one element.
    
Examples:

1. Input: [2 -> 4 -> 6 -> 4 -> 2]
   Output: True
   Explanation: The linked list reads the same forwards and backward, hence it is a palindrome.

2. Input: [2 -> 4 -> 6 -> 4 -> 2 -> 2]
   Output: False
   Explanation: The linked list does not read the same when reversed.

3. Input: [1]
   Output: True
   Explanation: A single element is always a palindrome.

Hints:
    - You may need to find the middle of the linked list.
    - Consider reversing the second half of the linked list and compare it with the first half.

Tags:
    - LinkedList
    - Two Pointers
"""

from collections import deque

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    # TODO: Implement the function
    stack = deque([])

    if not head or not head.next:
        return True

    slow = head
    fast = head 

    while fast and fast.next:
        stack.append(slow.value) 
        slow = slow.next
        fast = fast.next.next
    if fast: # if odd then u skip
        slow = slow.next
    while slow:
        if slow.value != stack.pop():
            return False
        slow = slow.next           
    return True
