"""
Unit tests for search_triplets.py
"""

from questions.triplet_sum import search_triplets


def test_search_triplets():
    """
    Tests for search_triplets.py
    """
    result = search_triplets([-3, 0, 1, 2, -1, 1, -2])
    expected = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([-5, 2, -1, -2, 3])
    expected = [[-5, 2, 3], [-2, -1, 3]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([0, 0, 0, 0])
    expected = [[0, 0, 0]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([3, -2, -1, 0, 1, 1])
    expected = [[-2, -1, 3], [-2, 1, 1], [-1, 0, 1]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([1, 2, 3])
    expected = []
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([-1, 0, 1, 2])
    expected = [[-1, 0, 1]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([0, -4, 4, -2, 2, 2, 2, -2, 0])
    expected = [[-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([-2, 0, 1, 1])
    expected = [[-2, 1, 1]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    result = search_triplets([-5, 3, 2, 0])
    expected = [[-5, 2, 3]]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
