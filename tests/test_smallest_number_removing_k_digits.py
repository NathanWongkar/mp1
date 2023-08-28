"""
Unit tests for remove_k_digits.py
"""
from questions.smallest_number_removing_k_digits import remove_k_digits


def test_remove_k_digits():
    """
    Tests for remove_k_digits.py
    """
    result = remove_k_digits("1432219", 3)
    expected = "1219"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("10200", 1)
    expected = "200"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("1901042", 4)
    expected = "2"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("12345", 3)
    expected = "12"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("4321", 2)
    expected = "21"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("100023", 3)
    expected = "0"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("22222", 4)
    expected = "2"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("1001", 3)
    expected = "0"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("11112", 1)
    expected = "1111"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = remove_k_digits("98765", 1)
    expected = "8765"
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
