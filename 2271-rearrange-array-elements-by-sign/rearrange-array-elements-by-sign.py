class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i = 0
        j = 1
        for num in nums:
            if num < 0:
                ans[j] = num
                j += 2
            else:
                ans[i] = num
                i += 2
        return ans