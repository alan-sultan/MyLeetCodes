class Solution:
    def minElement(self, nums: List[int]) -> int:
        minN = float('inf')
        for num in nums:
            minN = min(minN, sum(map(int, str(num))))
        return minN
