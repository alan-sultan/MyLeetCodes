class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sumN = 0
        for num in nums:
            if num - 10 < 0:
                sumN += num
        return True if 2 * sumN != sum(nums) else False
