class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        minN, maxN = 1, max(nums)
        tot = len(nums)

        while minN < maxN:
            midN = (minN + maxN) // 2
            p = 0
            index = 0
            while index < tot:
                if nums[index] <= midN:
                    p += 1
                    index += 2  
                else:
                    index += 1

            if p >= k:
                maxN = midN
            else:
                minN = midN + 1

        return minN