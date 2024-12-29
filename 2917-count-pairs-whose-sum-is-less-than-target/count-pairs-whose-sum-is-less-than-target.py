class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        r = len(nums) - 1
        l = 0
        res = 0
        while l < r:
            x = nums[l] + nums[r]
            if x < target:
                res += r - l
                l += 1
            else:
                r -= 1
        return res
