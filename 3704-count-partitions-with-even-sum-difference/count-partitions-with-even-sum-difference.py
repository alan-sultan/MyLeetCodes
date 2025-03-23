class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        return n - 1 if sum(num for num in nums) % 2 == 0 else 0