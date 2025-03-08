class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = [0, 0]
        for val in count.values():
            d, r = divmod(val, 2)
            ans[0] += d
            ans[1] += r
        return ans