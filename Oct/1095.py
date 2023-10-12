# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        n = mountain_arr.length()
        # Phase 1: find peak
        peak = -1
        l, r = 1, n - 2
        while l <= r:
            m = (l + r) // 2
            left, right, mid = (
                mountain_arr.get(m - 1),
                mountain_arr.get(m + 1),
                mountain_arr.get(m),
            )
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                peak = m
                break
        # Search left peak
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            mid = mountain_arr.get(m)
            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return m
        # Search right peak
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            mid = mountain_arr.get(m)
            if mid < target:
                r = m - 1
            elif mid > target:
                l = m + 1
            else:
                return m
        return -1
