"""
Unit tests for two_sum.py
"""
from questions.two_sum import two_sum


def test_two_sum():
    """
    Tests for two_sum.py
    """

    result = two_sum([1, 2, 3, 4, 6], 6)
    expected = [1, 3]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([2, 5, 9, 11], 11)
    expected = [0, 2]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([1, 2, 3, 4, 5, 6], 11)
    expected = [4, 5]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([5, 7, 9, 10], 15)
    expected = [0, 3]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([10, 15, 20, 25], 45)
    expected = [2, 3]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([1, 10, 25, 30, 40], 41)
    expected = [0, 4]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([5, 15, 22, 30, 35], 50)
    expected = [1, 4]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([10, 12, 15, 17, 19, 21], 38)
    expected = [3, 5]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([3, 8, 12, 20], 20)
    expected = [1, 2]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = two_sum([7, 9, 11, 14, 18], 23)
    expected = [1, 3]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
