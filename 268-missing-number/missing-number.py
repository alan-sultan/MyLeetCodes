class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # return (n * (n + 1)) // 2 - sum(nums)
        ans = 0
        for i, num in enumerate(nums):
            ans ^= (i + 1)
            ans ^= num
        return ans