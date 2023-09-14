"""
Problem: Cycle in a Singly LinkedList

Description:
Given the head of a Singly LinkedList, determine if the LinkedList has a cycle in it. The algorithm should detect cycles in the linked list efficiently without using any additional storage.

Function Signature:
def has_cycle(head: ListNode) -> bool:

Inputs:
    - head (ListNode): The head of the singly linked list.

Returns:
    - bool: True if there is a cycle in the linked list, False otherwise.

Notes:
    - You should not modify the original linked list after the function is executed.
    - Ensure that the function can detect cycles efficiently without using any additional storage.

Examples:

1. Input: 1 -> 2 -> 3 -> 1 (cycle)
   Output: True
   Explanation: The linked list has a cycle as the third node points back to the first node.

2. Input: 1 -> 2 -> null
   Output: False
   Explanation: The linked list does not have a cycle.

3. Input: 1 -> null
   Output: False
   Explanation: The linked list has only one node and does not have a cycle.

Hints:
    - Consider using the two-pointer technique. You can have one pointer that moves two steps at a time and another that moves one step at a time. If there's a cycle, the two pointers are bound to meet.

Tags:
    - LinkedList
    - Two Pointers
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head: ListNode) -> bool:
    # TODO: Implement the function
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

