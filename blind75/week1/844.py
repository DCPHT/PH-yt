# Solution 1:
# Time complexity: O(n)
# Space complexity: O(n)
def backspaceCompare(self, s: str, t: str) -> bool:
    # s = "ab#c", t = "ad#c"
    s1, s2 = [], []
    for ch in s:
        if s1 and ch == "#":
            s1.pop()
        elif ch != "#":
            s1.append(ch)

    for ch in t:
        if s2 and ch == "#":
            s2.pop()
        elif ch != "#":
            s2.append(ch)

    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


# Solution 2:
# Time complexity: O(n)
# Space complexity: O(1)
def backspaceCompare(self, s: str, t: str) -> bool:
    # s = "ab#c", t = "ad#c"
    def findchar(se, end):
        space = 0
        while end >= 0:
            if se[end] == "#":
                space += 1
            elif space > 0:
                space -= 1
            else:
                break
            end -= 1
        return end

    lens, lent = len(s) - 1, len(t) - 1
    while lens >= 0 or lent >= 0:
        lens = findchar(s, lens)
        lent = findchar(t, lent)
        if lens < 0 and lent < 0:
            return True
        if lens < 0 or lent < 0:
            return False
        if s[lens] != t[lent]:
            return False
        lens, lent = lens - 1, lent - 1
    return True
