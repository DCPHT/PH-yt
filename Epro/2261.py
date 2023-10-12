class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        # Using set to check distinct
        s = set()
        for i in range(len(nums)):
            # cnt is the counter to count value divisible by p
            cnt = 0

            # cur is the subarrays
            cur = ""
            for j in range(i, len(nums)):
                cur += str(nums[j])
                if nums[j] % p == 0:
                    cnt += 1
                    if cnt > k:
                        break

                # add a special character to the end of the subarray to ensure these subarray distinct
                cur += " "
                s.add(cur)
        return len(s)
