class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for bit in range(1 << n):
            an = []
            for i in range(n):
                if bit & (1 << i):
                    an.append(nums[i])
            ans.append(an)
        return ans

