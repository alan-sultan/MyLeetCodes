class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maxL = 1
        l = 0
        usedB = 0
        
        for r in range(len(nums)):
            while usedB & nums[r] != 0:
                usedB ^= nums[l]
                l += 1
                
            usedB |= nums[r]
            maxL = max(maxL, r - l + 1)
            
        return maxL