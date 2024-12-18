class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumd = sum(map(int,''.join(map(str,nums))))
        return (sum(nums) -sumd)

