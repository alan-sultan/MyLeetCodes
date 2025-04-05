class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tot = 0
        for num in nums:
            tot |= num
        return tot << (len(nums) - 1)