class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2:
                r -= 1
            elif nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums
