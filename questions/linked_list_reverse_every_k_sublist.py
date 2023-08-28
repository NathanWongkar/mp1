"""
Problem: Reverse every K-element Sub-list

Description:
Given a linked list, reverse its nodes in k-sized chunks. If the total number of nodes in the list is not a multiple of 'k', 
then reverse the remaining nodes too. If 'k' is greater than the number of nodes, reverse the whole list.
Furthermore, if, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.

Function Signature:
def reverse_every_k_elements(head: ListNode, k: int) -> ListNode:

Inputs:
    - head (ListNode): The head node of the singly linked list, with each node containing an integer value.
    - k (int): The size of each sub-list that needs to be reversed.

Returns:
    - ListNode: The head of the modified linked list after reversing every k-sized sublist.

Notes:
    - The linked list will have at least one element.
    - 'k' will always be a positive integer.
    
Examples:

1. Input: [1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8], k = 3
   Output: [3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7]
   Explanation: We reverse the first 3 elements, then the next 3, and finally the last 2.

2. Input: [1 -> 2 -> 3 -> 4 -> 5], k = 2
   Output: [2 -> 1 -> 4 -> 3 -> 5]
   Explanation: We reverse in chunks of 2, resulting in 2 reversed pairs and one single node at the end.

3. Input: [1 -> 2 -> 3 -> 4], k = 5
   Output: [4 -> 3 -> 2 -> 1]
   Explanation: 'k' is larger than the number of nodes, so the whole list is reversed.

Hints:
    - Consider breaking the list down into k-sized chunks, reversing each chunk, and then stitching them back together.
    - To reverse a k-sized chunk, you can use the standard linked list reversal technique.
    - Make sure to appropriately update the 'next' pointers to ensure the entire list remains connected.

Tags:
    - LinkedList
    - Two Pointers
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_every_k_elements(head: ListNode, k: int) -> ListNode:
    # TODO: Implement the function
    return None
