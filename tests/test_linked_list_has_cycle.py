"""
Unit tests for linked_list_has_cycle.py
"""
from questions.linked_list_has_cycle import has_cycle, ListNode


def list_to_nodes_with_cycle(lst, cycle_start_index=None):
    """
    Converts a list of values to a linked list and returns the head.
    Optionally, you can specify an index to introduce a cycle in the list.
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    nodes = [head]

    for val in lst[1:]:
        new_node = ListNode(val)
        current.next = new_node
        nodes.append(new_node)
        current = new_node

    # Introducing a cycle if an index is given
    if cycle_start_index is not None:
        current.next = nodes[cycle_start_index]

    return head


def test_has_cycle():
    """
    Tests for linked_list_has_cycle.py
    """
    result = has_cycle(list_to_nodes_with_cycle([1, 2, 3], 0))
    expected = True
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle([1, 2, 3]))
    expected = False
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle([1]))
    expected = False
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle([1, 2, 3, 4, 5, 6], 3))
    expected = True
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle([1, 2, 3, 4, 5, 6]))
    expected = False
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle([10, 20, 30, 40, 50], 2))
    expected = True
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle(
        [10, 20, 30, 40, 50, 60, 70, 80, 90]))
    expected = False
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle(
        [11, 22, 33, 44, 55, 66, 77], 5))
    expected = True
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle(
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7))
    expected = True
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = has_cycle(list_to_nodes_with_cycle([2, 4, 6, 8, 10, 12]))
    expected = False
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
