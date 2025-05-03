class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sumN = n * (n + 1) // 2
        sumR = sum(nums)
        sumwR = sum(set(nums))
        return [sumR - sumwR, sumN - sumwR]