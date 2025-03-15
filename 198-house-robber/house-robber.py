class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = r2 = 0
        for num in nums:
            curr = max(num + r1, r2)
            r1 = r2
            r2 = curr
        return r2