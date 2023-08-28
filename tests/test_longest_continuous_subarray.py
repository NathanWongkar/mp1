"""
Unit tests for longest_continuous_subarray.py
"""

from time import time
from questions.longest_continuous_subarray import longest_subarray


def test_longest_subarray():
    """
    Tests for longest_subarray.py
    """

    result = longest_subarray([8, 2, 4, 7], 4)
    expected = 2
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = longest_subarray([10, 1, 2, 4, 7, 2], 5)
    expected = 4
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = longest_subarray([4, 2, 2, 2, 4, 4, 2, 2], 0)
    expected = 3
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = longest_subarray([1, 2, 3, 4, 5], 0)
    expected = 1
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    nums = [1] * 10**5
    start_time = time()
    result = longest_subarray(nums, 0)
    end_time = time()
    assert result == len(nums), f"Test Failed: Expected '{len(nums)}', Got '{result}'"
    assert end_time - start_time < 2, "Test 5 exceeded time limit."

    nums = list(range(10**5))
    start_time = time()
    result = longest_subarray(nums, 2)
    end_time = time()
    assert result == 3, f"Test Failed: Expected '3', Got '{result}'"
    assert end_time - start_time < 2, "Test 6 exceeded time limit."

    nums = list(range(10**5))
    start_time = time()
    result = longest_subarray(nums, 100000)
    end_time = time()
    assert result == len(nums), f"Test Failed: Expected '{len(nums)}', Got '{result}'"
    assert end_time - start_time < 2, "Test 7 exceeded time limit."

    nums = [(-1)**i * i for i in range(10**5)]
    start_time = time()
    result = longest_subarray(nums, 2)
    end_time = time()
    assert result == 2, f"Test Failed: Expected '2', Got '{result}'"
    assert end_time - start_time < 2, "Test 8 exceeded time limit."

    nums = [1] * (10**5 - 1) + [10**5]
    start_time = time()
    result = longest_subarray(nums, 10**5)
    end_time = time()
    assert result == len(nums), f"Test Failed: Expected '{len(nums)}', Got '{result}'"
    assert end_time - start_time < 2, "Test 9 exceeded time limit."

    nums = [i % 3 for i in range(10**5)]
    start_time = time()
    result = longest_subarray(nums, 2)
    end_time = time()
    assert result == len(nums), f"Test Failed: Expected '{len(nums)}', Got '{result}'"
    assert end_time - start_time < 2, "Test 10 exceeded time limit."
