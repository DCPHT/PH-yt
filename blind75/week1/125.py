# Solution
# Time complexity: O(n)
# Space complexity: O(1)
def isPalindrome(self, s: str) -> bool:
    # s = "A man, a plan, a canal: Panama"
    #        l                         r
    def isAlphaNum(ch):
        if (ord(ch) >= ord("a") and ord(ch) <= ord("z")) or (
            ord(ch) >= ord("0") and ord(ch) <= ord("9")
        ):
            return True
        return False

    s = s.lower()
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not isAlphaNum(s[l]):
            l += 1
        while l < r and not isAlphaNum(s[r]):
            r -= 1
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True
