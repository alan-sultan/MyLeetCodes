class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while(l < r):
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans
        