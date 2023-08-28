"""
Unit tests for validate_expression.py
"""

from questions.validate_expression import validate_expression

def test_validate_expression():
    """
    Tests for validate_expression.py
    """

    # Test 1
    expr = "[(2+4)*6]+4"
    assert validate_expression(expr) == True, f"Test Failed: Expected True, Got {validate_expression(expr)}"

    # Test 2
    expr = "(5-6)/6}-3"
    assert validate_expression(expr) == False, f"Test Failed: Expected False, Got {validate_expression(expr)}"

    # Test 3
    expr = "[{2*4-(6/3)}]"
    assert validate_expression(expr) == True, f"Test Failed: Expected True, Got {validate_expression(expr)}"

    # Test 4
    expr = "{[5+2]*3)-4"
    assert validate_expression(expr) == False, f"Test Failed: Expected False, Got {validate_expression(expr)}"

    # Test 5
    expr = "([)]"
    assert validate_expression(expr) == False, f"Test Failed: Expected False, Got {validate_expression(expr)}"

    # Test 6
    expr = "()[]{}"
    assert validate_expression(expr) == True, f"Test Failed: Expected True, Got {validate_expression(expr)}"

    # Test 7
    expr = "[{[[(())]]}]"
    assert validate_expression(expr) == True, f"Test Failed: Expected True, Got {validate_expression(expr)}"

    # Test 8
    expr = "(]"
    assert validate_expression(expr) == False, f"Test Failed: Expected False, Got {validate_expression(expr)}"

    # Test 9
    expr = "{[(])}"
    assert validate_expression(expr) == False, f"Test Failed: Expected False, Got {validate_expression(expr)}"

    # Test 10
    expr = "{[()]}"
    assert validate_expression(expr) == True, f"Test Failed: Expected True, Got {validate_expression(expr)}"
