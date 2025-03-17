class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        ans = set()
        for num in nums:
            if num in ans:
                ans.remove(num)
            else:
                ans.add(num)
        return not ans
        