"""
Tests for linked_list_reverse_sublist.py
"""

from questions.linked_list_reverse_sublist import ListNode, reverse_sublist


def list_to_nodes(lst):
    """Converts a list of integers to a LinkedList of nodes."""
    dummy = ListNode(-1)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def nodes_to_list(node):
    """Converts a LinkedList of nodes to a list of integers."""
    lst = []
    while node:
        lst.append(node.value)
        node = node.next
    return lst


def test_reverse_sublist():
    """
    Tests for reverse_sublist function.
    """

    head = list_to_nodes([1, 2, 3, 4, 5])
    expected = [1, 4, 3, 2, 5]
    result = nodes_to_list(reverse_sublist(head, 2, 4))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([1, 2, 3, 4, 5])
    expected = [5, 4, 3, 2, 1]
    result = nodes_to_list(reverse_sublist(head, 1, 5))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([1, 2])
    expected = [2, 1]
    result = nodes_to_list(reverse_sublist(head, 1, 2))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([1, 2, 3])
    expected = [1, 3, 2]
    result = nodes_to_list(reverse_sublist(head, 2, 3))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([1, 2, 3, 4])
    expected = [1, 2, 3, 4]
    result = nodes_to_list(reverse_sublist(head, 4, 4))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([5, 6, 7, 8, 9])
    expected = [9, 8, 7, 6, 5]
    result = nodes_to_list(reverse_sublist(head, 1, 5))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([1])
    expected = [1]
    result = nodes_to_list(reverse_sublist(head, 1, 1))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]
    result = nodes_to_list(reverse_sublist(head, 4, 10))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([1, 2, 3, 4, 5, 6])
    expected = [1, 6, 5, 4, 3, 2]
    result = nodes_to_list(reverse_sublist(head, 2, 6))
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_nodes([7, 6, 5, 4, 3, 2, 1])
    expected = [7, 1, 2, 3, 4, 5, 6]
    result = nodes_to_list(reverse_sublist(head, 2, 7))
    assert result == expected, f"Expected {expected}, Got {result}"
