# Soltuion 1
# Time complexity: O(n^2)
# Space complexity: O(n)
def lengthOfLongestSubstring(self, s: str) -> int:
    cur = 0
    res = 0
    for i in range(len(s)):
        cur = 0
        se = set()
        for j in range(i, len(s)):
            if s[j] in se:
                res = max(res, cur)
                break
            se.add(s[j])
            cur += 1
            if j == len(s) - 1:
                res = max(res, cur)
    return res


# Solution 2
# Time complexity: O(n)
# Space complexity: O(n)
def lengthOfLongestSubstringN(s: str) -> int:
    l = 0
    res = 0
    se = set()
    for r, ch in enumerate(s):
        while l < r and ch in se:
            se.remove(s[l])
            l += 1
        se.add(ch)
        res = max(res, r - l + 1)
    return res
