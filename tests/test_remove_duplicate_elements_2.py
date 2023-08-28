"""
Unit test for remove_duplicate_elements_2.py
"""
from questions.remove_duplicate_elements_2 import remove_groups


def test_remove_groups():
    """
    Tests for remove_groups function.
    """

    s, k = "abbbaaca", 3
    expected = "ca"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "abbaccaa", 3
    expected = "abbaccaa"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "abbacccaa", 3
    expected = "abb"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "aabbbcc", 2
    expected = "bbb"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "aabbcc", 2
    expected = ""
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "aaabb", 2
    expected = "aaa"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "xyzxx", 2
    expected = "xyz"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "xyzxy", 2
    expected = "xyzxy"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "a", 2
    expected = "a"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    s, k = "aaaa", 3
    expected = "aaaa"
    result = remove_groups(s, k)
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

# This one is tough.
