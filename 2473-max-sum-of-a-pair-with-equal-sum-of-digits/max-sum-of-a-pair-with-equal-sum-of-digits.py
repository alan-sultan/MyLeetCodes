class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxN = [0] * 82
        ans = -1
        for num in nums:
            s = (sum(map(int, list(str(num)))))
            if maxN[s] > 0:
                ans = max(ans, maxN[s] + num)
            maxN[s] = max(maxN[s], num)
        return ans
        