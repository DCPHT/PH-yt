#
# Two Sum
# Solution 1:
# Time complexity: O(n^2)
# Space complexity: O(1)
def twoSumN2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Solution 2:
# Time complexity: O(nlogn)
# Space complexity: O(1)
# If all number in nums is unique, we can use this solution
def twoSumNlogn(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    sorted_nums = sorted(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        if sorted_nums[l] + sorted_nums[r] == target:
            break
        elif sorted_nums[l] + sorted_nums[r] < target:
            l += 1
        else:
            r -= 1
    # Find the index of the two numbers in the original array
    for i in range(len(nums)):
        if nums[i] == sorted_nums[l]:
            l = i
            break
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == sorted_nums[r]:
            r = i
            break
    return [l, r]


# Solution 2:
# Time complexity: O(n)
# Space complexity: O(n)
def twoSumN(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    hash_map = {}
    for i, num in enumerate(nums):
        # Check if the complement is in the dictionary
        if num in hash_map:
            return [i, hash_map[num]]
        remain = target - num
        # If not, add the value and index to the dictionary
        hash_map[remain] = i
