class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dic = {}
        ans = 0
        for i, num in enumerate(nums):
            if num in dic and dic[num] >= 3 * ans:
                ans = math.ceil((dic[num] + 1) / 3)
            dic[num] = i
        return ans