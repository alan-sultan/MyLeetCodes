class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        l = 0
        currS = 0
        for r, num in enumerate(nums):
            currS += num

            while currS >= target:
                ans = min(ans, r - l + 1)
                currS -= nums[l]
                l += 1

        return ans if ans != float('inf') else 0