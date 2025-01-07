class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, val in enumerate(nums):
            res[i] = nums[(i + val) % len(nums)]
        return res