from questions.maximum_width_ramp import maxWidthRamp

def test_maxWidthRamp():
    """
    Tests for maxWidthRamp function.
    """

    nums = [6, 0, 8, 2, 1, 5]
    expected = 4
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    expected = 7
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = [9, 8, 7, 6, 5]
    expected = 0
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = [1, 2, 3, 4, 5]
    expected = 4
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = list(range(100000, 0, -1))
    expected = 0
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = list(range(50000)) + list(range(50000, 0, -1))
    expected = 99999
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = [0] * 100000
    expected = 99999
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = list(range(100000))
    expected = 99999
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = [1] * 50000 + [0] * 50000
    expected = 49999
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"

    nums = list(range(100000, 0, -2)) + [1]
    expected = 0
    result = maxWidthRamp(nums)
    assert result == expected, f"Expected {expected}, Got {result}"
