"""
Test cases for linked_list_palindrome.py
"""
from questions.linked_list_palindrome import is_palindrome, ListNode


def test_is_palindrome():
    """
    Tests for is_palindrome function.
    """

    def list_to_linkedlist(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    head = list_to_linkedlist([2, 4, 6, 4, 2])
    expected = True
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([2, 4, 6, 4, 2, 2])
    expected = False
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1])
    expected = True
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2])
    expected = False
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 1])
    expected = True
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([5, 4, 3, 4, 5])
    expected = True
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([5, 5, 5, 5, 5])
    expected = True
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected = False
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 3, 2, 1])
    expected = True
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"

    head = list_to_linkedlist([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
    expected = True
    result = is_palindrome(head)
    assert result == expected, f"Expected {expected}, Got {result}"
