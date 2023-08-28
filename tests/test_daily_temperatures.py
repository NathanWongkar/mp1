"""
Unit tests for daily_temperatures.py
"""

from questions.daily_temperatures import days_to_wait_for_warmer

def test_days_to_wait_for_warmer():
    """
    Tests for daily_temperatures.py
    """
    temps = [70, 73, 75, 71, 69, 72, 76, 73]
    result = days_to_wait_for_warmer(temps)
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [73, 72, 71, 70]
    result = days_to_wait_for_warmer(temps)
    expected = [0, 0, 0, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [70, 71, 72, 73]
    result = days_to_wait_for_warmer(temps)
    expected = [1, 1, 1, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [70, 70, 70, 70]
    result = days_to_wait_for_warmer(temps)
    expected = [0, 0, 0, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [73, 74, 75, 76, 77]
    result = days_to_wait_for_warmer(temps)
    expected = [1, 1, 1, 1, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [80]
    result = days_to_wait_for_warmer(temps)
    expected = [0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [80, 79, 78]
    result = days_to_wait_for_warmer(temps)
    expected = [0, 0, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [70, 73, 75, 76, 69, 72, 76, 73]
    result = days_to_wait_for_warmer(temps)
    expected = [1, 1, 1, 0, 1, 1, 0, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [80, 85, 85, 85, 90]
    result = days_to_wait_for_warmer(temps)
    expected = [1, 3, 2, 1, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"

    temps = [70, 80, 90, 100, 110, 120]
    result = days_to_wait_for_warmer(temps)
    expected = [1, 1, 1, 1, 1, 0]
    assert result == expected, f"Test Failed: Expected {expected}, Got {result}"
