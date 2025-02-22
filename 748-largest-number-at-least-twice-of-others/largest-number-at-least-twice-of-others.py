class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxN = max(nums)
        index = nums.index(maxN)
        nums.remove(maxN)
        return index if max(nums) * 2 <= maxN else -1