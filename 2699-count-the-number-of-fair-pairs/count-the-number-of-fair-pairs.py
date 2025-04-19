class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            x = bisect_left(nums, lower - num, lo = 0, hi = i)
            y = bisect_right(nums, upper - num, lo = 0, hi = i)
            ans += y - x
        return ans