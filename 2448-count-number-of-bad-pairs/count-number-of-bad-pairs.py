class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = {}
        gPairs = 0
        for i, num in enumerate(nums):
            gPairs += count.get(num - i, 0)
            count[num - i] = count.get(num - i, 0) + 1
            
        n = len(nums)
        sumM = n*(n - 1)//2
        
        return sumM - gPairs