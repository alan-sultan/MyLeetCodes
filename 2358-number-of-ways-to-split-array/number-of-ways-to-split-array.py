class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sumN = sum(nums)
        currS = res = 0
        for i in range(len(nums) - 1):
            currS += nums[i]
            sumN -= nums[i]
            if currS >= sumN:
                res += 1
        return res
