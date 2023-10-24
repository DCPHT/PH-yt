from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def largestValues(self, root: [TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            curVal = float("-inf")
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    curVal = max(curVal, cur.val)
                    queue.append(cur.right)
                    queue.append(cur.left)

            if curVal != float("-inf"):
                res.append(curVal)
        return res
