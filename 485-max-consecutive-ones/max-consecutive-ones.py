class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j = ans = 0
        for i, num in enumerate(nums):
            if num == 1:
                j += 1
                ans = max(ans, j)
            else:
                j = 0
        return ans