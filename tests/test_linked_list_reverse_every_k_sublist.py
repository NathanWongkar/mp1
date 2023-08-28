"""
Test cases for linked_list_reverse_every_k_sublist.py
"""
from questions.linked_list_reverse_every_k_sublist import reverse_every_k_elements, ListNode


def test_reverse_every_k_elements():
    """
    Tests for reverse_every_k_elements function.
    """

    # Helper function to convert list to linked list
    def list_to_linkedlist(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert linked list to list
    def linkedlist_to_list(node):
        lst = []
        while node:
            lst.append(node.value)
            node = node.next
        return lst

    head = list_to_linkedlist([1, 2, 3, 4, 5, 6, 7, 8])
    expected = [3, 2, 1, 6, 5, 4, 8, 7]
    result = linkedlist_to_list(reverse_every_k_elements(head, 3))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4, 5])
    expected = [2, 1, 4, 3, 5]
    result = linkedlist_to_list(reverse_every_k_elements(head, 2))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4])
    expected = [4, 3, 2, 1]
    result = linkedlist_to_list(reverse_every_k_elements(head, 5))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1])
    expected = [1]
    result = linkedlist_to_list(reverse_every_k_elements(head, 1))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9])
    expected = [3, 2, 1, 6, 5, 4, 9, 8, 7]
    result = linkedlist_to_list(reverse_every_k_elements(head, 3))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([5, 4, 3, 2, 1])
    expected = [1, 2, 3, 4, 5]
    result = linkedlist_to_list(reverse_every_k_elements(head, 5))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4, 5])
    expected = [3, 2, 1, 5, 4]
    result = linkedlist_to_list(reverse_every_k_elements(head, 3))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
    result = linkedlist_to_list(reverse_every_k_elements(head, 2))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3])
    expected = [2, 1, 3]
    result = linkedlist_to_list(reverse_every_k_elements(head, 2))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = linkedlist_to_list(reverse_every_k_elements(head, 10))
    assert result == expected, f"Expected {expected}, Got {result}"
