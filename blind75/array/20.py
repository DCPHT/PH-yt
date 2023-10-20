# Solution
# Time complexity: O(n)
# Space complexity: O(n)
def isValid(self, s: str):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    paren = {"(": ")", "[": "]", "{": "}"}
    for ch in s:
        if ch in paren:
            stack.append(ch)
        elif stack:
            pre = stack.pop()
            if paren[pre] != ch:
                return False
        else:
            return False

    if len(stack) == 0:
        return True
    return False
