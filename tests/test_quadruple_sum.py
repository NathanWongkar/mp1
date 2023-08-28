"""
Test for quadruple_sum.py
"""

from questions.quadruple_sum import search_quadruplets


def test_search_quadruplets():
    """
    Tests for search_quadruplets function.
    """
    arr = [4, 1, 2, -1, 1, -3]
    target = 1
    expected = [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    result = search_quadruplets(arr, target)
    assert sorted(result) == sorted(
        expected), f"Expected {expected}, Got {result}"

    arr = [2, 0, -1, 1, -2, 2]
    target = 2
    expected = [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    result = search_quadruplets(arr, target)
    assert sorted(result) == sorted(
        expected), f"Expected {expected}, Got {result}"

    arr = [1, 1, 1, 1, 1]
    target = 4
    expected = [[1, 1, 1, 1]]
    result = search_quadruplets(arr, target)
    assert sorted(result) == sorted(
        expected), f"Expected {expected}, Got {result}"

    arr = []
    target = 4
    expected = []
    result = search_quadruplets(arr, target)
    assert result == expected, f"Expected {expected}, Got {result}"

    arr = [1, 2, 3, 4]
    target = 10
    expected = [[1, 2, 3, 4]]
    result = search_quadruplets(arr, target)
    assert result == expected, f"Expected {expected}, Got {result}"

    arr = [0, 0, 0, 0]
    target = 0
    expected = [[0, 0, 0, 0]]
    result = search_quadruplets(arr, target)
    assert result == expected, f"Expected {expected}, Got {result}"

    arr = [-1, 0, 1, 2, -1, -4]
    target = -1
    expected = [[-4, 0, 1, 2], [-1, -1, 0, 1]]
    result = search_quadruplets(arr, target)
    assert sorted(result) == sorted(
        expected), f"Expected {expected}, Got {result}"

    arr = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]
    target = 0
    expected = [[-5, -4, 4, 5], [-5, -3, 3, 5], [-5, -2, 2, 5], [-5, -2, 3, 4], [-5, -1, 1, 5], [-5, -1, 2, 4], [-4, -3, 2, 5], [-4, -3, 3, 4], [-4, -2, 1, 5], [-4, -2, 2, 4], [-4, -1, 1, 4], [-4, -1, 2, 3], [-3, -2, 1, 4], [-3, -2, 2, 3], [-3, -1, 1, 3], [-2, -1, 1, 2]]
    result = search_quadruplets(arr, target)
    assert sorted(result) == sorted(
        expected), f"Expected {expected}, Got {result}"

    arr = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 20
    expected = [[0, 4, 7, 9], [1, 3, 7, 9], [2, 4, 5, 9]]
    result = search_quadruplets(arr, target)
    assert sorted(result) == sorted(
        expected), f"Expected {expected}, Got {result}"

    arr = [-2, -1, 0, 0, 1, 2]
    target = 0
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    result = search_quadruplets(arr, target)
    assert sorted(result) == sorted(
        expected), f"Expected {expected}, Got {result}"
