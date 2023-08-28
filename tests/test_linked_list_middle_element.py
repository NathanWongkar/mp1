"""
Unit tests for linked_list_middle_element.py
"""
from questions.linked_list_middle_element import find_middle, ListNode

def list_to_nodes(lst):
    """Converts a list of values to a linked list and returns the head."""
    if not lst: return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_find_middle():
    """
    Tests for linked_list_middle_element.py
    """
    result = find_middle(list_to_nodes([1, 2, 3, 4, 5])).value
    expected = 3
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([1, 2, 3, 4, 5, 6])).value
    expected = 4
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([1])).value
    expected = 1
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([1, 2])).value
    expected = 2
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([1, 2, 3])).value
    expected = 2
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([1, 2, 3, 4])).value
    expected = 3
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([10, 20, 30, 40, 50, 60, 70, 80, 90])).value
    expected = 50
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([11, 22, 33, 44, 55, 66, 77])).value
    expected = 44
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])).value
    expected = 11
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = find_middle(list_to_nodes([2, 4, 6, 8, 10, 12])).value
    expected = 8
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
