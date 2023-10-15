# Is unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Date of Creation: 10/23/2019
def isUniqueSet(strs):
    if len(strs) > 256:
        return False
    s = set()
    for i in strs:
        if i in s:
            return False
        else:
            s.add(i)
    return True


def isUniqueArray(strs):
    if len(strs) > 256:
        return False
    chars = [False] * 256
    for ch in strs:
        if chars[ord(ch)]:
            return False
        chars[ord(ch)] = True
    return True


def isUniqueSort(strs):
    strs = sorted(strs)
    for i in range(len(strs) - 1):
        if strs[i] == strs[i + 1]:
            return False
    return True


# res = isUniqueSort("abc")
res = isUniqueSort("abca")
# res = isUniqueSet("abc")
# res = isUniqueSet("abca")
# res = isUniqueArray("abc")
print(res)
