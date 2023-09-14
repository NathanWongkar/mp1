"""
Problem: Validate Parentheses Expressions with Arithmetic Operations

Description:
Given a string containing parentheses `(`, `)`, `{`, `}`, `[`, `]` and arithmetic operations `+`, `-`, `*`, `/`, determine if the input string is valid. A string is valid if:

1. Open brackets are closed by the same type of brackets in the correct order.
2. It contains only valid mathematical expressions (you don't need to evaluate the expressions).
3. It doesn't contain any unmatched or unpaired parentheses.

The function should be able to differentiate between paired brackets like "[(2+4)*6]+4" and unpaired brackets like "(5-6)/6}-3".

Implement a function using stacks to validate the string:

Function Signatures:
```
def validate_expression(s: str) -> bool:
    return False
```

Examples:

1. Input: s = "[(2+4)*6]+4"
   Output: True
   Explanation: The string has matched and paired brackets with a valid arithmetic expression.

2. Input: s = "(5-6)/6}-3"
   Output: False
   Explanation: The string has an unmatched '}' bracket.

3. Input: s = "[{2*4-(6/3)}]"
   Output: True
   Explanation: The string is correctly paired and matched.

4. Input: s = "{[5+2]*3)-4"
   Output: False
   Explanation: The string has an unmatched ')' bracket.

Notes:
    - Utilize a stack to keep track of opening brackets and ensure they match with the corresponding closing brackets.
    - The string only contains the mentioned characters and numbers; no other characters will be present.
    - An empty string is considered valid.

Tags:
    - Stack
    - String
    - Data Structures
"""

from collections import deque
def validate_expression(s: str) -> bool:
   if s == "":
        return True
   
   stack = deque([])
   opening = ['(', '{', '[']
   closing = [')', '}', ']']
   bracket_match = {')': '(', '}': '{', ']': '['}

   for c in s:
      if c in opening:
         stack.append(c)
      elif c in closing:   
         if not stack:
            return False
         if stack[-1] != bracket_match[c]:
            return False
         stack.pop()


   return not stack