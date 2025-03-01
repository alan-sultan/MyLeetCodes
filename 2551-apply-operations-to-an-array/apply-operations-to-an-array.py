class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
                i += 1
        r = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[r] = nums[i]
                r += 1
        for i in range(r, len(nums)):
            nums[i] = 0

        return nums