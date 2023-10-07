class Solution:
    def majorityElementHashTable(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            if cnt[num] > n // 2:
                return num

    def majorityElement(self, nums: List[int]) -> int:
        res = -1
        cnt = 0
        for num in nums:
            if num == res:
                cnt += 1
            elif cnt == 0:
                res = num
            else:
                cnt -= 1
        return res
