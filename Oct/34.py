# O(n)
def searchRange(nums, target):
    left, right = -1, -1
    for i, num in enumerate(nums):
        if num == target:
            left = i
            while right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
            break
    return [left, right]


# O(logn)
def searchRange(nums, target):
    def binsearch(nums, target, isLeft):
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                idx = m
                if isLeft:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return idx

    left = binsearch(nums, target, True)
    right = binsearch(nums, target, False)
    if left == -1:
        return [-1, -1]
    return [left, right]
