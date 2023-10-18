from typing import List


# Solution 1: Brute force
# Time complexity: O(n^2)
# Space complexity: O(1)
def maxAreaBruteForce(self, height: List[int]) -> int:
    res = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            cur = min(height[i], height[j]) * (j - i)
            res = max(res, cur)
    return res


# Solution 2: Two pointer
# Time complexity: O(n)
# Space complexity: O(1)
def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        cur = min(height[l], height[r]) * (r - l)
        res = max(res, cur)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res
