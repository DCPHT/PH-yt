from typing import List


# Solution 1: Use a stack to store the numbers
# Time complexity: O(n)
# Space complexity: O(n)
def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    operators = ["+", "-", "*", "/"]
    for token in tokens:
        if token in operators:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            cur = 0
            if token == "+":
                cur = num2 + num1
            elif token == "-":
                cur = num2 - num1
            elif token == "*":
                cur = num2 * num1
            else:
                cur = int(num2 / num1)
            stack.append(cur)
        else:
            stack.append(token)

    return int(stack[0])
