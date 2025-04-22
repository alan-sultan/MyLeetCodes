class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count = (Counter(abs(num) for num in set(nums)))
        maxN = -1
        for key, val in count.items():
            if val == 2:
                maxN = max(maxN, key)
        return maxN