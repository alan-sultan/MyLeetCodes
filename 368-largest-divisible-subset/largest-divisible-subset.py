class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        maxS, maxI = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > maxS:
                        maxS = dp[i]
                        maxI = i

        res = []
        num = nums[maxI]
        for i in range(maxI, -1, -1):
            if num % nums[i] == 0 and dp[i] == maxS:
                res.append(nums[i])
                num = nums[i]
                maxS -= 1

        return res