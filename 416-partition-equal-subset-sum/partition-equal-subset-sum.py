class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        tr = total // 2
        ans = [False] * (tr + 1)
        ans[0] = True

        for num in nums:
            for i in range(tr, num - 1, -1):
                ans[i] = ans[i] or ans[i - num]

        return ans[tr]