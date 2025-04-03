class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans, x, y = 0, 0, 0
        for k in range(n):
            ans = max(ans, y * nums[k])
            y = max(y, x - nums[k])
            x = max(x, nums[k])
        return ans