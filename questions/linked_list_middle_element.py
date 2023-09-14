"""
Problem: Middle of the LinkedList

Description:
Given the head of a singly linked list, return the middle node. If the total number of nodes 
in the linked list is even, return the second middle node. Ensure your algorithm does not modify 
the original linked list after the function is executed.

Function Signature:
def find_middle(head: ListNode) -> ListNode:

Inputs:
    - head (ListNode): The head node of the singly linked list, with each node containing an integer value.

Returns:
    - ListNode: The middle node of the linked list.

Notes:
    - The linked list will have at least one element.
    - Do not return a new linked list. Return the middle node of the given linked list.

Examples:

1. Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
   Output: 3
   Explanation: The middle of the linked list is the third node with the value 3.

2. Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
   Output: 4
   Explanation: The linked list has an even number of nodes, so the second middle node (the fourth node) with value 4 is returned.

3. Input: 1 -> null
   Output: 1
   Explanation: The linked list has only one node, which is the middle.

Hints:
    - Build on your knowledge from "linked_list_has_cycle". Consider using two pointers to traverse the list; one moving two steps at a time and the other moving one step at a time.

Tags:
    - LinkedList
    - Two Pointers

"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head: ListNode) -> ListNode:
    # TODO: Implement the function
    if not head or not head.next:
        return head
    
    slow = head
    fast = head

    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        
    return slow
