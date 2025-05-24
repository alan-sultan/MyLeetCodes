class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ths = len(nums) // 3
        ans = []
        for key, val in count.items():
            if val > ths:
                ans.append(key)
        return ans