class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if int(log10(num)) % 2 == 1)

            

