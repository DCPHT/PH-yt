class Solution:
    def majorityElementHashTable(self, nums: List[int]) -> List[int]:
        table = {}
        major = len(nums) // 3 + 1
        res = []
        for num in nums:
            table[num] = table.get(num, 0) + 1
            if table[num] == major:
                res.append(num)

        return res

    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = -1, -1
        cnt1, cnt2 = 0, 0
        major = len(nums) // 3 + 1
        res = []
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        if cnt1 >= major:
            res.append(num1)
        if cnt2 >= major:
            res.append(num2)
        return res
