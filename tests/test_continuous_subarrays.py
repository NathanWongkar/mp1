"""
Unit tests for continuous_subarrays.py
"""

import time
from questions.continuous_subarrays import count_continuous_subarrays

def test_count_continuous_subarrays():
    """
    Tests for continuous_subarrays.py
    """

    nums = [5, 4, 2, 4]
    result = count_continuous_subarrays(nums)
    expected = 8
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    nums = [1, 2, 3]
    result = count_continuous_subarrays(nums)
    expected = 6
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    nums = []
    result = count_continuous_subarrays(nums)
    expected = 0
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    nums = [5]
    result = count_continuous_subarrays(nums)
    expected = 1
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    nums = [5, 10, 15]
    result = count_continuous_subarrays(nums)
    expected = 3
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    start_time = time.time()
    nums = [1] * 100000
    result = count_continuous_subarrays(nums)
    expected = 5000050000
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
    print(f"Test 6 runtime: {time.time() - start_time}")

    start_time = time.time()
    nums = [1, 3] * 50000
    result = count_continuous_subarrays(nums)
    expected = 5000050000
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
    print(f"Test 7 runtime: {time.time() - start_time}")

    nums = list(range(1, 11))
    result = count_continuous_subarrays(nums)
    expected = 27
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    start_time = time.time()
    nums = [1, 2, 3, 4, 5] * 20000
    result = count_continuous_subarrays(nums)
    expected = 240000
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
    print(f"Test 9 runtime: {time.time() - start_time}")

    nums = [1, 4, 7, 10]
    result = count_continuous_subarrays(nums)
    expected = 4
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
    