"""
Unit tests for remove_duplicate_letters.py
"""
from questions.remove_duplicate_letters import remove_adjacent_dups


def test_remove_adjacent_dups():
    """
    Tests for remove_adjacent_dups.py
    """

    result = remove_adjacent_dups("abccba")
    expected = ""
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("foobar")
    expected = "fbar"
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("abcd")
    expected = "abcd"
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("aabbcc")
    expected = ""
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("abbacca")
    expected = "a"
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("zzzyz")
    expected = "zyz"
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("xyzzyx")
    expected = ""
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("xxyyyzzz")
    expected = "yz"
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("abccbadef")
    expected = "def"
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"

    result = remove_adjacent_dups("a")
    expected = "a"
    assert result == expected, f"Test Failed: Expected '{expected}', Got '{result}'"
