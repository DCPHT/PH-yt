# Solution 1
# Time complexity: O(n)
# Space complexity: O(n)
def longestPalindromeSet(self, s: str) -> int:
    # s = "abccccdd"
    # set = (a, b,)
    res = 0
    se = set()
    for ch in s:
        if ch in se:
            se.remove(ch)
            res += 2
        else:
            se.add(ch)

    if se:
        res += 1
    return res


# Solution 2
# Time complexity: O(n)
# Space complexity: O(n)
def longestPalindromeMap(self, s: str) -> int:
    # s = "abccccdd"
    # counter = {a: 1, b: 1, c: 4, d: 2}
    res = 0
    odd = 0
    hashmap = {}
    for ch in s:
        if ch in hashmap:
            hashmap[ch] += 1
        else:
            hashmap[ch] = 1
    for k, v in hashmap.items():
        if v % 2 != 0:
            odd += 1
        res += v

    res = res - odd + 1
    if odd == 0:
        res -= 1
    return res
