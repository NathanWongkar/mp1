"""
Unit tests for dutch_flag.py
"""
from questions.dutch_flag import sort_array

def test_sort_array():
    """
    Tests for dutch_national_flag.py
    """
    arr = [1, 0, 2, 1, 0]
    sort_array(arr)
    expected = [0, 0, 1, 1, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [2, 2, 0, 1, 2, 0]
    sort_array(arr)
    expected = [0, 0, 1, 2, 2, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [1]
    sort_array(arr)
    expected = [1]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [2, 1, 0]
    sort_array(arr)
    expected = [0, 1, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [2, 2, 2, 1, 1, 0, 0, 0]
    sort_array(arr)
    expected = [0, 0, 0, 1, 1, 2, 2, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [0]
    sort_array(arr)
    expected = [0]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [1, 1, 0, 2, 2]
    sort_array(arr)
    expected = [0, 1, 1, 2, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [0, 1, 2, 0, 1, 2]
    sort_array(arr)
    expected = [0, 0, 1, 1, 2, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [2, 0, 2, 1, 1, 0, 2]
    sort_array(arr)
    expected = [0, 0, 1, 1, 2, 2, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"

    arr = [0, 0, 1, 1, 2, 2]
    sort_array(arr)
    expected = [0, 0, 1, 1, 2, 2]
    assert arr == expected, f"Test Failed: Expected {expected}, Got {arr}"
